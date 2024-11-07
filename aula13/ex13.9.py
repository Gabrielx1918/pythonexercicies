from datetime import date
atual = date.today().year
cont = 0
cont2 = 0
for c in range(1,10+1):
    nasc = int(input('Em que ano vós nasceu: '))
    calc = atual - nasc
    if calc >= 18:
        cont += 1
    else:
        cont2 += 1
print(f'{cont} pessoas são maiores, já {cont2} são menores')