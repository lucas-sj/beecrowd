"""
Escreva um programa que leia três valores com ponto flutuante de dupla
precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
"""
valor = input().split()
A = float(valor[0])
B = float(valor[1])
C = float(valor[2])
triangulo = (A*C)/2
circulo = (3.14159 * C**2)
trapezio = ((A + B)*C)/2
quadrado = B**2
retangulo = A*B
print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))