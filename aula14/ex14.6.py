print('-'*30)
print('   SEQUENCIA DE FIBONACCI')
print('-'*30)
n = int(input('Quantos termos você quer? '))
t1 = 0
t2 = 1
cont = 3
if n == 0:
    print('OK')
else:
    print(f'{t1} - {t2} ', end='')
    while cont <= n:
        t3 = t1 + t2
        print(f'- {t3} ', end='')
        cont += 1
        t1 = t2
        t2 = t3
    print('- FIM', end='')