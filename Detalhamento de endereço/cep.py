import requests

#Cores utilizadas no programa.
cores = ('\033[m',          #0-NDA
         '\033[30;47m',     #1-Preto/Branco
         '\033[37;40m'      #2-Branco/Preto
         )

#Lê o cep em que deseja saber detalhes.
cep = str(input('CEP: ')).strip()

#Se a quantidade de números no cep estiver errada, finaliza o programa.
if len(cep) != 8:
    print('CEP Inválido')
    exit()

#Tentando consultar a API do viacep fazendo com que seus valores sejam manipulaveis.
try:
    local = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
except:
    print('Erro, Site viacep fora do ar!')
else:
    local = local.json()

    #Tentando pegar os detalhes do endereço, se o cep não for válido finaliza o programa.
    try:
        rua = local['logradouro']           # <- Rua xxxxxx xxxx
        rua = rua.replace('Rua', '')        # <- xxxxxx xxxx
        rua = rua.strip()

        bairro = local['bairro']
        cidade = local['localidade']
        uf = local['uf']
        ddd = local['ddd']

    except KeyError:
        print('CEP Inválido')
        exit()

    else:
        #Titulo do programa.
        print(cores[2], end='')
        print('=' * 30)
        print('DETALHE DE ENDEREÇO'.center(30))
        print('=' * 30)
        print(cores[0], end='')

        #Informações apartir do CEP.
        print(cores[1], end='')
        print(f'Rua: {rua}')
        print(f'Bairro: {bairro}')
        print(f'Cidade: {cidade}')
        print(f'Estado: {uf}')
        print(f'DDD: ({ddd})XXXXX-XXXX')
        print(cores[0], end='')
