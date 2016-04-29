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

        
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
        
        

        