num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))

resultado = 0
selec = 0

while selec != 5:
    print("""Opcoes de operacoes matematicas:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa""")
    selec = int(input("Qual sua opcao? "))
    if selec == 1:
        resultado = num1 + num2
        print('Resultado da soma dos numeros: {}'.format(resultado))
    elif selec == 2:
        resultado = num1 * num2
        print('Resultado da multiplicar dos numeros: {}'.format(resultado))
    elif selec == 3:
        if num1 > num2:
            print("O maior numeror foi {}".format(num1))
        elif num1 == num2:
            print(f"Os numeros sao iguais!")
        else:
            print("O maior numeror foi {}".format(num2))
    elif selec == 4:
        num1 = int(input("Digite um numero inteiro: "))
        num2 = int(input("Digite outro numero inteiro: "))
    elif selec == 5:
        print("Saindo do programa")
    else:
        print("Opcao invalida. Tente novamente")
print("Programa finalizado com sucesso")