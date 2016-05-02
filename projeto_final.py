# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:34:01 2016

@author: Bruno Dratcu
"""

import webbrowser


class Pagina:
    """Classe que irá abrir uma pagina para mostrar dados de jogos"""   
    
    def __init__(self, busca, titulo, descricao):
        self.busca = busca
        self.titulo = titulo
        self.descricao = descricao

    def buscar(self):
        self.busca = True
        
    def titulo(self):
        if self.busca:
            print(self.titulo)
        
    def descricao(self):
        if self.titulo:
            print(self.descricao)
        

gta = Pagina(True, "GTA", "blablabla")
print(gta.titulo)
print(gta.descricao)
    
#    def ___init__(self, busca, titulo, descricao, poster, preco, trailer):
#        self.busca = busca
#        self.titulo = titulo
#        self.descricao = descricao
#        self.poster_url = poster
#        self.preco = preco
#        self.trailer_url = trailer
#        
#    def buscar(self):
#        self.busca = True
#        
#    def show_titulo(self):
#        if self.busca:
#            print(self.titulo)
#            
#    def show_poster(self):
#        if self.titulo:
#            print(self.poster_url)
#            
#    def show_descricao(self):
#        if self.poster_url:
#            print(self.descricao)
#            print(self.preco)
#            print(webbrowser.open("self.trailer_url"))
#        
#        
##gta_poster = webbrowser.open("http://cdn.atl.clicrbs.com.br/wp-content/uploads/sites/27/2015/04/actual_1410520494.jpg")
##gta_trailer = webbrowser.open("https://www.youtube.com/watch?v=VjZ5tgjPVfU")
##
##mario_poster = webbrowser.open("https://i.ytimg.com/vi/1dhrHlol3SM/maxresdefault.jpg")
##mario_trailer = webbrowser.open("https://www.youtube.com/watch?v=eO8xe2AUY4c")
#
#
##gta = Pagina(True, 
##             "GTA", 
##             "Jogo que mata pessoas",
##             "http://cdn.atl.clicrbs.com.br/wp-content/uploads/sites/27/2015/04/actual_1410520494.jpg"
##             "R$200,00", 
##             "https://www.youtube.com/watch?v=VjZ5tgjPVfU")
#gta = Pagina(True, "GTA", "Jogo que mata pessoas", "", "R$200,00", "")
#
#                           
#print(gta.titulo)
#print(gta.descricao)
##print(gta.poster_url)
#print(gta.preco)
##print(gta.trailer_url)
#
##mario_bros = Pagina("Super Mario Bros", 
##                    "Jogo de um encanador psicodelico", 
###                    "mario_poster", 
##                    "https://i.ytimg.com/vi/1dhrHlol3SM/maxresdefault.jpg"
##                    "R$150,00", 
###                    "mario_trailer")
##                    "https://www.youtube.com/watch?v=eO8xe2AUY4c")
##                    
##                    
##print(mario_bros)