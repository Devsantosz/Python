import random

# valor = random.randint(1,20)
# print(valor)

# print('Gerar cinco numeros aleatorios entre 1 e 50: \n')
# for i in range(5):
#     n = random.randint(1,50)
#     print(f'Números gerado: {n}')

# valor = random.random()
# print(f'Numeros gerado: {round(valor * 10, 2)}')

# valor = random.uniform(1,100)
# print(f'Número: {round(valor, 2)}')

L = [2,4,6,9,10,13,14,16,18,20,21,27,33]
# n = random.choice(L)
# print(f'Número escolhido: {n}')

# n = random.sample(L,3)
# print(f'Números escolhidos: {n}')

#Embaralha
print(f'Exibir a lista original: {L}')
print(f'Embaralhar a lista e exibi-la:')
n = random.shuffle(L)
print(L)