arquivo = open('arqtext.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula Pratica')
arquivo.close()

#Leitura do arquivo texto
arquivo = open('arqtext.txt', 'r')
print((arquivo.read()))
arquivo.close()