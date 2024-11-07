km = float(input('Quantos km terá a sua viagem? '))
preco = km*0.50
longa = km*0.45
if km <=200:
    print(f'Senhor sua viagem deu {preco}R$')
else:
    print(f'Senhor sua viagem deu {longa}R$ por passar de 200km então você recece desconto!')

