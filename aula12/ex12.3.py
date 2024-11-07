num1 = int(input('Me dê um numero: '))
num2 = int(input('Me dê +1 numero: '))
if num1 > num2:
    print(f'O primeiro valor é maior ({num1}).')
elif num2 > num1:
    print(f'O segundo valor é maior ({num2}).')
elif num1 == num2:
    print('Não existe valor maior, os dois são iguais!')