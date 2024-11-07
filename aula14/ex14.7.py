n = int(input('DIGITE UM NUMERO [999 para parar]: '))
t1 = 0
cont = 0
while n != 999:
    t1 += n
    n = int(input('DIGITE UM NUMERO [999 para parar]: '))
    cont += 1
print(f'Você digitou {cont} numeros, e a soma deles é {t1}')