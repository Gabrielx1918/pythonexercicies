ano = int(input('Que ano quer analisar? '))
if ano % 400//100 == 0:
    print(f'seu ano {ano} é bissexto')
else:
    print(f'seu ano {ano} não é bissexto')