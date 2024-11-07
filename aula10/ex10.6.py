num1 = int(input('Escolha um numero: '))
num2 = int(input('Escolha um numero pela segunda vez: '))
num3 = int(input('Escolha um numero pela terceira vez: '))
#Verificando o menor numero:
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
#Verificando o maior numero:
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f'O menor numero é {menor}, O maior numero é {maior}')