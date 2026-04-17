import math

ang = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(ang))
print('O angulo de {} tem o seno de {}'.format(ang, seno))
co = math.cos(math.radians(ang))
print('O angulo de {} tem o co {}'.format(ang, co))
tan = math.tan(math.radians(ang))
print('O angulo de {} tem o tan {}'.format(ang, tan))