nomemaisvelho = ''
idademaisvelho = 0
media = 0
femeas = 0
abaixo = 0
for c in range(1, 7):
    print('-'*5, f'{c}° PESSOA', '-'*5)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    media += idade
    media = media // c
    abaixo += sexo in 'Ff'
    if sexo in 'Ff':
        femeas += idade <= 20
    if c == 1:
        idademaisvelho = idade
        nomemaisvelho = nome
    else:
        if sexo in 'Mm' and idade > idademaisvelho and nome > nomemaisvelho:
            idademaisvelho = idade
            nomemaisvelho = nome
print(f'A média de idade do grupo é: {media} anos')
print(f'O homem mais velho é {nomemaisvelho} e ele tem {idademaisvelho} anos.')
print(f'No grupo tem {abaixo} mulheres, e {femeas} mulheres tem menos de 20 anos.')