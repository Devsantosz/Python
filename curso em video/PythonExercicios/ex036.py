casa = float(input("Qual o valor da casa: "))
salario = float(input("Qual o seu salario: "))
anos = int(input("Quantos anos de financiamento: "))

prestacao = casa / (anos * 12)
#Verifica se a prestacao dele e menor que o salario
min = salario * 30 / 100


print(f"Para pagar uma casa de R$ {casa:.2f} em {anos} anos", end='')
print(f" a prestacao sera de R$ {prestacao:.2f}")

#Verifica se a prestacao dele e menor que o salario
if prestacao <= min:
    print("Emprestimo Concedido!")
else:
    print("Emprestimo NEGADO!")
