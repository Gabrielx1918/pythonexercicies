altura = float(input('Me diga sua altura: '))
peso = float(input('Me diga seu peso: '))
imc = peso/(altura**2)
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.6 <= imc <= 25:
    print('Você está com o peso ideal!')
elif 25.1 <= imc <= 30:
    print('Você está com Sobrepeso!')
elif 30.1 <= imc <= 40:
    print('Você está obeso!')
elif imc > 40:
    print('Você está com obesidade mórbida!')