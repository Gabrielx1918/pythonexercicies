from random import choice
lista = [1,2,3,4,5,6,7,8,9,10]
sort = choice(lista)
esc = ''
s = 0
while esc != sort:
    esc = int(input('Escolha um numero de 1 a 10: '))
    sort = choice(lista)
    s += 1
    if esc != sort:
        print(f'Você errou! o PC escolheu {sort} HAHHAHA')
    else:
        print(f'Parabens você acertou porém precisou de {s} tentativas, o numero escolhido pelo pc tambem foi {sort}')
