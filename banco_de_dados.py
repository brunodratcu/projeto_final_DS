# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:34:01 2016
@author: Bruno Dratcu
"""

import tkinter as tk
import dados
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
        
        self.mercado_livre = Image.open("Sites/mercado_livre.png") 
        self.mercado_livre_show = ImageTk.PhotoImage(self.mercado_livre)
        
        self.submarino = Image.open("Sites/submarino.jpg") 
        self.submarino_show = ImageTk.PhotoImage(self.submarino)
        
        self.PS3 = Image.open("Plataformas/PS3.jpg") 
        self.PS3_show = ImageTk.PhotoImage(self.PS3)
        
        self.Xbox_360 = Image.open("Plataformas/xbox-360.jpg") 
        self.Xbox_360_show = ImageTk.PhotoImage(self.Xbox_360)
        
        self.Rockstar = Image.open("Plataformas/Rockstar.jpg") 
        self.Rockstar_show = ImageTk.PhotoImage(self.Rockstar)
        
        self.Xbox_one = Image.open("Plataformas/xbox_one.jpg") 
        self.Xbox_one_show = ImageTk.PhotoImage(self.Xbox_one)
        
        self.Steam = Image.open("Plataformas/steam.jpg") 
        self.Steam_show = ImageTk.PhotoImage(self.Steam)
        
        self.Origin = Image.open("Plataformas/origin.png") 
        self.Origin_show = ImageTk.PhotoImage(self.Origin)
        
        self.WiiU = Image.open("Plataformas/WiiU.png") 
        self.WiiU_show = ImageTk.PhotoImage(self.WiiU)
        
        self.N3DS = Image.open("Plataformas/3DS.png") 
        self.N3DS_show = ImageTk.PhotoImage(self.N3DS)
        
        self.PS4 = Image.open("Plataformas/PS4.jpg") 
        self.PS4_show = ImageTk.PhotoImage(self.PS4)
        
        self.sites_pictures = [self.Americanas_show, self.saraiva_show, self.G2A_show,  self.mercado_livre_show,  self.submarino_show]
        
        self.plataformas_pictures = [self.PS3_show, self.Xbox_360_show, self.Rockstar_show, self.Xbox_one_show, self.Steam_show, self.Origin_show, self.WiiU_show, self.N3DS_show, self.PS4_show]
        
        self.init.withdraw()
       
    def games(self, number):
    
        if number == 1:
        
            self.info = dados.data()
            self.games_data = self.info.read_games("GTA")       
            self.preco = self.games_data[0]
            self.site_link = self.games_data[1]
            self.transform = int(self.games_data[2])
            self.site_im = self.sites_pictures[self.transform]           
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = int(self.games_data[3])
            self.platform_ind = self.plataformas_pictures[self.platform]
            self.game_ID = "{0}".format(number)
            self.poster_GTA_im = Image.open("Images/GTA_poster.jpg")     
            self.poster_Gta_show = ImageTk.PhotoImage(self.poster_GTA_im)
            self.button_Gta_im = Image.open("Images/Gta_Button.jpg") 
            self.button_Gta_show = ImageTk.PhotoImage(self.button_Gta_im)
            self.dict_game_info = { self.game_ID : {"nome": "Grand Theft Auto V", "short": "GTA", "melhor preco" : self.price, "plataforma" : self.platform_ind , "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação.", "poster" : self.poster_Gta_show, "button": self.button_Gta_show}}          
            return self.dict_game_info
        
        elif number == 2:
            
            self.info = dados.data()     
            self.games_data = self.info.read_games("COD3")
            self.preco = self.games_data[0]
            self.site_link = self.games_data[1]
            self.transform = int(self.games_data[2])
            self.site_im = self.sites_pictures[self.transform]           
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = int(self.games_data[3])
            self.platform_ind = self.plataformas_pictures[self.platform]
            self.game_ID = "{0}".format(number)
            self.poster_CO3_im = Image.open("Images/COD_poster.jpg")     
            self.poster_CO3_show = ImageTk.PhotoImage(self.poster_CO3_im)
            self.button_CO3_im = Image.open("Images/COD_Button.jpg")     
            self.button_CO3_show = ImageTk.PhotoImage(self.button_CO3_im)
            self.dict_game_info = { self.game_ID : {"nome": "Call of Duty Black Ops 3", "short": "COD3", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação.", "poster" : self.poster_CO3_show, "button": self.button_CO3_show}}
            return self.dict_game_info
       
        elif number == 3:
            
            self.info = dados.data()     
            self.games_data = self.info.read_games("PACM")
            self.preco = self.games_data[0]
            self.site_link = self.games_data[1]
            self.transform = int(self.games_data[2])
            self.site_im = self.sites_pictures[self.transform]           
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = int(self.games_data[3])
            self.platform_ind = self.plataformas_pictures[self.platform]
            self.game_ID = "{0}".format(number)
            self.poster_PAC_im = Image.open("Images/PAC_poster.jpg")     
            self.poster_PAC_show = ImageTk.PhotoImage(self.poster_PAC_im)
            self.button_PAC_im = Image.open("Images/PAC_Button.jpg")     
            self.button_PAC_show = ImageTk.PhotoImage(self.button_PAC_im) 
            self.dict_game_info = { self.game_ID : {"nome": "Pac-Man", "short": "PACM", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação.", "poster" : self.poster_PAC_show, "button": self.button_PAC_show}}
            return self.dict_game_info     
       
        elif number == 4:
            
            self.info = dados.data()     
            self.games_data = self.info.read_games("MARIO")
            self.preco = self.games_data[0]
            self.site_link = self.games_data[1]
            self.transform = int(self.games_data[2])
            self.site_im = self.sites_pictures[self.transform]           
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = int(self.games_data[3])
            self.platform_ind = self.plataformas_pictures[self.platform]
            self.game_ID = "{0}".format(number)
            self.poster_MARIO_im = Image.open("Images/Mario_poster.jpg")     
            self.poster_MARIO_show = ImageTk.PhotoImage(self.poster_MARIO_im)
            self.button_MARIO_im = Image.open("Images/Mario_Button.png")     
            self.button_MARIO_show = ImageTk.PhotoImage(self.button_MARIO_im)
            self.dict_game_info = { self.game_ID : {"nome": "Mario", "short": "MARIO", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação.", "poster" : self.poster_MARIO_show, "button": self.button_MARIO_show}}
            return self.dict_game_info         
               
        elif number == 5:
            
            self.info = dados.data()     
            self.games_data = self.info.read_games("BF4")
            self.preco = self.games_data[0]
            self.site_link = self.games_data[1]
            self.transform = int(self.games_data[2])
            self.site_im = self.sites_pictures[self.transform]           
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = int(self.games_data[3])
            self.platform_ind = self.plataformas_pictures[self.platform]
            self.game_ID = "{0}".format(number)
            self.poster_BF4_im = Image.open("Images/BF4_poster.jpg")     
            self.poster_BF4_show = ImageTk.PhotoImage(self.poster_BF4_im)
            self.button_BF4_im = Image.open("Images/BF4_Button.jpg")     
            self.button_BF4_show = ImageTk.PhotoImage(self.button_BF4_im)
            self.dict_game_info = { self.game_ID : {"nome": "Battlefield 4", "short":"BF4", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação.", "poster" : self.poster_BF4_show, "button": self.button_BF4_show}}
            return self.dict_game_info     
              
        elif number == 6:
            
            self.info = dados.data()     
            self.games_data = self.info.read_games("PokemonA")
            self.preco = self.games_data[0]
            self.site_link = self.games_data[1]
            self.transform = int(self.games_data[2])
            self.site_im = self.sites_pictures[self.transform]           
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = int(self.games_data[3])
            self.platform_ind = self.plataformas_pictures[self.platform]
            self.game_ID = "{0}".format(number)
            self.poster_PKMA_im = Image.open("Images/PokemonA_poster.jpg")     
            self.poster_PKMA_show = ImageTk.PhotoImage(self.poster_PKMA_im)
            self.button_PKMA_im = Image.open("Images/PokemonA_Button.jpg")     
            self.button_PKMA_show = ImageTk.PhotoImage(self.button_PKMA_im)
            self.dict_game_info = { self.game_ID : {"nome": "Pokemon Alpha Sapphire", "short":"PKMA", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação.", "poster" : self.poster_PKMA_show, "button": self.button_PKMA_show}}
            return self.dict_game_info     
              
        elif number == 7:
            
            self.info = dados.data()     
            self.games_data = self.info.read_games("FIFA16")
            self.preco = self.games_data[0]
            self.site_link = self.games_data[1]
            self.transform = int(self.games_data[2])
            self.site_im = self.sites_pictures[self.transform]           
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = int(self.games_data[3])
            self.platform_ind = self.plataformas_pictures[self.platform]
            self.game_ID = "{0}".format(number)
            self.poster_FIFA16_im = Image.open("Images/FIFA2016_poster.jpg")     
            self.poster_FIFA16_show = ImageTk.PhotoImage(self.poster_FIFA16_im)
            self.button_FIFA16_im = Image.open("Images/FIFA2016_Button.jpg")     
            self.button_FIFA16_show = ImageTk.PhotoImage(self.button_FIFA16_im)
            self.dict_game_info = { self.game_ID : {"nome": "FIFA 2016", "short":"FIFA16", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação.", "poster" : self.poster_FIFA16_show, "button": self.button_FIFA16_show}}           
            return self.dict_game_info     
              
        elif number == 8:
            
            self.info = dados.data()     
            self.games_data = self.info.read_games("MARIOKART")
            self.preco = self.games_data[0]
            self.site_link = self.games_data[1]
            self.transform = int(self.games_data[2])
            self.site_im = self.sites_pictures[self.transform]           
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = int(self.games_data[3])
            self.platform_ind = self.plataformas_pictures[self.platform]
            self.game_ID = "{0}".format(number)
            self.poster_MARIOK_im = Image.open("Images/MARIOK_poster.jpg")     
            self.poster_MARIOK_show = ImageTk.PhotoImage(self.poster_MARIOK_im)
            self.button_MARIOK_im = Image.open("Images/MARIOK_Button.png")     
            self.button_MARIOK_show = ImageTk.PhotoImage(self.button_MARIOK_im)
            self.dict_game_info = { self.game_ID : {"nome": "Mario Kart", "short":"MARIOK", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação.", "poster" : self.poster_MARIOK_show, "button": self.button_MARIOK_show}}         
            return self.dict_game_info          
              
        elif number == 9:
            
            self.info = dados.data()     
            self.games_data = self.info.read_games("NFSR")
            self.preco = self.games_data[0]
            self.site_link = self.games_data[1]
            self.transform = int(self.games_data[2])
            self.site_im = self.sites_pictures[self.transform]           
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = int(self.games_data[3])
            self.platform_ind = self.plataformas_pictures[self.platform]
            self.game_ID = "{0}".format(number)
            self.poster_NFSR_im = Image.open("Images/NFSR_poster.jpg")     
            self.poster_NFSR_show = ImageTk.PhotoImage(self.poster_NFSR_im)
            self.button_NFSR_im = Image.open("Images/NFSR_Button.jpg")     
            self.button_NFSR_show = ImageTk.PhotoImage(self.button_NFSR_im)
            self.dict_game_info = { self.game_ID : {"nome": "Need for Speed Rivals", "short":"NFSR", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação.", "poster" : self.poster_NFSR_show, "button": self.button_NFSR_show}}             
            return self.dict_game_info          
              
        elif number == 10:
            
            self.info = dados.data()     
            self.games_data = self.info.read_games("SFV")
            self.preco = self.games_data[0]
            self.site_link = self.games_data[1]
            self.transform = int(self.games_data[2])
            self.site_im = self.sites_pictures[self.transform]           
            self.preco_l = "R${0}".format(self.preco)
            self.inter = self.preco_l.split(".", 2)    
            self.price = "{0},{1}".format(self.inter[0], self.inter[1])
            self.platform = int(self.games_data[3])
            self.platform_ind = self.plataformas_pictures[self.platform]
            self.game_ID = "{0}".format(number)
            self.poster_SFV_im = Image.open("Images/SFV_poster.jpg")     
            self.poster_SFV_show = ImageTk.PhotoImage(self.poster_SFV_im)
            self.button_SFV_im = Image.open("Images/SFV_Button.jpg")     
            self.button_SFV_show = ImageTk.PhotoImage(self.button_SFV_im)
            self.dict_game_info = { self.game_ID : {"nome": "Street Fighter V", "short":"SFV", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação.", "poster" : self.poster_SFV_show, "button": self.button_SFV_show}}
            return self.dict_game_info

    
