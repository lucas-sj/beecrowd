"""
Roberto precisava coletar o numero de matricula dos alunos da sua turma de engenharia de produção e engenharia hídrica para a chamada. Logo, ele teve a excelente ideia de falar para todos os seus alunos gritarem os números de chamada para seus assistentes anotarem. Obviamente, isso não deu certo, e logo a sala entrou em colapso. Todos queriam falar ao mesmo tempo, e com a competição para ver quem conseguia ir embora mais rápido, houve um principio de tumulto, com cadeiras sendo jogadas nos colegas, puxões de cabelo, e socos na cara.
Júnior como é um cara pacífico, está tentando atender todos rapidamente. Porem, como são muitas requisições, está ficando sobrecarregado. Ele então, lembrou que você sabe programar e decidiu dar uma ideia.
Todos os alunos da sala deverão dar os números de matricula e a sigla do curso em uma folha, e a chamada sera computada posteriormente. Ele precisa saber quantos alunos de cada curso compareceram. Ele tem os dados, mas infelizmente, não tem a proeficiencia necessária em programação para “codar” isso. Você poderia ajuda-lo a saber, dada uma lista de alunos, quantos são de EPR, quantos são de EHD e quantos são intrusos?
"""
while True:
    try:
        ehd = 0
        epr = 0
        intrusos = 0
        n = int(input())
        for i in range(n):
            matricula, curso = input().split()
            if curso == 'EHD':
                ehd +=1
            elif curso =='EPR':
                epr +=1
            else:
                intrusos += 1
        print(f'EPR: {epr}')
        print(f'EHD: {ehd}')
        print(f'INTRUSOS: {intrusos}')
    except:
        break
