import random 
from time import sleep #biblioteca de tempo

numero_aleatorio = random.randint(0,5)

num_select = int(input('Digite um numero de 0 a 5: '))
print("Processando resposta...")
sleep(2) # Faz o computador "dormir por () determinado."
if (num_select == numero_aleatorio):
    print('Voce ganho, parabens!')
else:
    print('Voce erro!')
    print(f'O numero era {numero_aleatorio}.')