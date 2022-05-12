from ast import Break
from os import system
import urllib.request

def clear():
    return system('clear')

def titulo(txt):
    print('-'*len(txt))
    print(txt)
    print('-'*len(txt))
    print()

def prosseguir():
    txt = 'Pressione ENTER para prosseguir.'
    input(f'\n{txt}\n' + '-' * len(txt))
    clear()

def divisor(txt):
    print(txt)
    print('-' * len(txt))

def get_conversao(txt):
    url = "https://api.exchangerate-api.com/v4/latest/" + txt
    webUrl = urllib.request.urlopen(url)
    data = str(webUrl.read())
    dataAt = data[248:]
    dataAt = dataAt[:-3]
    dados = dict()
    aux = ''    
    p1 = ''
    for d in dataAt:
        if d not in ',':
            aux += d
        elif d == ',':
            ax = ''
            for i in aux:
                if i != ":":
                    ax += i
                if i == ":":
                    p1 = ax
                    ax = ''
            dados[p1] = ax
            aux = ''
    return dados

def moeda_escolhida(op):
    if op == 1:
        return 'USD'
    if op == 2:
        return 'EUR'
    if op == 3:
        return 'JPY'
    if op == 4:
        return 'BRL'

def moeda_para_converter(op):
    if op == 1:
        return '"USD"'
    if op == 2:
        return '"EUR"'
    if op == 3:
        return '"JPY"'
    if op == 4:
        return '"BRL"'

def outra_moeda():
    print()
    divisor('Selecione uma opção:')
    return 0

moedas = {1:"Dólar", 2:"Euro", 3:"Iene", 4:"Real"}



clear()
titulo('Seja bem-vindo ao Converter!')
prosseguir()

#Apresentação
#nome
divisor('Digite seu nome.') 
nome = str(input())
clear()
titulo(f'Seja bem-vindo(a) {nome}.')
#pais
divisor('De que país você é?')
pais = str(input())
clear()
divisor(f'Legal! Sabemos que você é do pais {pais}.')
prosseguir()

while True:

    #Comeco do programa
    titulo('Qual moeda você deseja converter')
    #mostrando moedas no dicionario moedas
    for i, m in moedas.items():
        print(f'{i} - {m}')
    print()
    divisor("Selecione")
    #escolha da moeda
    op1 = int(input())
    prosseguir()

    # Converter para qual moeda
    titulo(f'{moedas[op1]} para: ')
    for i, m in moedas.items():
        if i != op1:
            print(f'{i} - {m}')
    print()
    divisor("Selecione")
    op2 = int(input())
    prosseguir()

    divisor(f'Digite o valor do {moedas[op1]} que você deseja converter para {moedas[op2]}.')
    valor = float(input('$'))

    ##Moeda para converter
    moeda = moeda_escolhida(op1)

    ##Moeda a ser convertida
    moeda_a_converter = moeda_para_converter(op2)

    dados = dict(get_conversao(moeda))

    cotacao_atual = float(dados[moeda_a_converter])

    print(f'A cotação atual é de R${cotacao_atual}')
    print(f'E o valor a ser convertido é de {valor * cotacao_atual}')

    prosseguir()

    titulo(f'{nome}, você deseja realizar outra consulta?')

    op = str(input('S/N: '))
    prosseguir()
    if op.upper() == 'N':
        break
    
