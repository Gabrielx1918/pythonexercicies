maior = 0
menor = 0
for c in range(1,6):
    metros = float(input(f'Quantos m o {c}° vai querer? '))
    if c == 1:
        maior = metros
        menor = metros
    else:
        if metros > maior:
            maior = metros
        if metros < menor:
            metros = menor
print(f'O maior ceramicado terá {maior}m, e o menor terá {menor}m')