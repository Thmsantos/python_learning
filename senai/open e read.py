#função open e read
#primeiro (nome do arquivo)
#segundo (o que fazer com o arquivo (r - read)

arquivo = open ('open.txt' , 'r')
conteudo = arquivo.read()
print (conteudo)

#arquivo com muitas linhas

arquivo = open ('open.txt' , 'r')
for linha in arquivo.readlines():
    print (linha)
