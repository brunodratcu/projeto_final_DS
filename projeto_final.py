# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:34:01 2016

@author: Bruno Dratcu
"""

import webbrowser
import projeto_final_2



class Pagina:
    """Classe que irá abrir uma pagina para mostrar dados de jogos"""   
    
    def __init__(self, busca, titulo, descricao, preco, trailer, poster):
        self.busca = busca
        self.titulo = titulo
        self.descricao = descricao
        self.preco = preco
        self.trailer = trailer
        self.poster = poster

    def buscar(self):
        self.busca = True
        
    def show_titulo(self):
        if self.busca:
            print(self.titulo)
        
    def show_descricao(self):
        if self.titulo:
            print(self.descricao)
    
    def show_preco(self):
        if self.titulo:
            print(self.preco)
            
    def show_trailer(self):
        if self.titulo:
            webbrowser.open(self.trailer)
            
    def show_poster(self):
        if self.titulo:
            webbrowser.open(self.poster)



gta = Pagina(True, 
             "GTA", 
             "Jogo de um maniaco que mata todo mundo", 
             "R$200,00", 
             "https://www.youtube.com/watch?v=VjZ5tgjPVfU", 
             "http://cdn.atl.clicrbs.com.br/wp-content/uploads/sites/27/2015/04/actual_1410520494.jpg")

mario_bros = Pagina(True,
                    "Super Mario Bros",
                    "Jogo de um encanador psicodelico", 
                    "R$150,00",
                    "https://www.youtube.com/watch?v=eO8xe2AUY4c",
                    "https://i.ytimg.com/vi/1dhrHlol3SM/maxresdefault.jpg")
                    
pac_man = Pagina(True,
                 "Pac-Man",
                 "Bolinha amarela que fica numa sala escura e quando come um doce tem poderes para comer fantasmas",
                 "R$100,00",
                 "https://www.youtube.com/watch?v=CFWnTu_42d0",
                 "http://www.redefonte.com/wp-content/uploads/2013/06/Pacman-Online.jpg")
                    
print(gta.titulo)
#print(gta.descricao)
#print(gta.preco)
#print(gta.trailer)
#print(gta.poster)
#gta.show_trailer()
#gta.show_poster()

print()

print(mario_bros.titulo)
#print(mario_bros.descricao)
#print(mario_bros.preco)
#print(mario_bros.trailer)
#print(mario_bros.poster)
#mario_bros.show_trailer()
#mario_bros.show_poster()

print()

print(pac_man.titulo)
#print(pac_man.descricao)
#print(pac_man.preco)
#print(pac_man.trailer)
#print(pac_man.poster)
#pac_man.show_trailer()
#pac_man.show_poster()

    
    
jogos = [gta, mario_bros, pac_man]
projeto_final_2.open_movies_page(jogos)