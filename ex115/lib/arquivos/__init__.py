"""
Funções para a manipulação do arquivo de texto
"""
from ex115.lib.interface import *

def arquivo_existe(nome):
    try:
        # função open() para abrir o arquivo, e 'rt' para ler arquivo texto
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        # open arquivo de texto, legível, e o + é para caso não exista, crie (write text +)
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'\033[31merro na criação do arquivo {nome}\033[m')
    else:
        print(f'arquivo {nome} criado com sucesso')


def ver_cadastrados(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'\033[31merro ao abrir arquivo {nome}\033[m')
    else:
        for pessoa in a:
            dado = pessoa.split(';')
            # tirando o \n entre as linhas print
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{f"{dado[1]} anos":>10}')
    finally:
        a.close()


def cadastrar(arquivo, nome='<desconhecido>', idade=0):
    try:
        # append texto
        arq = open(arquivo, 'at')
    except:
        print(f'\033[31merro ao abrir arquivo\033[m')
    else:
        try:
            arq.write(f'{nome};{idade}\n')
        except:
            print(f'\033[31merro ao escrever no arquivo\033[m')
        else:
            print(f'novo registro de {nome}')
    finally:
        arq.close()
