import funções

preco = float(input('digite o preço do produto: '))
print(f'a metade de {preco} é {funções.metade(preco)}')
print(f'o dobro de {preco} é {funções.dobro(preco)}')
print(f'aumentando 15%: {funções.aumentar(preco, 15)}')
print(f'diminuindo 12%: {funções.diminuir(preco, 12)}')
