# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:34:01 2016

@author: Bruno Dratcu
"""

from random import randint
import tkinter as tk
from PIL import Image, ImageTk

class Games:
    
    def __init__(self):
        
        
        self.init = tk.Tk()
        
        self.G2A = Image.open("Sites/G2A.jpeg") 
        self.G2A_show = ImageTk.PhotoImage(self.G2A)
        
        self.Americanas = Image.open("Sites/americanas.jpg") 
        self.Americanas_show = ImageTk.PhotoImage(self.Americanas)
        
        self.saraiva = Image.open("Sites/saraiva.jpg") 
        self.saraiva_show = ImageTk.PhotoImage(self.saraiva)
        
        self.init.withdraw()
       
    def games(self, number):
    
        if number == 1:
            
            self.sites_pictures = [self.Americanas_show, self.saraiva_show, self.G2A_show]        
            self.precos_games = [122.33,134.91,133.09]
            self.plataformas = ["PS3","XBOX 360","Rockstar Club"]
            self.sites_games = ["http://www.americanas.com.br/produto/113150110/game-grand-theft-auto-v-ps3?opn=YSMESP&loja=02&WT.srch=1&epar=bp_pl_00_go_pla-gmjogos-todas",
                                "http://www.saraiva.com.br/gta-grand-theft-auto-v-x360-4851893.html?sku=4851893&force_redirect=1&PAC_ID=123134&gclid=CODQw43s6MwCFUsJkQod3d0E2w",
                                "https://www.g2a.com/grand-theft-auto-v-cd-key-global.html?___store=brazil&___currency=BRL&adid=GMC&id=64&gclid=CKCp-ovs6MwCFYaAkQodxv8BLw"]
            self.number_r = randint(0,2)        
            self.preco = self.precos_games[self.number_r]
            self.site_im = self.sites_pictures[self.number_r]
            self.site_link = self.sites_games[self.number_r]
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = self.plataformas[self.number_r]
            self.dict_game_info = { "Grand Theft Auto V" : {"melhor preco" : self.preco_l, "plataforma" : self.platform, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação."}}
            return self.dict_game_info
        
        elif number == 2:
            
            self.sites_pictures = [self.Americanas_show, self.saraiva_show, self.G2A_show]        
            self.precos_games = [158.33,206.91,118.12]
            self.plataformas = ["XBOX ONE","XBOX ONE","Steam"]
            self.sites_games = ["http://www.americanas.com.br/produto/124606848/game-call-of-duty-black-ops-3-xbox-one?opn=YSMESP&loja=02&WT.srch=1&epar=bp_pl_00_go_pla-gmjogos-todas",
                                "http://www.saraiva.com.br/call-of-duty-black-ops-iii-xbox-one-9201680.html?sku=9201680&force_redirect=1&PAC_ID=123134&gclid=COnL6_z86MwCFcQIkQodhAACHg",
                                "https://www.g2a.com/call-of-duty-black-ops-iii-steam-cd-key-preorder-global.html?___store=brazil&___currency=BRL&adid=GMC&id=64&gclid=CITMnNn86MwCFYIGkQodApgIbw"]
            self.number_r = randint(0,2)        
            self.preco = self.precos_games[self.number_r]
            self.site_im = self.sites_pictures[self.number_r]
            self.site_link = self.sites_games[self.number_r]
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = self.plataformas[self.number_r]
            self.dict_game_info = { "Call of Duty Black Ops 3" : {"melhor preco" : self.preco_l, "plataforma" : self.platform, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação."}}
            return self.dict_game_info
       
        elif number == 3:
            
            self.sites_pictures = [self.Americanas_show, self.saraiva_show, self.G2A_show]        
            self.precos_games = [0,0,15.12]
            self.plataformas = ["XBOX ONE","PS3","Steam"]
            self.sites_games = ["http://www.americanas.com.br/produto/116558954/game-pac-man-and-the-ghostly-adventures-xbox-360",
                                "http://www.saraiva.com.br/pac-man-e-as-aventuras-fantasmagoricas-ps3-5914934.html",
                                "https://www.g2a.com/pac-man-championship-edition-dx-all-you-can-eat-edition-steam-cd-key-global.html"]
            self.number_r = randint(0,2)        
            self.preco = self.precos_games[self.number_r]
            self.site_im = self.sites_pictures[self.number_r]
            self.site_link = self.sites_games[self.number_r]
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = self.plataformas[self.number_r]
            self.dict_game_info = { "Pac-Man" : {"melhor preco" : self.preco_l, "plataforma" : self.platform, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação."}}
            return self.dict_game_info     
       
        elif number == 4:
            
            self.sites_pictures = [self.Americanas_show, self.saraiva_show, self.G2A_show]        
            self.precos_games = [386.72,206.91,118.12]
            self.plataformas = ["Wii U","XBOX ONE","Nintendo 3DS"]
            self.sites_games = ["http://www.americanas.com.br/produto/116707930/game-new-super-mario-bros.-u-wii-u",
                                "http://www.saraiva.com.br/call-of-duty-black-ops-iii-xbox-one-9201680.html?sku=9201680&force_redirect=1&PAC_ID=123134&gclid=COnL6_z86MwCFcQIkQodhAACHg",
                                "https://www.g2a.com/new-super-mario-bros-2-nintendo-3ds-cd-key-global.html"]
            self.number_r = randint(0,2)        
            self.preco = self.precos_games[self.number_r]
            self.site_im = self.sites_pictures[self.number_r]
            self.site_link = self.sites_games[self.number_r]
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = self.plataformas[self.number_r]
            self.dict_game_info = { "Super Mario Bros" : {"melhor preco" : self.preco_l, "plataforma" : self.platform, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação."}}
            return self.dict_game_info     
            return self.dict_game_info     
