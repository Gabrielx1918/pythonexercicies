print('-'*30)
print('LOJA SUPER BARATÃO'.center(30))
print('-'*30)
soma = cont = contm = menor = 0
nomem = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    quer = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += preco
    contm += 1
    if preco >= 1000:
        cont += 1
    if contm == 1 or preco < menor:
        menor = preco
        nomem = produto
    if quer == 'N':
        break
print(f'O valor da sua compra deu {soma}R$')
print(f'{cont} produtos foram mais de R$1000')
print(f'O produto mais barato foi {nomem} custando R${menor}')
