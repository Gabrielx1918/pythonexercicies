import math
emp = str(input('Você deseja um empréstimo?')).strip().upper()
if emp == 'NÃO':
    print('OK, tenha um bom dia!')

else:
    print('OK, vamos prosseguir!')
    deq = str(input('Para o que seria esse empréstimo? '))
    casa = float(input(f'Qual o valor da {deq}?'))
    salario = float(input('Me diga o seu salário: '))
    parcelas = int(input('Em quantos anos deseja pagar? '))
    calculop = casa / (parcelas * 12)
    porc = salario / 100 * 30
    if porc > calculop:
        print(
            f'O seu empréstimo foi aprovado! as parcelas ficam no valor de {calculop: .2f} por mês durante {parcelas: .0f} anos')
    else:
        print('Seu empréstimo foi negado pois seu salário não pode pagar.')


