reta1 = float(input('Me diga cm de uma reta: '))
reta2 = float(input('Me diga cm de uma reta p2: '))
reta3 = float(input('Me diga cm de uma reta p3: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Suas retas formam sim um triangulo!')
else:
    print('Suas retas não formam um triangulo!')

