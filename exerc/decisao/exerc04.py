letra = str(input("Digite uma letra: ")).lower()
#Formatar str para minuscula .lower()

if letra in "aeiou":
    print(f"A letra {letra} é uma vogal.")
else:
    print(f"A letra {letra} é uma consoante.")

