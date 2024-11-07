print('-'*30)
print('CADASTRE UMA PESSOA'.center(30))
print('-'*30)
cont18 = homi = muie20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo not in 'MF':
            print('REPITA')
    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        homi += 1
    if sexo == 'F' and idade <=20:
        muie20 += 1

    print('-'*30)

    conti = ' '
    while conti not in 'SN':
      conti = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
      if conti not in 'SN':
            print('REPITA')
    if conti in 'N':
        print(f'{cont18} pessoas são maiores de idade.')
        print(f'{homi} homens foram cadastrados.')
        print(f'{muie20} mulheres com menos de 20 anos foram cadastradas.')
        break
