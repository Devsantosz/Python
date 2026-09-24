sexo = str(input("Digite seu sexo (M/F): ")).upper()

#Formatar uma string para maiuscula .upper()

if sexo == "M":
    print("Você é do sexo masculino.")
elif sexo == "F":
    print("Você é do sexo feminino.")
else:
    print("Sexo inválido.")