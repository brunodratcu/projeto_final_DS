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
            self.sites_games = ["http://goo.gl/6LD7Ki",
                                "http://goo.gl/ktwTaY",
                                "https://goo.gl/XZ7EJd"]
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
            self.sites_games = ["http://goo.gl/qlcOKO",
                                "http://goo.gl/T6Scdm",
                                "https://goo.gl/dddh2s"]
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
            self.sites_games = ["http://goo.gl/nnqyZa",
                                "http://goo.gl/f87mMp",
                                "https://goo.gl/N8Cv0b"]
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
            self.sites_games = ["http://goo.gl/MYfto4",
                                "http://goo.gl/ChcZTo",
                                "https://goo.gl/e6dSMO"]
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
               
        elif number == 5:
            
            self.sites_pictures = [self.Americanas_show, self.saraiva_show, self.G2A_show]        
            self.precos_games = [120.90,0,155.61]
            self.plataformas = ["XBOX ONE","PS4","Origin"]
            self.sites_games = ["http://goo.gl/Fr2EJu",
                                "http://goo.gl/ezNgwP",
                                "https://goo.gl/OlJkSo"]
            self.number_r = randint(0,2)        
            self.preco = self.precos_games[self.number_r]
            self.site_im = self.sites_pictures[self.number_r]
            self.site_link = self.sites_games[self.number_r]
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = self.plataformas[self.number_r]
            self.dict_game_info = { "Battlefield 4" : {"melhor preco" : self.preco_l, "plataforma" : self.platform, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação."}}
            return self.dict_game_info     
              
        elif number == 6:
            
            self.sites_pictures = [self.Americanas_show, self.saraiva_show, self.G2A_show]        
            self.precos_games = [179.90,0,0]
            self.plataformas = ["Nintendo 3DS","Nintendo 3DS","Nintendo 3DS"]
            self.sites_games = ["http://goo.gl/rfGEfS",
                                "http://goo.gl/FWKKiC",
                                "https://goo.gl/L4Vu9T"]
            self.number_r = randint(0,2)        
            self.preco = self.precos_games[self.number_r]
            self.site_im = self.sites_pictures[self.number_r]
            self.site_link = self.sites_games[self.number_r]
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = self.plataformas[self.number_r]
            self.dict_game_info = { "Pokemon" : {"melhor preco" : self.preco_l, "plataforma" : self.platform, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação."}}
            return self.dict_game_info     
              
        elif number == 7:
            
            self.sites_pictures = [self.Americanas_show, self.saraiva_show, self.G2A_show]        
            self.precos_games = [179.90,179.90,130.45]
            self.plataformas = ["XBOX ONE","PS4","Origin"]
            self.sites_games = ["http://goo.gl/vRfqu0",
                                "http://goo.gl/VknbdA",
                                "https://goo.gl/LSKDT8"]
            self.number_r = randint(0,2)        
            self.preco = self.precos_games[self.number_r]
            self.site_im = self.sites_pictures[self.number_r]
            self.site_link = self.sites_games[self.number_r]
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = self.plataformas[self.number_r]
            self.dict_game_info = { "Fifa 2016" : {"melhor preco" : self.preco_l, "plataforma" : self.platform, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação."}}
            return self.dict_game_info     
              
        elif number == 8:
            
            self.sites_pictures = [self.Americanas_show, self.saraiva_show, self.G2A_show]        
            self.precos_games = [259.90,0,0]
            self.plataformas = ["Wii U","Nintendo DS","Wii U"]
            self.sites_games = ["http://goo.gl/ZLzbNa",
                                "http://goo.gl/5KYDJg",
                                "https://goo.gl/wUsfI0"]
            self.number_r = randint(0,2)        
            self.preco = self.precos_games[self.number_r]
            self.site_im = self.sites_pictures[self.number_r]
            self.site_link = self.sites_games[self.number_r]
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = self.plataformas[self.number_r]
            self.dict_game_info = { "Mario Kart" : {"melhor preco" : self.preco_l, "plataforma" : self.platform, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação."}}
            return self.dict_game_info     
              
        elif number == 9:
            
            self.sites_pictures = [self.Americanas_show, self.saraiva_show, self.G2A_show]        
            self.precos_games = [169.90,279.90,150.58]
            self.plataformas = ["XBOX 360","PS4","Origin"]
            self.sites_games = ["http://goo.gl/jQQczN",
                                "http://goo.gl/7AyCuS",
                                "https://goo.gl/reAuU1"]
            self.number_r = randint(0,2)        
            self.preco = self.precos_games[self.number_r]
            self.site_im = self.sites_pictures[self.number_r]
            self.site_link = self.sites_games[self.number_r]
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = self.plataformas[self.number_r]
            self.dict_game_info = { "Need for Speed" : {"melhor preco" : self.preco_l, "plataforma" : self.platform, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação."}}
            return self.dict_game_info     
              
        elif number == 10:
            
            self.sites_pictures = [self.Americanas_show, self.saraiva_show, self.G2A_show]        
            self.precos_games = [269.99,149.90,123.75]
            self.plataformas = ["XBOX 360","PS4","Steam"]
            self.sites_games = ["http://goo.gl/H9OSUu",
                                "http://goo.gl/S5Hi6T",
                                "https://goo.gl/9OsYXh"]
            self.number_r = randint(0,2)        
            self.preco = self.precos_games[self.number_r]
            self.site_im = self.sites_pictures[self.number_r]
            self.site_link = self.sites_games[self.number_r]
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = self.plataformas[self.number_r]
            self.dict_game_info = { "Street Fighter" : {"melhor preco" : self.preco_l, "plataforma" : self.platform, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação."}}
            return self.dict_game_info
       
#teste2