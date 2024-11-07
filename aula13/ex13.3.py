inicio = int(input('Me de um numero: '))
fim = int(input('Me de um numero: '))
s = 0
if inicio % 2 != 0:
    for c in range(inicio, fim+1, 2):
        if c % 3 == 0:
            s += c
    print(f'\nA soma entre seus numeros impares é {s}')
else:
    for c in range(inicio, fim+1, 2):
        if c % 3 == 0:
            s += c
    print(f'\nA soma entre seus numeros pares é {s}')