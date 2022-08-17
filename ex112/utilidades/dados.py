def leia_dinheiro(frase):
    while True:
        numero = input(frase)
        if numero.replace(' ', '').replace(',', '').replace('.', '').isdigit():
            numero = numero.replace(' ', '').replace(',', '')
            return float(numero)
        print(f'{numero.strip()} não é um valor monetário')
