#Sitema de cores em Python

#Style: 0,1,4,7
#Text: 30,31,32,33,34,35,36,37
#Back: 40,41,42,43,44,45,46,47

#Utilizando cores dentro do codigo
#print("\033[1;33;45m Ola, Mundo! \033[m")

#Usando .format para utilizar as cores
#print("{}Ola, Mundo!{}".format('\033[1;33;45m','\033[m'))

#Utilizando dicionario para criar cores 
cores = {
    'fim':'\033[m',
    'red':'\033[31m',
    'green':'\033[32m',
    'yellow':'\033[33m',
    'blue':'\033[34m',
    'purple':'\033[35m',
}

nome = str(input("\033[1;30;45m Qual e o seu nome? \033[m"))

print(f'Muito legal conhecer voce {cores['purple']}{nome}{cores['fim']}, Bora {cores['green']}Codar{cores['fim']}!')

