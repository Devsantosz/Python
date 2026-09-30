nome = str(input("Qual o seu nome? "))

if nome == "Guilherme":
    print("Que nome Bonito!")
elif nome == "Yasmin" or nome == "Yara" or nome == "Yago":
    print("Seu nome tem Y, que legal!")
else:
    print("Seu nome e bem normal.")
print(f"Tenha um bom dia {nome}!")