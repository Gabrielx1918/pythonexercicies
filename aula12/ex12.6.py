print('\033[7:34:41m CONFEDERAÇÃO NACIONAL DE NATAÇÃO \033[m')
idade = int(input('Me diga sua idade para saber sua categoria: '))
if idade < 10:
    print(f'Por ter {idade} anos, você é da categoria MIRIM!')
elif 10 <= idade <= 14:
    print(f'Por ter {idade} anos, você é da categoria INFANTIL!')
elif 15 <= idade <= 19:
    print(f'Por ter {idade} anos, você é da categoria JUNIOR!')
elif idade == 20:
    print(f'Por ter {idade} anos, você é da categoria SENIOR!')
elif idade > 20:
    print(f'Por ter {idade} anos, você é da categoria MASTER!')