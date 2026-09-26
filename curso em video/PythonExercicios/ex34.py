salario = float(input("Qual e o seu salario? R$"))

#Regra de 3 representa em codigo(para descontos/promocao ou aumento em porcentagem)
#(salario * 10 / 100) = +15%
if salario <= 1250:
    n_salario = salario + (salario * 15 / 100)
else:
    n_salario = salario + (salario * 10 / 100)
print(f"O seu salario era R${salario} e agora esta R${n_salario}")                                                                      