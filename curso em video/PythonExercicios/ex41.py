from datetime import date

nascimento = int(input("Qual a sua nascimento? "))

ano = date.today().year
idade = ano - nascimento

if idade <= 9:
    print(f"O atleta tem {idade} anos.")
    print(f"E ele e um atleta MIRIM.")
elif idade <= 14:
    print(f"O atleta tem {idade} anos.")
    print(f"E ele e um atleta INFATIL.")
elif idade <= 19:
    print(f"O atleta tem {idade} anos.")
    print(f"E ele e um atleta JUNIOR.")
elif idade <= 25:
    print(f"O atleta tem {idade} anos.")
    print(f"E ele e um atleta MASTER.")
else:
    print(f"O atleta tem {idade} anos.")
    print(f"E ele e um atleta MASTER.")
