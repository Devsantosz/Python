cont = 0
soma = 0

for i in range(1, 7):
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        soma = soma + numero
        cont = cont + 1
print(f"Voce informou {cont} numeros pares e a soma de {soma}.")
