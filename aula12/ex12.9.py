prod = str(input('Olá bom dia! Qual produto irá levar? '))
price = float(input('Me diga qual o preço dele:'))
forma = str(input('Qual será a forma de pagamento? ')).upper()
vista = price - price/100*10
cartao = price - price/100*5
parcela = price
parcela3 = price + price/100*20
if forma == 'A VISTA':
    print(f'Seu produto {prod} de {price}, com essa forma de pagamento fica por {vista}R$')
elif forma == 'CARTÃO':
    print(f'Seu produto {prod} de {price}, com essa forma de pagamento fica por {cartao}R$')
elif forma == 'DEBITO':
    print(f'Seu produto {prod} de {price}, com essa forma de pagamento fica por {parcela}R$')
elif forma == 'CREDITO PARCELADO':
    print(f'Seu produto {prod} de {price}, com essa forma de pagamento fica por {parcela3}R$')