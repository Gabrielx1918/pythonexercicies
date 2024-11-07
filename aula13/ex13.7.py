num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[34m{c}', end=' ')
        tot += 1
    else:
        print(f'\033[31m{c}', end=' ')
if tot == 2:
    print('\n\033[mNUMERO PRIMO',end=' ')
else:
    print('\n\033[mNÃO PRIMO',end=' ')
print(f'\n\033[mO numero {num} foi divisivel {tot} vezes')