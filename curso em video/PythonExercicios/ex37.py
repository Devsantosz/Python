num = int(input("Digite um numero inteiro: "))

print('''EScolha uma das bases para conversao

[ 1 ] converter para binario
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')

opcao = int(input("Qual a opcao desejada: "))

if opcao == 1:
    #Funcao de num binario
    print(f"{num} Convertido para binario e igual a {bin(num)[2:]}")
elif opcao == 2:
    # Funcao de num octal
    print(f"{num} Convertido para binario e igual a {oct(num)[2:]}")
elif opcao == 3:
    # Funcao de num hexadecimal
    print(f"{num} Convertido para binario e igual a {hex(num)[2:]}")
else:
    print("Opcao invalida, tente novamente")
