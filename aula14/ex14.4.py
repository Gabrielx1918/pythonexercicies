num = int(input('Me diga um numero: '))
c = num
f = 1
while c >= 1:
    print(f'{c}', end='')
    print(' x ' if c >1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

'''EXISTE MATH FACTORIAL PARA ISSO'''