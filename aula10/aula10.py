n1 = float(input('Sua nota do primeiro bimestre: '))
n2 = float(input('Sua nota do segundo bimestre: '))
n3 = float(input('Sua nota do terceiro bimestre: '))
n4 = float(input('Sua nota do quarto bimestre: '))
m = (n1+n2+n3+n4)/4
if m >= 7.0:
    print(f'Sua nota final foi {m}, você passou de ano!')
else:
    print(f'Sua nota final foi {m}, você reprovou!')