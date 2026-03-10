cont = 1
s = 0
n = 0
resp = "S"


while(resp == "S" or "s"):
    n = int(input("Digite o valor: "))

    s = s + n
    resp = str(input("Voce quer continuar? [S/N]"))
print(s)
    

