ref_arquivo = open("a.txt","r")
lista_de_linhas = ref_arquivo.readlines()
valores=[]
indices=[]
i=0
while i<len(lista_de_linhas):
    if lista_de_linhas[i].split(",")[0]=="PACMAN":
       n=float(lista_de_linhas[i].split(",")[1]) 
       valores.append(n)
       indices.append(i)
    i=i+1

a=valores.index(min(valores))
b=indices[a]
preco=lista_de_linhas[b].split(",")[1]
loja=lista_de_linhas[b].split(",")[2]
link=lista_de_linhas[b].split(",")[3]
print(preco)

ref_arquivo.close()
