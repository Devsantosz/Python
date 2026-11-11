num = 0
print("-=-"*10)
print('PROGRAMA DE TABUADA')
while True:
    num = int(input('Quer ver a tabuada de qual numero? '))
    if num < 0:     #Se o numero for menor q 0/ser negativo
        print('NUMERO NEGATIVO ENVIADO!')
        break       #Para o loop
    for c in range(1, 11):      #Faça de 1 ate "10"
        print(f"{num} x {c} = {num * c}")   #Mostrar o valor digitado, a contagem e o resultado
    print("-=-"*10)
print('PROGRAMA DE TABUADA FINALIZADO!')