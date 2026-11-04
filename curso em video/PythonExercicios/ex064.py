num = soma = cont = 0
num = int(input("Digite um numero [999 para parar]: "))
while num != 999:
    if num == 999:
        break
    else:
        soma += num
    cont += 1
    num = int(input("Digite um numero [999 para parar]: "))
print(f"Foram digitados {cont} e a soma deles foram {soma}")
print("Acabou!")
