r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima, PODEM FORMAR UM TRIANGULO: ", end='')
    if r1 == r2 == r3: #Verifica se todos os lados sao iguais
        print("Equilatero")
    elif r1 != r2 != r3 != r1:  #verifica se sao diferentes
        print("Escaleno")
    else:
        print("Isoceles")
else:
    print("Os segmentos acima, NAO PODEM FORMAR UM TRIANGULO!")