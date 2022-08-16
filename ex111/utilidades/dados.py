def leia_dinheiro(numero):
    while True:
        if numero.isdigit():
            return numero
        else:
            print(f'{numero} não é um valor monetário')
            numero = input('digite um número válido: ')