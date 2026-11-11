from random import randint

print("-=-"*10)
print("Par ou impar")
print("-=-"*10)

vit = 0
while True:
    jogador = int(input("Diga um valor: "))
    cpu = randint(0, 10)
    total = jogador + cpu
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input("Par ou impar? [P/I] ")).strip().upper()[0]
    print(f"Voce jogou {jogador} e o computador jogou {cpu} ", end = "")
    print(f"Deu par!"if total % 2 == 0 else "Deu impar!")
    if tipo == 'P':
        if total % 2 == 0:
            print("Voce ganhou!")
            vit += 1
        else:
            print("Voce perdeu!")
            print("-=-" * 10)
            break
    if tipo == 'I':
        if total % 2 == 1:
            print("Voce ganhou!")
            vit += 1
        else:
            print("Voce perdeu!")
            print("-=-" * 10)
            break

    print("Vamos jogar novamente...")
    print("-=-"*10)
print(f"Voce venceu {vit} vezes!")
print("-=-" * 10)
