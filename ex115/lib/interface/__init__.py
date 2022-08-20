"""
Funções para a criação da interface do programa
"""


def linhas():
    print('_'*30)


def bloco(frase):
    linhas()
    print(f'{frase:^30}')
    linhas()


def leia_int(frase):
    while True:
        escolha = input(frase)
        try:
            numero = int(escolha)
        except (ValueError, TypeError):
            print(f'\033[31mERRO: digite um número inteiro válido\033[m')
            continue
        else:
            return numero


def menu(lista):
    bloco('MENU')
    for i, v in enumerate(lista):
        print(f'\033[34m{i+1} - \033[35m{v}\033[m')
    linhas()
    escolha = leia_int('sua opção: ')
    return escolha
