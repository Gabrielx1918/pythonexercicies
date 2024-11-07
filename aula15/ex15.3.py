from random import randint
print('=-'*13)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*13)
while True:
    jogador = int(input('Digite um valor: '))
    cpu = randint(0,11)
    pi = input('Par ou Impar? [P/I] ')
    print('=-'*7)
    s = jogador + cpu
    if pi in "Ii":
        if s % 2 == 0:
            print(f'O jogador escolheu: {jogador}, e o CPU: {cpu}, a soma deu: {s}. Você perdeu!')
            break
        else:
            print(f'O jogador escolheu: {jogador}, e o CPU: {cpu}, a soma deu: {s}. Você ganhou!')
    if pi in 'Pp':
        if s % 2 == 0:
            print(f'O jogador escolheu: {jogador}, e o CPU: {cpu}, a soma deu: {s}. Você ganhou!')
        else:
            print(f'O jogador escolheu: {jogador}, e o CPU: {cpu}, a soma deu: {s}. Você perdeu!')
            break
