soma_idades = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ""
mulheres_menores_20 = 0

for pessoa in range(1, 5):
    print(f"----- {pessoa}ª pessoa -----")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    soma_idades += idade

    if pessoa == 1 and sexo == "M":
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    if sexo == "M" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    if sexo == "F" and idade < 20:
        mulheres_menores_20 += 1

media_idade = soma_idades / 4

print("\n----- RESULTADO -----")
print(f"A média de idade do grupo é {media_idade:.1f} anos.")

if nome_homem_mais_velho:
    print(f"O homem mais velho é {nome_homem_mais_velho}")
    print(f"com {idade_homem_mais_velho} anos.")
else:
    print("Não foi informado nenhum homem.")

print(f"Há {mulheres_menores_20} mulher(es) com menos de 20 anos.")