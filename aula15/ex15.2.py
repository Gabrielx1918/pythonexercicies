while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if tab <= 0:
        print('FINISH HIM')
        break
    for c in range(1,11):
        resul = tab * c
        print(f'{tab} x {c} = {resul}')
