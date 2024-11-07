num = int(input('Escolha um numero para saber suas casas: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print(f'O numero: {num} tem: \n UNIDADE: {uni} \n'
      f' DEZENA: {dez}\n CENTENA: {cen}\n MILHAR: {mil}')