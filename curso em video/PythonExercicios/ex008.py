medida = float(input('Uma distancia em metros: '))
dam = medida / 10
hm = medida / 100
km = medida / 1000

cm = medida * 100 #centrimentros
mm = medida * 1000 #milimitros
print('A medida {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
print('A medida {}m corresponde a {:.0f}dam, {:.0f}hm e {:.0f}km'.format(medida,dam, hm, km))
