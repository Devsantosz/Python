#Recursividade em Python

#Formula geral para o fatorial
#Fatorial(num) = 1, se num = 0 ou se num = 1 'Caso-Base'
#Fatorial(num) = num * Fatorial(num - 1), para num > 1 'caso Recursivo'
# 4! = 4 * fatorial(3) = 4 * 3 * fatorial(2) = 4 * 3 * 2 * fatorial(1) 
# 4 * 3 * 2 * 1 = 24

def fatorial(numero):
    if numero == 0 or numero == 1: #caso-base
        return 1
    else: #caso-recursivo
        return numero * fatorial(numero - 1)

if __name__ == '__main__':
    x = int(input('Digite um numero inteiro para calcular seu fatorial: '))
    try:
        res = fatorial(x)
    except RecursionError:
        print('Numero muito grande para calcular o fatorial ou numero negativo!')
    else:
        print(f'O fatorial de {x} é igual a {res}')