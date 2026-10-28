sexo = str(input("Digite seu sexo: [M/F]")).strip().upper()[0] #Tirar espaco e deixar maiusculo, pegando a primeira letra
while sexo not in 'MF': #Se o seu sexo nn estiver em 'MF', continua executando
    sexo = str(input("Dados invalidos. Por favor,digite seu sexo: [M/F]")).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')


