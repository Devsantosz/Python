#Jogo de Pedra, Papel ou Tesoura

from random import randint #Aleatorio
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2) # de 0 ate o 2: 0,1,2
print('-=-'* 10)
print(''''Suas opcoes:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
jogador = int(input("Qual a sua jogada? "))
print('-=-'* 10)
sleep(1)
print("Jo")
sleep(1)
print("KEN")
sleep(1)
print("PO")


print('-=-'* 10)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=-'* 10)

if computador == 0: #pedra
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    else:
        print("COMPUTADOR VENCE")
elif computador == 1: #Papel
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    else:
        print("JOGADOR VENCE")
elif computador == 2: #Tesoura
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    else:
        print("EMPATE")
print('-=-'* 10)
