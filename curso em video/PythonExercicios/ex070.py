total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input("Digite o nome do produto: "))
    preco = float(input("Preco: R$"))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print("{:-^40}". format(" Fim do programa "))
print(f"O total da compra foi de R${total:.2f}")
print(f"Temos {totmil} que custao R$1.000,00")
print(f"O produto mais barato foi {barato}e custa R${menor:.2f}")