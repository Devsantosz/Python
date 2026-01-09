#Manipulação de arquivos de texto

import os


base_dir = os.path.dirname(__file__)
caminho = os.path.join(base_dir, 'dados', 'arquivo.txt')

# with open(caminho, 'r', encoding='UTF-8') as manipulador:
#     print('Metodo read():\n')
#     print(manipulador.read())

# with open(caminho, 'r', encoding='UTF-8') as manipulador:
#     print('Metodo read():\n')
#     print(manipulador.readline())
#     print(manipulador.readline())

# with open(caminho, 'r', encoding='UTF-8') as manipulador:
#     print('Metodo read():\n')
#     print(manipulador.readlines())

# base_dir = os.path.dirname(__file__)
# caminho = os.path.join(base_dir, 'dados', 'arquivo.txt')

# texto = input('Qual termo deseja procurar no arquivo?')
# try:
#     manipulador = open(caminho, 'r', encoding='utf-8')
#     for linha in manipulador:
#         linha = linha.rstrip()
#         if texto in linha:
#             print(f'A String foi encontrada!')
#             print(linha)
#         else:
#             print(f'String não encontrada!')
# except IOError:
#     print(f'Não foi possivel abrir o arquivo')
# else:
#     manipulador.close()

#  base_dir = os.path.dirname(__file__)
#  caminho = os.path.join(base_dir, 'dados', 'arquivo.txt')
# texto = 'Python é usado em ciencia de dados extensivamente'

frutas = ['Morango\n','Uva\n','Caju\n','Amora\n','Framboesa\n','Graviola']

#Criar e gravar arquivos
try:
     manipulador = open('frutas.dat', 'a', encoding='utf-8')
     manipulador.writelines(frutas)
except IOError:
     print(f'Não foi possivel abrir o arquivo')
else:
    manipulador.close()

#Ler o arquiuvo criado
try:
     manipulador = open('frutas.dat', 'r', encoding='UTF-8')
     print(manipulador.read())
except IOError:
     print(f'Não foi possivel abrir o arquivo')
else:
     manipulador.close()