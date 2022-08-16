def resumo(numero, aumenta, diminui):
    print('_'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('_'*30)
    print(f'{"Preço analisado:":<20}{moeda(numero):>10}')
    print(f'{"Metade do preço:":<20}{metade(numero, True):>10}')
    print(f'{"Dobro do preço:":<20}{dobro(numero, True):>10}')
    print(f'{f"{aumenta}% de aumento:":<20}{aumentar(numero, aumenta, True):>10}')
    print(f'{f"{diminui}% de redução:":<20}{diminuir(numero, diminui, True):>10}')
    print('_'*30)


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
