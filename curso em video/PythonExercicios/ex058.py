from time import sleep
import random

tent = 0    #Contagem de tentativas
selec_num = 0   #Numero que o usuario ira digitar
num_sort = random.randint(1, 10)    #Numero que o computador vai receber

print('Vou pensar em um numero entre 1 e 10')
print("Pensando...")
sleep(2)
print("Tente advinhar!")

while selec_num != num_sort:        #Se o numero for diferente do que o cumputador pensou, executa.
    selec_num = int(input("Em que numero eu pensei? "))
    if selec_num == num_sort:  #Se o usuario acertar so vai rodar esse
        print("Voce acertou!")
    else:
        if selec_num < num_sort:  #Mostra ao usuario chances de estar proximo ao numero digitado
            print("Mais... Tente mais uma vez")
        else:
            print("Menos... Tente mais uma vez")
    tent = tent + 1  #Conta Quantas tentativas o usuario tentou
print('Voce pensei no numero {} e foram {} tentativas.'.format(num_sort, tent))
