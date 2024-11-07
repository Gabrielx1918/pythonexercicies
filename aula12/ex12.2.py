num  = int(input('Olá cara usuário, digite um numero: '))
escolha = int(input('Ok, agora digite 1 para conversão em binário, 2 para octal e 3 para hexagonal: '))
bina = bin(num)
oct = oct(num)
hex = hex(num)
if escolha == 1:
    print(f'Sua conversão para binário do numero {num}, resultou em: {bina [2:]}')
elif escolha == 2:
    print(f'Sua conversão para octal do numero {num}, resultou em: {oct [2:]}')
else:
    print(f'Sua conversão para hexagonal do numero {num}, resultou em: {hex [2:]}')