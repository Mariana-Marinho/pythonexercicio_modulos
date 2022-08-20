"""
Funções que manipulam o arquivo .txt em que contém os dados dos usuários
"""


def abrir_arquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        try:
            a = open(nome, 'wt+')
            a.close()
        except Exception as erro:
            print(f'erro ao criar aquivo {nome}: {erro}')
    else:
        print('arquivo existe')
        a.close()


def ver_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except Exception as erro:
        print(f'erro ao abrir arquivo {nome}: {erro}')
    else:
        for pessoa in a:
            p = pessoa.split(';')
            p[1] = p[1].replace('\n', '')
            print(f'{p[0]:<15}{f"{p[1]} anos":>15}')


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except Exception as erro:
        print(f'erro ao abrir o arquivo {arq} para cadastrar: {erro}')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except Exception as erro:
            print(f'erro ao adicionar elementos ao arquivo: {erro}')
        else:
            print(f'{nome} registrado')
