prod = float(input('Qual o produto? '))

novo = prod - (prod * 5 / 100)

print('O produto que custava {:.2f}, na promocao vai custar R${:.2f}'.format(prod, novo))
