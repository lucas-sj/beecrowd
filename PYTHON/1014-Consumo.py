"""
Calcule o consumo médio de um automóvel sendo fornecidos a distância
total percorrida (em Km) e o total de combustível gasto (em litros).
"""
X = int(input())
Y = float(input())
saida=round((X/Y),3)
print('{:.3f} km/l' .format(saida))