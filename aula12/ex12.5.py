n1 = float(input('Sua nota do primeiro bimestre: '))
n2 = float(input('Sua nota do segundo bimestre: '))
n3 = float(input('Sua nota do terceiro bimestre: '))
n4 = float(input('Sua nota do quarto bimestre: '))
m = (n1+n2+n3+n4)/4
if m >= 7.0:
    print(f'Sua nota final foi {m: .2f}, você passou de ano!')
elif 5.0 <= m <= 6.9:
    print(f'Sua nota final foi {m: .2f}, está de recuperação!')
else:
    print(f'Sua nota final foi {m: .2f}, você reprovou!')