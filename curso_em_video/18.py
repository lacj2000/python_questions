from math import sin, cos, radians

angulo = float(input('Digite o angulo: '))
radiano = radians(angulo)
seno = sin(radiano)
cosseno = cos(radiano)

print('seno: {}\nCosseno: {}'.format(seno, cosseno))
