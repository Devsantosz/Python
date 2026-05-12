n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print("O seu primeiro nome e {}. ".format(nome[0]))
print("O seu ultimo nome e {}. ".format(nome[-1]))