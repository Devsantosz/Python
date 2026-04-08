d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

km_value = 0.15
d_value = 60

orc = (d * d_value) + (km * km_value)

print('O total a pagar e R${:.2f}'.format(orc))