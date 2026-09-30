num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))

#Operador logico de comparacao, verifica se num1 e maior que num2.
if num1 > num2:
    print(f"O numero {num1} e maior que o numero {num2}")
elif num1 < num2:
    print(f"O numero {num2} e maior que o numero {num1}")
#Operador logico de comparacao, verifica se ambos os numeros sao igual.
#elif num1 == num2:
else:
    print(f"O numero {num1} e igual a {num2}")
