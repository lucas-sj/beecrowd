"""
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no
plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles,
mostrando 4 casas decimais após a vírgula, segundo a fórmula:
Distancia =
"""
p1 = input().split()
x1 = float(p1[0])
y1 = float(p1[1])
p2 = input().split()
x2 = float(p2[0])
y2 = float(p2[1])
distancia=(x2-x1)**(2)+(y2-y1)**(2)
raiz = float(distancia) ** 0.5
print('{:.4f}'.format(raiz))