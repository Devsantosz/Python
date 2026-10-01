peso = float(input("Qual o seu peso? (KG)"))
altura = float(input("Qual a sua altura? (m)"))

imc = peso / (altura ** 2) #potenciacao de altura elevada por 2 ou altura x altura

if imc < 18.5:
    print("Abaixo do peso.")
elif imc >= 18.5 and imc <= 25:
    print("Peso ideal.")
elif imc >= 25 and imc <= 30:
    print("Sobrepeso!")
elif imc >= 30 and imc <= 35:
    print("Obesidade grau I")
elif imc <= 40:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")
print(f"O seu IMC foi de {imc:.1f}")