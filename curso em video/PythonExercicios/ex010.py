real = float(input('Quanto de dinheiro vc tem? '))
dolar = 3.27

saldo = real / dolar

print('Com R${:.0f} voce pode comprar US${:.0f}'.format(real,saldo))
