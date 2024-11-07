pri = int(input('Me diga o primeiro termo: '))
raz = int(input('Me diga sua razão: '))
termo = pri
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, ' - ', end='')
        termo += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer a mais? '))
print(f'fim, com {termo}')
