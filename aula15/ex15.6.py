print('-'*25)
print('BANCO DO GAYBRIEL'.center(25))
print('-'*25)
valor = int(input('Quanto deseja sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        print(f'Total de {totced} cedulas de {ced}R$')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-'*25)
print('VOLTE SEMPRE'.center(25))
print('-'*25)