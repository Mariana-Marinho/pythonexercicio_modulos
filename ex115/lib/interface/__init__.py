"""
Funções para a criação da interface do programa
"""


def linhas():
    """
    Printa 30 underlines
    :return: não retorna
    """
    print('_'*30)


def bloco(frase):
    """
    Cria um cabeçalho com linhas
    :param frase: frase do cabeçalho
    :return: não retorna
    """
    linhas()
    print(f'{frase:^30}')
    linhas()


def leia_int(escolha):
    """
    Função que tenta receber um inteiro do usuário, caso não repete a mensagem até receber um inteiro
    :param escolha: frase ara printar na tela
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


def menu(lista):
    """
    Cria um menu na tela e retorna o número inteiro digitado pelo usuário, usando a função leia_int()
    :param lista: opções do menu, em lista
    :return: número inteiro
    """
    bloco('MENU')
    for i, v in enumerate(lista):
        print(f'\033[34m{i+1} - \033[35m{v}\033[m')
    linhas()
    escolha = leia_int('sua opção: ')
    return escolha
