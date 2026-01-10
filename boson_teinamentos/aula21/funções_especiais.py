#Funções lambda (funções anônimas)
#Sintaxe:
# lambda argumentos: expressão

#Raiz quadrada///
# quadrado = lambda x: x**2
# for i in range(1,11):
#     print(quadrado(i))

#Verificar se um número é par///
# par = lambda x: x %2 == 0
# print(par(8))

#Converter Fahrenheit para Celsius///
# f_c = lambda f: (f - 32) * 5/9
# print(f_c(32))

#Função map()
#Sintaxe:
# map(função, iterável)

# num = [1, 2, 3, 4, 5, 6, 7, 8]
# dobro = list(map(lambda x: x * 2, num))
# print(dobro)

# palavras = ['python', 'é', 'uma', 'linguagem', 'de', 'programação']
# maiusculas = list(map(str.upper, palavras))
# print(maiusculas)

#Função filter()
#Sintaxe:
# filter(função, sequência)

# def numeros_pares(n):
#     return n % 2 == 0

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13]

# num_pares = list(filter(numeros_pares,numeros))
# print(num_pares)

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13]
# num_impar = list(filter(lambda x: x % 2 != 0, numeros))
# print(num_impar)

#Função reduce()
#Sintaxe:
# reduce(função, sequência, valor_inicial)

from functools import reduce

# def multi(x,y):
#     return x * y

# numeros =[1, 2, 3, 4, 5, 6]

# total = reduce(multi,numeros)
# print(total) 

#Soma cumulativa dos quadrados de valores, usando a função lambda
numeros =[1, 2, 3, 4]
#((1² + 2²) + 3²) + 4² 
total = reduce(lambda x,y: x**2 + y**2, numeros)
print(total)