print("{:=^40}".format("LOJA DO DEV"))

preco = float(input("Qual foi o valor das compras: R$"))

print(''''Formas de pagamento
[1] A vista dinheiro/cheque
[2] A vista no cartao
[3] 2x no cartao
[4] 3x ou mais no cartao
''')

opcao = int(input("Qual e a opcao?"))

if opcao == 1:
    desconto = preco - (preco * 10 / 100)
    print(f"A sua compra de R$ {preco:.2f}, ficou por R$ {desconto:.2f}, com 10% de desconto")
elif opcao == 2:
    desconto = preco - (preco * 5 / 100)
    print(f"A sua compra de R$ {preco:.2f}, ficou por R$ {desconto:.2f}, com 5% de desconto")
elif opcao == 3:
    parcela = preco / 2
    print(f"A sua compra de R$ {preco:.2f} parcelado em 2x, ficou R${parcela:.2f} cada parcela.")
elif opcao == 4:
    preco = preco + (preco * 20 / 100)
    parc = int(input("Quantas parcelas?"))
    parcelas = preco / parc
    print(f"A sua compra ficou R$ {preco:.2f} com juros de 20%, parcelado em {parc}x, ficou R${parcelas:.2f} cada parcela.")
else:
    print("Opcao invalida!")