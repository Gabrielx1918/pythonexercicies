pri = int(input('Me de o primeiro termo: '))
raz = int(input('Me sua razao: '))
enes = pri+(10-1)*raz
print('A PA é: ')
for c in range(pri, enes+raz, raz):
    print(c, end=' ')
