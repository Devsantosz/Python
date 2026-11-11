from random import randint
#biblioteca importada e a funcao que sera usada para escolher

print("-=-"*10)
print("Par ou impar")
print("-=-"*10)

vit = 0
while True:
    jogador = int(input("Diga um valor: "))         #Pedir ao usuario um valor
    cpu = randint(0, 10)        #Faz o cpu "escolher" um numero
    total = jogador + cpu       #Soma dos num, para a selecao de impar ou par
    tipo = ' '
    while tipo not in 'PI':     #Enquanto o tipo nao for selecionado entre P ou I
        tipo = str(input("Par ou impar? [P/I] ")).strip().upper()[0] #Formatar tipo, tirando espacos e deixando em maisculo
    print(f"Voce jogou {jogador} e o computador jogou {cpu} ", end = "")
    print(f"Deu par!"if total % 2 == 0 else "Deu impar!")       #Condicoes para mostrar se deu impar ou par
    if tipo == 'P':     #Se for escolhido P
        if total % 2 == 0:  #Se o resto de divisao entre os numero for de 0
            print("Voce ganhou!")
            vit += 1        #Conta 1+ para a vitoria
        else:
            print("Voce perdeu!")
            print("-=-" * 10)
            break           #Parar a repeticao
    if tipo == 'I':     #Se for escolhido I
        if total % 2 == 1:  #Se o resto de divisao entre os numero for de 1
            print("Voce ganhou!")
            vit += 1
        else:
            print("Voce perdeu!")
            print("-=-" * 10)
            break           #Parar a repeticao

    print("Vamos jogar novamente...")
    print("-=-"*10)
print(f"Voce venceu {vit} vezes!")
print("-=-" * 10)
