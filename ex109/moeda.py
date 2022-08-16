def moeda(numero):
    return float(f'{numero:.2f}')


def aumentar(numero, botar, f=False):
    if f:
        numero = moeda(numero)
        return f'R$ {numero * (100 + botar) / 100}'
    else:
        return numero*(100+botar)/100


def diminuir(numero, tirar, f=False):
    if f:
        numero = moeda(numero)
        return f'R$ {numero*(100-tirar)/100}'
    else:
        return numero*(100-tirar)/100


def dobro(numero, f=False):
    if f:
        numero = moeda(numero)
        return f'R$ {numero*2}'
    else:
        return numero*2


def metade(numero, f=False):
    if f:
        numero = moeda(numero)
        return f'R$ {numero/2}'
    else:
        return numero/2
