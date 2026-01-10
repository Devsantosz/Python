notaA = float(input("Digite a nota do aluno: "))
notaB = float(input("Digite a nota do aluno: "))

#Calcular media
mediafinal = (notaA + notaB ) / 2

#Verificação
if mediafinal >= 7:
    print("A media %.1f - Aprovado"% mediafinal)
else:
    print("A media %.1f - Reprovado"% mediafinal)