"""
Programa Principal
Criar um menu com ver pessoas cadastradas, cadastrar e sair do programa
"""

from ex115a.interface import *
from ex115a.arquivos import *
from time import sleep

arq = 'cadastros.txt'


if not abrir_arquivo(arq):
    criar_arquivo(arq)

while True:
    escolha = menu(['Cadastrar novo usuário', 'Ver pessoas cadastradas', 'Sair do programa'])
    sleep(1)
    if escolha == 1:
        # cadastrar novo usuário
        bloco('CADASTRAR NOVO USUÁRIO')
        nome = str(input('nome: '))
        idade = leia_int('idade: ')
        cadastrar(arq, nome, idade)
    elif escolha == 2:
        # ver cadastrado
        bloco('VER CADASTRADOS')
        ver_arquivo(arq)
    elif escolha == 3:
        # sair do programa
        print(f'\n\033[31mPrograma finalizado\033[m')
        break
    else:
        print(f'\n\033[31mDigite um valor válido\033[m')
        sleep(0.5)
