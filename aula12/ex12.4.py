print('\033[:34mOlá bom dia!')
nome = str(input('\033[mQual seu nome? '))
sexo = str(input('\033[mQual seu sexo? ')).upper()
idade = int(input('\033[mQual sua idade?'))
falta = 18 - idade
passou = idade - 19
if sexo == 'MASCULINO':
    if idade <= 17:
        print(f'Ainda irá se alistar, tem {falta} anos para realizar.')
    elif idade == 18 and 19:
        print('Hora de se alistar!')
    elif idade > 19:
        print(f'Já passou da hora de alistar, foram {passou}! Pague a multa.')
else:
    print('Você não tem obrigação de se alistar, siga seu caminho.')