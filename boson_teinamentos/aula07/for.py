# lista = [2,6,9,5,0,12,3,7]
# palavra = 'python'
# for letra in palavra:
#     print(letra)

# for numero in range(1, 1001):
#     print(f'Y LOVE YOU {numero}!')

# nome = input('Digite seu nome: ')
# for x in range(10):
#     print(f'{x+1} {nome}')

# Range (início, fim, incremento)

# for x in range (2,20,2):
    # print(x)

pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Diamante', 'Safira','Turmalina')

for pedra in pedras:
    if pedra == 'Quartzo':
        continue
    print(pedra)