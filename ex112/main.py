from ex112.utilidades import moedas, dados

valor = dados.leia_dinheiro('digite o preço do produto em R$: ')
moedas.resumo(valor, 35, 22)
