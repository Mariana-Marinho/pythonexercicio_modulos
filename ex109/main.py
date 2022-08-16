"""
Modificar o ex107 para aceitar mais um parâmetro, informando se vai ser formatado ou não pela função moeda
"""
from ex109 import moeda

valor = float(input('digite um valor: '))
print(f"""
1) a metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}
2) o dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}
3) aumentando 15% de {moeda.moeda(valor)} é {moeda.aumentar(valor, 15, True)}
4) diminuindo 12% de {moeda.moeda(valor)} é {moeda.diminuir(valor, 12, True)}""")
