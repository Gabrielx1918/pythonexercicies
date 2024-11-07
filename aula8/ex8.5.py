from random import choice, shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolha = choice(lista)
emba = shuffle(lista)
print(f'O aluno escolhido foi {escolha}\ne a lista fica na ordem {lista}')