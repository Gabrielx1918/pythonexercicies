inicio = int(input('Me de um numero: '))
fim = int(input('Me de um numero: '))
s = 0
if inicio % 2 == 0:
    for c in range(inicio, fim+1, 2):
        print(c, end=' ')
        s += 1
    print(f'\nEntre o que você pediu tem {s} num pares')
else:
    for c in range(inicio, fim+1, 2):
        print(c, end=' ')
        s += 1
    print(f'\nEntre o que você pediu tem {s} num impares')