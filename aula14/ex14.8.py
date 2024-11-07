resp = 'S'
soma = cont = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    cont += 1
    media = soma / num
    resp = str(input('Deseja continuar? [S/N] '))
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Você digitou {cont} valores, e sua média foi {media: .2f}')
print(f'O maior numero foi {maior} e o menor foi {menor}')