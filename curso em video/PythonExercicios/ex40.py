nota1 = float(input("Qual a sua primeira nota: "))
nota2 = float(input("Qual a sua segunda nota: "))

media = (nota1 + nota2) / 2
print("-=-"*20)
#Se a nota for acima de 7
if media > 7:
    print("Aluno - aprovado!")
    print(f"Sua media foi {media} , Parabens!")
#Se a nota for acima de 5
elif media > 5:
    print("Aluno - recuperacao!")
    print(f"Sua media foi {media} , Vamos melhorar!")
#caso a nota for menor que 5
else:
    print("Aluno - reprovado!")
    print(f"Sua media foi {media} , Vamos melhorar, estude!")
print("-=-"*20)

