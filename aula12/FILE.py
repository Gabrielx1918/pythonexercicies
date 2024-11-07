import random
resp = str(input('Vamos brincar de jokenpô? ')).strip().upper()
if resp == 'SIM' or resp == 'VAMOS' :
    lista = [0, 2, 5]
    print('Vamos brincar de jokenpô com numeros representando.')
    j1 = int(input('Escolha 0, 2 ou 5: '))
    j2 = random.choice(lista)
    if j1 == 5 and j2 == 0:
        print(f'Parabéns você venceu! eu escolhi {j2}')
    elif j1 == 0 and j2 == 5:
        print(f'HAHA eu venci! eu escolhi {j2}')
    elif j1 == 0 and j2 == 2:
        print(f'Parabéns você venceu! eu escolhi {j2}')
    elif j1 == 2 and j2 == 0:
        print(f'HAHA eu venci! eu escolhi {j2}')
    elif j1 == 2 and j2 == 5:
        print(f'Parabéns você venceu! eu escolhi {j2}')
    elif j1 == 5 and j2 == 2:
        print(f'HAHA eu venci! eu escolhi {j2}')
    elif j1 == j2:
        print(f'EMPATE :) eu escolhi {j2}')
else:
    print('Ok, se mudar de ideia volta aqui!')