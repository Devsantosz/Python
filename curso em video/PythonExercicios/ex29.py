import math

Km_car = float(input("Qual e a velocidade do carro km/h: "))

if(Km_car > 80):
    multa = (Km_car - 80) * 7
    print(f"Voce foi multado, no valor de R${multa}. po excesso de velocidade")
else:
    print("Velocidade segura, continue com cuidado!")