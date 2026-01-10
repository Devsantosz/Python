# São imutaveis

# tupla = (2,4,6,7,9)
# tupla[1] = 5
# print(tupla)

halogenios = ('f', 'cl', 'Br','I', 'At')
gases_nobres = ('He','Ne','Ar','Xe','Kr','Rn')
elementos = halogenios + gases_nobres
t1 = (5,2,6,8,4,5,6,4,4,0,12,22,3,4,5)
print(sum(t1))

#Operações não disponiveis em tuplas:
#.sort()
#.append()
#.reverse()
#.pop()

# for elemento in elementos:
#     print(f'Elemento quimico: {elemento}')

# grupo17 = list(halogenios)
# grupo17[0] = 'H'
# print(grupo17)

grupo1 = ['li','Na','K','Rb','Cs','Fr']
alcalinos = tuple(grupo1)
print(alcalinos)

print(sorted(alcalinos))