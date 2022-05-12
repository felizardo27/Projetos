from dados_moeda import *
from os import system
import platform
import urllib.request

def clear():
    if platform.system() == 'Linux':
        return system('clear')
    if platform.system() == 'Windows':
        return system('cls')
    else:
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

    titulo('Selecione o continente que deseja escolher a moeda:')
    for i, c in continentes.items():
        print(f'{i} - {c}')
    print()
    divisor('Selecione:')
    continente1 = int(input())
    prosseguir()

    titulo(f'Selecione o pais do(a) {continentes[continente1]}')
    continente_escolhido1 = verifica_continente(continente1)
    moeda_pais1 = verifica_moeda_continente(continente1)
    for i, p in continente_escolhido1.items():
        print(f'{i} - {p}')
    print()
    divisor('Selecione:')
    pais_escolhido1 = int(input()) # retonar número do pais
    moeda_pais_escolhida1 = moeda_pais1[pais_escolhido1] # capturando moeda
    prosseguir()

    #--=-=-=--=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==-=-=-=-=-=-=-=-

    titulo('Selecione o continente que deseja escolher a moeda:')
    divisor(f'Moeda do(a) {continente_escolhido1[pais_escolhido1]} para: ')
    for i, c in continentes.items():
        print(f'{i} - {c}')
    print()
    divisor('Selecione:')
    continente2 = int(input())
    prosseguir()

    titulo(f'Selecione o pais do(a) {continentes[continente2]}')
    continente_escolhido2 = verifica_continente(continente2)
    moeda_pais2 = verifica_moeda_continente(continente2)
    for i, p in continente_escolhido2.items():
        print(f'{i} - {p}')
    print()
    divisor('Selecione:')
    pais_escolhido2 = int(input()) # retonar número do pais
    moeda_pais_escolhida2 = moeda_pais2[pais_escolhido2] # capturando moeda
    prosseguir()


    divisor(f'Digite o valor em {moeda_pais_escolhida1} ({continente_escolhido1[pais_escolhido1]}) que você deseja converter para {moeda_pais_escolhida2} ({continente_escolhido2[pais_escolhido2]}).')
    valor = float(input('$'))

    ##Moeda para converter
    moeda = moeda_pais_escolhida1
    ##Moeda a ser convertida
    moeda_a_converter = moeda_pais_escolhida2

    dados = dict(get_conversao(moeda[1:-1]))

    cotacao_atual = float(dados[moeda_a_converter])

    print(f'A cotação atual é de $ {cotacao_atual:.2f} {moeda[1:-1]}')
    conversao = valor * cotacao_atual
    print(f'E o valor a ser convertido é de $ {conversao:.2f} {moeda_a_converter[1:-1]}')

    prosseguir()

    titulo(f'{nome}, você deseja realizar outra consulta?')

    op = str(input('S/N: '))
    prosseguir()
    if op.upper() == 'N':
        break


    
