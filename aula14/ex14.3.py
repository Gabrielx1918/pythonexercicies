from time import sleep
p1 = int(input('Primeiro valor: '))
p2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print(
        '     [ 1 ] SOMAR \n     [ 2 ] MULTIPLICAR \n     [ 3 ] MAIOR \n     [ 4 ] NOVOS NUMEROS \n     [ 5 ] SAIR DO PROGRAMA ')

    op = int(input('>>>>>> Qual sua opção? '))
    if op == 1:
        print(f'A soma entre {p1} e {p2} é:', p1 + p2)
    elif op == 2:
        print(f'A multiplicação entre {p1} e {p2} é:', p1 * p2)
    elif op == 3:
        if p1 > p2:
            print(f'O maior entre {p1} e {p2} é: {p1}')
        else:
            print(f'O maior entre {p1} e {p2} é: {p2}')
    elif op == 4:
        print('Informe os numeros novamentes: ')
        sleep(1)
        p1 = int(input('Primeiro valor: '))
        p2 = int(input('Segundo valor: '))
    elif op == 5:
        print('finalizando...\n', '=-' * 20)
    else:
        print('Opção inválida, tente novamente.')
sleep(1)
print('Obrigado por participar, até a proxima!')