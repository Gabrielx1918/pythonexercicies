cont = t1 = n = 0
while True:
    n = int(input('DIGITE UM NUMERO [999 para parar]: '))
    if n == 999:
        break
    t1 += n
    cont += 1
print(f'Você digitou {cont} numeros, e a soma deles é {t1}')