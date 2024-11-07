salario = float(input('Qual o seu salario? R$'))
if salario <=1250:
    pro = salario + salario/100*15
    print(f'O seu novo salário é de {pro: .2f}!')
else:
    pro = salario + salario/100*10
    print(f'Seu novo salário é de {pro: .2f}!')