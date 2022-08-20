"""
Programa principal
"""

from lib.interface import *
from time import sleep
from lib.arquivos import *

arquivo = 'PessoasCadastradas.txt'

if not arquivo_existe(arquivo):
    print('Arquivo não encontrado')
    criar_arquivo(arquivo)

while True:
    escolha = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Programa'])
    sleep(1)
    if escolha == 1:
        bloco('VER PESSOAS CADASTRADAS')
        ver_cadastrados(arquivo)
    elif escolha == 2:
        bloco('NOVO CADASTRO')
        nome = str(input('nome: '))
        idade = leia_int('idade: ')
        cadastrar(arquivo, nome, idade)
    elif escolha == 3:
        print(f'\n\033[31mPrograma finalizado\033[m')
        break
    else:
        print('digite uma opção válida')
    sleep(1)
