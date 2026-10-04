from datetime import date
atual = date.today().year
maior_d = 0
menor_d = 0

for c in range(1, 8):
    ano = int(input(f"Qual o ano de nascimento da {c} pessoa?"))
    idade = atual - ano
    if idade >= 21:
        maior_d += 1
    else:
        menor_d += 1

print(f"{maior_d} atingiram a maior idade.")
print(f"{menor_d} nao atingiram a maior idade.")