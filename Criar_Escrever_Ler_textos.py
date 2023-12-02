arquivo =  open('arquivo.txt', 'w')

arquivo.write('Curso de Python no Bradesco Learning\n')
arquivo.write('Hora da prática')
arquivo.close()

leitura = open('arquivo.txt', 'r')
print(leitura.read())
leitura.close()