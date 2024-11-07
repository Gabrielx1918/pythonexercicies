i = int(input('Um numero: '))
f = int(input('Outro numero : '))
s = 0
cont = 0
if i % 2 == 0:
    for c in range(i, f+1, 2):
        s += c
        cont += 1
    print(f'A soma de {cont} numeros pares resulta em {s}')
else:
    print('Banido')