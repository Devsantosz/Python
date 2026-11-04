resp = 'S'
media = quant = soma = maior = menor = 0

while resp in 'Ss':
    num = int(input("Digite um numero: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input("Quer continuar? [S/N] ")).upper().split()[0] #Deixar a str maiuscula e pega a primeira letra
media = soma / quant
print(f"Vc digitou {quant} numeros e a media foi {media}.")
print(f"O maior numero foi {maior} e o menor foi {menor}.")
print("Acabou!")
