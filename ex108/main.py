import funções

valor = float(input('digite um valor: '))
print(f"""
1) dobro de {funções.moeda(valor)}: {funções.moeda(funções.dobro(valor))}
2) metade de {funções.moeda(valor)}: {funções.moeda(funções.metade(valor))}""")
