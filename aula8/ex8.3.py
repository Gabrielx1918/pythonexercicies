from math import hypot
co = float(input('Qual a medida do cateto oposto: '))
ca = float(input('Qual a medida do cateto adjascente: '))
hi = hypot(co, ca)
print(f'O cateto oposto tem {co} unidades e o adjescente {ca}, sua hipotenusa equivale a {hi: .2f}')
