# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:34:01 2016

@author: Bruno Dratcu
"""

import webbrowser

class Pagina():
    """Classe que irá abrir uma pagina para mostrar dados de jogos"""
    
    def ___init__(self, title, descricao, poster, preco, trailer):
        self.title = title
        self.descricao = descricao
        self.poster_url = poster
        self.preco = preco
        self.trailer_url = trailer
        
    def show_title(self):
        if self.title:
            print(self.poster_url)
            
    def show_descricao(self):
        if self.poster_url:
            def abre_pagina():
                print(self.descricao)
                print(self.preco)

        
    def show_trailer(self):
        if self.trailer_url:
            print(webbrowser.open("self.trailer_url"))
        
        
        
#gta_poster = webbrowser.open("http://cdn.atl.clicrbs.com.br/wp-content/uploads/sites/27/2015/04/actual_1410520494.jpg")
#gta_trailer = webbrowser.open("https://www.youtube.com/watch?v=VjZ5tgjPVfU")
#
#mario_poster = webbrowser.open("https://i.ytimg.com/vi/1dhrHlol3SM/maxresdefault.jpg")
#mario_trailer = webbrowser.open("https://www.youtube.com/watch?v=eO8xe2AUY4c")


GTA = Pagina("GTA", 
             "Jogo que mata pessoas", 
#             "gta_poster", 
             webbrowser.open("http://cdn.atl.clicrbs.com.br/wp-content/uploads/sites/27/2015/04/actual_1410520494.jpg"),
             "R$200,00", 
#             "gta_trailer")
             webbrowser.open("https://www.youtube.com/watch?v=VjZ5tgjPVfU"))
                           
print(GTA)

mario_bros = Pagina("Super Mario Bros", 
                    "Jogo de um encanador psicodelico", 
#                    "mario_poster", 
                    "https://i.ytimg.com/vi/1dhrHlol3SM/maxresdefault.jpg"
                    "R$150,00", 
#                    "mario_trailer")
                    "https://www.youtube.com/watch?v=eO8xe2AUY4c")
                    
                    
print(mario_bros)