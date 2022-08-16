import funções
import ex107.funções

valor = float(input('digite um valor: '))
print(f"""
1) dobro: {funções.moeda(ex107.funções.dobro(valor))}
2) metade: {funções.moeda(ex107.funções.metade(valor))}""")
