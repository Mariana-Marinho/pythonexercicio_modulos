def moeda(numero):
    return f'{numero:.2f}'


def aumentar(numero, botar, f=False):
    final = numero*(100+botar)/100
    return final if f is False else moeda(final)


def diminuir(numero, tirar, f=False):
    final = numero*(100-tirar)/100
    return final if f is False else moeda(final)


def dobro(numero, f=False):
    return numero*2 if f is False else moeda(numero*2)


def metade(numero, f=False):
    return numero/2 if f is False else moeda(numero/2)
