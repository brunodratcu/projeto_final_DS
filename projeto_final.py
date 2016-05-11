# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:34:01 2016

@author: Bruno Dratcu
"""

import webbrowser
import projeto_final_2



class Pagina:
    """Classe que irá abrir uma pagina para mostrar dados de jogos"""   
    
    def __init__(self, games, titulo, descricao, preco, trailer, poster):
        self.games = games
        self.titulo = titulo
        self.descricao = descricao
        self.preco = preco
        self.trailer = trailer
        self.poster = poster

    def show_games(self):
        self.games = True
        
    def show_titulo(self):
        if self.games:
            print(self.titulo)
        
    def show_descricao(self):
        if self.titulo:
            print(self.descricao)
            webbrowser.open(self.preco)
    
    def show_preco(self):
        if self.titulo:
            webbrowser.open(self.preco)
            
    def show_trailer(self):
        if self.titulo:
            webbrowser.open(self.trailer)
            
    def show_poster(self):
        if self.titulo:
            webbrowser.open(self.poster)
            
def show_buscar_jogos():
    if nomes_jogos == "GTA" or nomes_jogos == "gta":
        gta.show_descricao()
    elif nomes_jogos == "Mario Bros" or nomes_jogos == "mario bros":
        mario_bros.show_descricao()
    elif nomes_jogos == "pac man" or nomes_jogos == "Pac Man" or nomes_jogos == "Pac-Man":
        pac_man.show_descricao()
    elif nomes_jogos == "call of duty" or nomes_jogos == "Call of Duty":
        call_of_duty.show_descricao()
    else:
        print("Jogo não encontrado!")
            
            
nomes_jogos = input("Qual o game desejado? ")


gta = Pagina(True, 
             "GTA V", 
             "Jogo de um maniaco que mata todo mundo", 
             "http://www.uzgames.com.br/gta?&utmi_p=_games&utmi_pc=BuscaFullText&utmi_cp=gta", 
             "https://www.youtube.com/watch?v=VjZ5tgjPVfU", 
             "http://cdn.atl.clicrbs.com.br/wp-content/uploads/sites/27/2015/04/actual_1410520494.jpg")

mario_bros = Pagina(True,
                    "Super Mario Bros",
                    "Jogo de um encanador psicodelico", 
                    "http://www.uzgames.com.br/mario%20bros?&utmi_p=_gta&utmi_pc=BuscaFullText&utmi_cp=mario%20bros",
                    "https://www.youtube.com/watch?v=eO8xe2AUY4c",
                    "https://i.ytimg.com/vi/1dhrHlol3SM/maxresdefault.jpg")
                    
pac_man = Pagina(True,
                 "Pac-Man",
                 "Bolinha amarela que fica numa sala escura e quando come um doce tem poderes para comer fantasmas",
                 "http://www.uzgames.com.br/pac%20man?&utmi_p=_gta&utmi_pc=BuscaFullText&utmi_cp=pac%20man",
                 "https://www.youtube.com/watch?v=CFWnTu_42d0",
                 "http://www.redefonte.com/wp-content/uploads/2013/06/Pacman-Online.jpg")
                 
call_of_duty = Pagina(True,
                      "Call of Duty",
                      "Jogo no qual vc pode atirar em outros usuarios online",
                      "http://www.uzgames.com.br/call%20of%20duty%20ghosts?&utmi_p=_call+of+duty+gosth&utmi_pc=BuscaFullText&utmi_cp=call%20of%20duty%20ghosts",
                      "https://www.youtube.com/watch?v=ktz5G24BOsg",
                      "http://cdn2-www.comingsoon.net/assets/uploads/2015/04/cod-bo3-header2.jpg")
                      
                      
show_buscar_jogos()

#print()
#                      
#
#print(gta.titulo)
#print(gta.descricao)
#print(gta.preco)
#print(gta.trailer)
#print(gta.poster)
#                    
#gta.show_trailer()
#gta.show_poster()
#gta.show_preco()
#
#print()
#
#print(mario_bros.titulo)
#print(mario_bros.descricao)
#print(mario_bros.preco)
#print(mario_bros.trailer)
#print(mario_bros.poster)
#
#mario_bros.show_trailer()
#mario_bros.show_poster()
#mario_bros.show_preco()
#
#print()
#
#print(pac_man.titulo)
#print(pac_man.descricao)
#print(pac_man.preco)
#print(pac_man.trailer)
#print(pac_man.poster)
#
#pac_man.show_trailer()
#pac_man.show_poster()
#pac_man.show_preco()
#
#print()
#
#print(call_of_duty.titulo)
#print(call_of_duty.descricao)
#print(call_of_duty.preco)
#print(call_of_duty.trailer)
#print(call_of_duty.poster)
#
#call_of_duty.show_trailer()
#call_of_duty.show_poster()
#call_of_duty.show_preco()

    
    
jogos = [gta, mario_bros, pac_man, call_of_duty]
#projeto_final_2.open_movies_page(jogos)