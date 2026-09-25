nota1 = float(input('Primeira nota: '))

nota2 = int(input('Segunda nota: '))

media = (nota1 +nota2)/2

if media >= 7:
    print('Aprovado')
elif media >= 5:
    print('recuperacao')
else:
    print('Reprovado')

