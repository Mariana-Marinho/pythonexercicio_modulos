from ex111.utilidades import moeda

valor = float(input('preço: '))
mais = float(input('aumentar em %: '))
menos = float(input('diminuir em %: '))
moeda.resumo(valor, mais, menos)
