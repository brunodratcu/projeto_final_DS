# -*- coding: utf-8 -*-
"""
Created on Fri May 20 14:39:22 2016

@author: Gabriel
"""

class data:
    
    def __init__(self):

        self.ref_arquivo = open("banco.txt","r")
        self.lista_de_linhas = self.ref_arquivo.readlines()
        self.ref_arquivo.close()
    
    def read_games(self, nome):
        
        self.valores=[]
        self.indices=[]
        for self.i in range(len(self.lista_de_linhas)):
            if self.lista_de_linhas[self.i].split(",")[0]== nome:
                self.preco=float(self.lista_de_linhas[self.i].split(",")[1]) 
                self.valores.append(self.preco)
                self.indices.append(self.i)        
        self.a=self.valores.index(min(self.valores))
        self.b=self.indices[self.a]
        self.info = self.lista_de_linhas[self.b].split(",")
        self.info.pop(0)  
        return self.info
    
    def list_games(self):
       
        self.lista_games=[]
        self.lista_plataformas=[]
        self.lista_games_id = []
        
        for self.i in range(len(self.lista_de_linhas)):
            self.lista_info = self.lista_de_linhas[self.i].split(",")
            self.game_space = self.lista_info[5].split("_")
            self.lista_games.append(self.game_space)
            self.lista_plataformas.append(self.lista_info[3])
            self.lista_games_id.append(self.lista_info[6])

        return [self.lista_games,self.lista_plataformas,self.lista_games_id]    