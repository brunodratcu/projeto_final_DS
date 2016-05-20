ref_arquivo = open("b.txt","r")
lista_de_linhas = ref_arquivo.readlines()
valores=[]
indices=[]
i=0
while i<=len(lista_de_linhas):
    if lista_de_linhas[i].split(",")[0]=="GTA":
       valores.append(lista_de_linhas[i].split(",")[1])
       indices.append(i)
       return(valores,indices)
       i=i+1

a=valores.index(min(valores))
b=indices[a]
preco=lista_de_linhas[b].split(",")[1]
loja=lista_de_linhas[b].split(",")[2]
link=lista_de_linhas[b].split(",")[3]

ref_arquivo.close()
