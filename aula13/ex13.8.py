nome = input('Me de uma frase: ').strip().upper()
separar = nome.split()
junta = ''.join(separar)
inverso = ''
for letras in range(len(junta)-1, -1, -1):
    inverso += junta[letras]
print(junta, inverso)
if junta == inverso:
    print('TEMOS UM PALINDROMO')
else:
    print('NÃO TEMOS UM PALINDROMO')
