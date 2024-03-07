"""
Neste problema, você deverá ler 3 palavras que definem o tipo de animal
possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua
qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

VER IMAGEM NO BEECROWD https://judge.beecrowd.com/pt/problems/view/1049
"""
a = input()
b = input()
c = input()

if a == 'vertebrado':
    if b == 'ave':
        if c == 'carnivoro':
            print('aguia')
        elif c == 'onivoro':
            print('pomba')
    elif b == 'mamifero':
        if c == 'onivoro':
            print('homem')
        elif c == 'herbivoro':
            print('vaca')
elif a == 'invertebrado':
    if b == 'inseto':
        if c == 'hematofago':
            print('pulga')
        elif c == 'herbivoro':
            print('lagarta')
    elif b == 'anelideo':
        if c == 'hematofago':
            print('sanguessuga')
        elif c == 'onivoro':
            print('minhoca')
