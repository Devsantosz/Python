import math

area = float(input("Digite o tamanho da área a ser pintada em m²: "))

#Divide a area por 3
litros = area / 3
#Arrendonda o valor para cima, divide a quantiodade de litros
latas = math.ceil(litros / 18)
#Calcula o preco total, pelo valor de cada lata
preco_total = latas * 80

print(f"\nQuantidade de latas: {latas}")
print(f"Preço total: R$ {preco_total:.2f}")