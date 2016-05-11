import sys
import os
import random

ref_arquivo = open("banco.txt","r")

for linha in ref_arquivo:
    coluna = linha.split()
    titulo=coluna[0]
    preco=coluna[1]
    loja=coluna[2]
    link=coluna[3]
    print(titulo, preco,link )

ref_arquivo.close()


