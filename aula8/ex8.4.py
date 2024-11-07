from math import sin, cos, tan, radians
ang = float(input('Me dê um angulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(f'O angulo de {ang} tem:\nseu seno de {sen: .2f}\nseu cosseno de {cos: .2f}\nseu tangente de {tan: .2f}')