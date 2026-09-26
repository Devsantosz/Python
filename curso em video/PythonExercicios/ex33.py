a = int(input("Digite um valor:"))
b = int(input("Digite outro valor:"))
c = int(input("Mais um valor:"))
#Formata o a como menor valor e caso nao seja, sera atribuido outro valor a VAR menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Formata o a como maior valor e caso nao seja, sera atribuido outro valor a VAR menor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f"O menor valor foi {menor}")
print(f"O maior valor foi {maior}")

