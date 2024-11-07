nome = str(input('Dois nomes: ')).lower().strip()
name = len(nome.strip()) - nome.count(' ')
a = nome.count('a')
ap = nome.find('a')+1
au = nome.rfind('a')
print(f'Os nomes: {nome}, contem {a} letras "a", e sua primeira a letra \n'
      f'esta na posição: {ap} \ne a ultima: {au}')
