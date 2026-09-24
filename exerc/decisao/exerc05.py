nota01 = float(input("Qual a 1 nota do aluno? "))
nota02 = float(input("Qual a 2 nota do aluno? "))

#Faz a soma das duas notas e divide
media = (nota01 + nota02) / 2

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")