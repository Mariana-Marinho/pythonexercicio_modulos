from ex110 import moeda

valor = float(input('digite o preço do produto em R$: '))
mais = float(input('aumentá-lo em quantos %? '))
menos = float(input('diminuí-lo em quantos %? '))
moeda.resumo(valor, mais, menos)
