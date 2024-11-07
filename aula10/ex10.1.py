from random import choice
lista = [1,2,3,4,5,6,7,8,9,10]
esc = int(input('Escolha um numero de 1 a 10: '))
sort = choice(lista)
if esc != sort:
    print(f'Você escolheu {esc}')
    print(f'Você errou! o PC escolheu {sort} HAHHAHA')
else:
    print(f'Você escolheu {esc}')
    print(f'Parabens você acertou o numero escolhido foi {sort}')