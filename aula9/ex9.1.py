nome = str(input('Digite 2 nomes: ')).strip()
letras = len(nome) - nome.count(' ')
primeiro = nome.find(' ')
print(f'O nome {nome} tem suas seguintes variantes:\n Maiuscula: {nome.upper()}\n Minuscula:'
      f' {nome.lower()}\n Letras: {letras}\n Letras do primeiro nome: {primeiro}')



