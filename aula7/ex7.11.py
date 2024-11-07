km = float(input('Olá, quantos quilometros você percorreu com o carro alugado? '))
day = int(input('E por quantos dias ele foi alugado? '))
apa = (km * 0.15) + (day * 60)
print(f'O senhor(ar) deve {apa:.2f}R$ pelo carro alugado, de acordo com os {km}km rodados durante {day} dias!')
