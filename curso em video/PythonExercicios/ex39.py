from datetime import date
#Biblioteca de data
idade = int(input("Qual a sua idade? "))

#importa a data atual do computador e utiliza
#date=funcao .today=hoje .year=formatacao de ano
ano = date.today().year

print(f'Quem nasceu em {(ano - idade )} tem {idade} e nasceu em {ano}.')

if idade < 18:
    print(f"Voce tem {idade} anos e falta {18 - idade } ano para voce poder se alistar.")
elif idade == 18:
    print(f"Voce tem {idade} e esta na hora de se alistar!")
    print(f"Seu ano de alistamento e em {ano - (idade - 18 )}.")
else:
    print(f"Voce Ja devia ter se alistado!")
    print(f"O ano de alistamento foi em {ano - (idade - 18 )} ano.")
