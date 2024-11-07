from emoji import emojize
sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = input('Erro desconhecido 404, por favor realizar novamente: ').upper().strip()[0]
print(f'Sexo registrado!')