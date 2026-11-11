num = soma = cont = 0   #Formatacao de variaveis, todas iram receber o mesmo valor

while True:             #Enquanto for vdd, exececuta.
    num = int(input("Digite um numero (999 para parar): "))
    if num == 999 :     #Caso o numero digitado seja 999, ele finaliza o while.
        break           #Finalizar Repeticao.
    soma += num         #Fazer a soma dos valores digitados.
    cont += 1           #Contador.

#F strings - Mostrar variaveis com a F-string.
print(f"A soma vale {soma} e foram {cont} digitados.")