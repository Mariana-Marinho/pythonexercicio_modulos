from ex111.utilidades import moedas, dados

valor = input('digite o preço do produto em R$: ')
mais = input('aumentá-lo em quantos %? ')
menos = input('diminuí-lo em quantos %? ')
moedas.resumo(valor, mais, menos)
