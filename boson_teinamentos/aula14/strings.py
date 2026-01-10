frase = 'Vamos aprender python hoje.'
# palavras = frase.split()
# print(palavras[1])
# for letra in frase:
#     print(letra)


# email = input('Digite seu email:')
# arroba = email.find('@')
# print(arroba)
# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(usuario)
# print(dominio)

# produtos = 'carbonato de sodio e óxido de zinco'
# print('sodio' in produtos)
# print('magnesio' not in produtos)

# item = 'hipoclorito'
# pos = item.find('clor')
# print(pos)
# pos = item.find('flu')
# print(pos)

# objeto_celeste = 'galaxia esPiral M31'
# print(objeto_celeste.title())

# suplemento = 'cloreto de magnesio'
# n_suplemento = suplemento.replace('magnesio', 'zinco')
# print(suplemento)
# print(n_suplemento)

# frase = '   Õmega 3 é bom para saude!     '
# print(frase)
# print(frase.lstrip())
# print(frase.rstrip())
# print(frase.strip())

# fruta = 'Abacate'
# print(fruta)
# print(fruta.rjust(20))
# print(fruta.center(20))
# print(fruta.ljust(20,"-"))

# p = 'Bóson Treinamentos'
# print(p.startswith('B'))
# print(p.endswith('s'))

#Docstrings

texto = """"
Docstring é uma especie de documentação
que podemos inserir dentro de um modulo, função
ou classe no Pyhon, entre outros locais 
    Respeita deslocamento do texto e é multilinhas
"""

print(texto)