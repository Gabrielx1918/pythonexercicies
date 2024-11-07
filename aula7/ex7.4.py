me = float(input('Quantos metros de barbante você quer? '))
cen = me*100
mm = me*1000
print(f'Então quer exatamente {cen: .2f} centimetros e {mm: .2f} milimetros de barbante?')
r = input('Sim ou não?')
print(r,'? Obrigado pela preferência!')