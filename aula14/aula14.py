n = 1
p = 0
i = 0
while n != 0:
    n = int(input('ME de um numero: '))
    if n != 0:
        if n % 2 == 0:
            p += 1
        else:
            i += 1
print(f'Tiveram {i} nums impares e {p} nums pares')