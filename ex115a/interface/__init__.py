"""
Funções que produzem a interface do programa
"""


def linhas():
    print('_'*30)


def bloco(frase):
    linhas()
    print(f'{frase:^30}')
    linhas()


def leia_int(escolha):
    """
    Função que tenta receber um inteiro do usuário, caso não repete a mensagem até receber um inteiro
    :param escolha: frase para printar na tela
    :return: número inteiro
    """
    while True:
        e = input(escolha)
        try:
            numero = int(e)
        except (ValueError, TypeError):
            print(f'\033[31mERRO: digite um número inteiro válido\033[m')
            continue
        else:
            return numero


def menu(opcoes):
    bloco('MENU')
    for i, v in enumerate(opcoes):
        print(f'\033[34m{i+1} - \033[35m{v}\033[34m')
    escolha = leia_int('\033[34mSua opção: \033[34m')
    return escolha
