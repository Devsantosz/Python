print("-=-"*10)
print("CADASTRE UMA PESSOA")
print("-=-"*10)

tot18 = totH = totM20 = idade = 0

while True:
    idade = int(input("Qual a sua idade? "))
    sexo = ' '

    #Caso nao seja enviado M ou F
    while sexo not in "MF":
        sexo = str(input("Qual o seu sexo? [M/F] ")).strip().upper()[0]
    #Condicao de ver quants usuarios sao maiores de 18 anos
    if idade > 18:
        tot18 += 1
    #Condicao para verificar quantos usuarios sao H
    if sexo == "M":
        totH += 1
    #Condicao para verificar quantas M sao menores de 20 anos
    if sexo == "F" and idade < 20:
        totM20 += 1
    resp = ' '
    #Verificar com o usuario quer continuar
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    #Condicao de parada
    if resp == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {tot18} pessoas.")
print(f"AO todo temos {totH} homens cadastrados.")
print(f"E temos o total de {totM20} mulheres com menos de 20 anos.")
print("FIM DO PROGRAMA")
