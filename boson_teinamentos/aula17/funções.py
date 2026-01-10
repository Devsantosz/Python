#Funções
#Modularização, Reúso de codigo, Legibilidade

# def <nome_função> ([argumento]):
#     <Instruções>

# def mensagem():
#     print('Bóson Treinamentos em tecnolgia')
#     print('Curso completo de Python')

# mensagem()

#função com argumentos
# def soma(a, b):
#     print(a+b)

# soma(12,7)

# def multi(x, y):
#     return x * y

# a = 5
# b = 8
# c = multi(a, b)

# print(f'o produto de {a} e {b} é {c}')

# def div(k, j):
#     if j != 0:
#         return k / j
#     else:
#         return 'Impossivel dividir por zero!'

# if __name__ == '__main__':
#     a = int(input('Digite um numero:'))
#     b = int(input('Digite outro numero:'))

#     r = div(a, b)
#     print(f'{a} dividido por {b} é igual a {r}')

def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados

if __name__ == '__main__':
    valores = [2,5,7,9,12]
    resultados = quadrado(valores)
    for g in resultados:
        print(g)