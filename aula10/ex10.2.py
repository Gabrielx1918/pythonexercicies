fotosensor = float((input('Qual foi sua velocidade naquela via?')))
if fotosensor >=81:
    multa = fotosensor-80
    igual = multa*7
    print(f'Lhe informo que o Senhor foi multado! sua multa será no valor de {igual}R$')
else:
    print('Sem problemas, tudo certo por aqui!')

