import sys
import os
import random

le_entrada(): #Recebe o Título do jogo do arquivo do Vilaça e retorna uma 
    return x

def acha_menor(x):
ref_arquivo = open("banco.txt","r")
lista_de_linhas = ref_arquivo.readlines()
for linha in ref_arquivo:
    coluna = linha.split()
    titulo=coluna[0]
    preco=coluna[1]
    loja=coluna[2]
    link=coluna[3]
    i=0
    a="Não temos um valor atualizado"
    listaloja=[]
    listapreco=[]
    listatitulo=[]
    listalink=[]
    while i<=len(lista_de_linhas):
        if x==coluna[i]:
            listatitulo.append(titulo[i])
            listapreco.append(precos[i])
            listaloja.append(loja[i])
            listalink.append(link[i])
            return listatitulo,listapreco,listaloja,listalink
        i=i+1
    b=listaprecos.index(min(listaprecos))
    precominimo=listapreco[b]
    lojaminimo=listaloja[b]
    linkminimo=listalink[b]
    if b>=0:
        #return
        return (precominimo, lojaminimo,linkminimo)
    elif 
        return a

ref_arquivo.close()


