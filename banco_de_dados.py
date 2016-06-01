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
       
        self.dict_game_info = {}
        
    def games(self, number):
    
        self.info = dados.data() 
        
        if number == 1:
                
            self.games_data = self.info.read_games("GTA")
            self.read_games()
            self.game_ID = "{0}".format(number)
            self.poster_GTA_im = Image.open("Images/GTA_poster.jpg")     
            self.poster_Gta_show = ImageTk.PhotoImage(self.poster_GTA_im)
            self.button_Gta_im = Image.open("Images/Gta_Button.jpg") 
            self.button_Gta_show = ImageTk.PhotoImage(self.button_Gta_im)
            self.descrição = "Grand Theft Auto V, ou simplesmente GTA V, é um jogo de ação e aventura em mundo aberto desenvolvido pela empresa britânica Rockstar North e publicado pela Rockstar Games no dia 17 de setembro de 2013 para os videogames Playstation 3 e Xbox 360. Uma versão melhorada do game foi lançada para Playstation 4 e Xbox One em 18 de novembro de 2014 e para computadores foi lançada no dia 14 de abril de 2015. É o décimo quinto jogo da série Grand Theft Auto (incluindo as expansões) desde Grand Theft Auto IV (2008) e a continuação do universo fictício que foi introduzido neste jogo. "
            self.dict_game_info[self.game_ID] = {"nome": "Grand Theft Auto V", "short": "GTA", "melhor preco" : self.price, "plataforma" : self.platform_ind , "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : self.descrição, "poster" : self.poster_Gta_show, "button": self.button_Gta_show}          
        
        elif number == 2:
            
            self.games_data = self.info.read_games("COD3")
            self.read_games()
            self.game_ID = "{0}".format(number)
            self.poster_CO3_im = Image.open("Images/COD_poster.jpg")     
            self.poster_CO3_show = ImageTk.PhotoImage(self.poster_CO3_im)
            self.button_CO3_im = Image.open("Images/COD_Button.jpg")     
            self.button_CO3_show = ImageTk.PhotoImage(self.button_CO3_im)
            self.descrição = "Call of Duty: Black Ops III é um jogo eletrônico de tiro produzido pela empresa Treyarch e lançado no dia 6 de novembro de 2015 pela Activision para Microsoft Windows, PlayStation 4 e Xbox One. É o décimo terceiro título Call of Duty, contudo, a campanha desse jogo não é uma continuação do arco Black Ops, que se iniciou em Call of Duty: World at War (2008) e foi até Black Ops II."
            self.dict_game_info[self.game_ID] = {"nome": "Call of Duty Black Ops 3", "short": "COD3", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : self.descrição, "poster" : self.poster_CO3_show, "button": self.button_CO3_show}
       
        elif number == 3:
            
            self.games_data = self.info.read_games("PACM")
            self.read_games()
            self.game_ID = "{0}".format(number)
            self.poster_PAC_im = Image.open("Images/PAC_poster.jpg")     
            self.poster_PAC_show = ImageTk.PhotoImage(self.poster_PAC_im)
            self.button_PAC_im = Image.open("Images/PAC_Button.jpg")     
            self.button_PAC_show = ImageTk.PhotoImage(self.button_PAC_im) 
            self.descrição = "Pac-Man (Puckman ou パックマン) é um jogo eletrônico criado pelo Tōru Iwatani para a empresa Namco, e sendo distribuído para o mercado estadunidense pela Midway Games. Produzido originalmente para Arcade no início dos anos 1980, tornou-se um dos jogos mais populares no momento, tendo versões para diversos consoles e continuações para tantos outros, inclusive na atualidade."
            self.dict_game_info[self.game_ID] = {"nome": "Pac-Man", "short": "PACM", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : self.descrição, "poster" : self.poster_PAC_show, "button": self.button_PAC_show}
       
        elif number == 4:
            
            self.games_data = self.info.read_games("MARIO")
            self.read_games()
            self.game_ID = "{0}".format(number)
            self.poster_MARIO_im = Image.open("Images/Mario_poster.jpg")     
            self.poster_MARIO_show = ImageTk.PhotoImage(self.poster_MARIO_im)
            self.button_MARIO_im = Image.open("Images/Mario_Button.png")     
            self.button_MARIO_show = ImageTk.PhotoImage(self.button_MARIO_im)
            self.descrição = "New Super Mario Bros. Wii é um videogame do gênero de plataforma desenvolvido e publicado pela empresa japonesa Nintendo para o console de videogame Wii. O jogo foi lançado em 12 de novembro de 2009 na Austrália, 15 de novembro na América do Norte, 20 de novembro de 2009 na Europa e 3 de dezembro de 2009 no Japão."
            self.dict_game_info[self.game_ID] = {"nome": "Mario", "short": "MARIO", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : self.descrição, "poster" : self.poster_MARIO_show, "button": self.button_MARIO_show}
            
        elif number == 5:
            
            self.games_data = self.info.read_games("BF4")
            self.read_games()
            self.game_ID = "{0}".format(number)
            self.poster_BF4_im = Image.open("Images/BF4_poster.jpg")     
            self.poster_BF4_show = ImageTk.PhotoImage(self.poster_BF4_im)
            self.button_BF4_im = Image.open("Images/BF4_Button.jpg")     
            self.button_BF4_show = ImageTk.PhotoImage(self.button_BF4_im)
            self.descrição = "Battlefield 4 (abreviado como BF4) é um jogo de tiro em primeira pessoa desenvolvido pela EA Digital Illusions CE (DICE) e publicado pela Electronic Arts. É o décimo terceiro título da série, sequência de Battlefield 3, e foi lançado entre outubro e novembro de 2013 para Microsoft Windows, PlayStation 3, Xbox 360, PlayStation 4 e Xbox One."
            self.dict_game_info[self.game_ID] = {"nome": "Battlefield 4", "short":"BF4", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : self.descrição, "poster" : self.poster_BF4_show, "button": self.button_BF4_show}
                 
        elif number == 6:
            
            self.games_data = self.info.read_games("PokemonA")
            self.read_games()
            self.game_ID = "{0}".format(number)
            self.poster_PKMA_im = Image.open("Images/PokemonA_poster.jpg")     
            self.poster_PKMA_show = ImageTk.PhotoImage(self.poster_PKMA_im)
            self.button_PKMA_im = Image.open("Images/PokemonA_Button.jpg")     
            self.button_PKMA_show = ImageTk.PhotoImage(self.button_PKMA_im)
            self.descrição = "Pokémon Alpha Sapphire (アルファサファイア, Arufa Safaia?) são dois videogames lançados para Nintendo 3DS. Ele é remake do jogo de 2002, Pokémon Sapphire, do Game Boy Advance.Foi anunciado em 7 de maio de 2014, através de um trailer divulgado pela Nintendo."
            self.dict_game_info[self.game_ID] = {"nome": "Pokemon Alpha Sapphire", "short":"PKMA", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : self.descrição, "poster" : self.poster_PKMA_show, "button": self.button_PKMA_show}
                          
        elif number == 7:
              
            self.games_data = self.info.read_games("FIFA16")
            self.read_games()
            self.game_ID = "{0}".format(number)
            self.poster_FIFA16_im = Image.open("Images/FIFA2016_poster.jpg")     
            self.poster_FIFA16_show = ImageTk.PhotoImage(self.poster_FIFA16_im)
            self.button_FIFA16_im = Image.open("Images/FIFA2016_Button.jpg")     
            self.button_FIFA16_show = ImageTk.PhotoImage(self.button_FIFA16_im)
            self.descrição = "FIFA 16 é um jogo de simulação de futebol lançado pela EA Sports para Windows, PlayStation 3, PlayStation 4, Xbox 360, Xbox One, Android e iOS no dia 22 de setembro de 2015, sendo o primeiro da série que inclui o futebol feminino, com doze seleções nacionais: a Austrália, o Brasil, o Canadá, a China, a Inglaterra, a França, a Alemanha, a Itália, o México, a Espanha, a Suécia e os Estados Unidos."
            self.dict_game_info[self.game_ID] = {"nome": "FIFA 2016", "short":"FIFA16", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : self.descrição, "poster" : self.poster_FIFA16_show, "button": self.button_FIFA16_show}          
              
        elif number == 8:
            
            self.games_data = self.info.read_games("MARIOKART")
            self.read_games()
            self.game_ID = "{0}".format(number)
            self.poster_MARIOK_im = Image.open("Images/MARIOK_poster.jpg")     
            self.poster_MARIOK_show = ImageTk.PhotoImage(self.poster_MARIOK_im)
            self.button_MARIOK_im = Image.open("Images/MARIOK_Button.png")     
            self.button_MARIOK_show = ImageTk.PhotoImage(self.button_MARIOK_im)
            self.descrição = "Mario Kart (マリオカート, Mario Kāto) é uma série de jogos de corrida desenvolvida e publicada pela Nintendo como spin-off da franquia Mario. O primeiro da série, Super Mario Kart, foi lançado em 1992 para o Super Nintendo Entertainment System e é considerado um dos jogos mais influentes da história."
            self.dict_game_info[self.game_ID] = {"nome": "Mario Kart", "short":"MARIOK", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : self.descrição, "poster" : self.poster_MARIOK_show, "button": self.button_MARIOK_show}
              
        elif number == 9:
            
            self.games_data = self.info.read_games("NFSR")
            self.read_games()
            self.game_ID = "{0}".format(number)
            self.poster_NFSR_im = Image.open("Images/NFSR_poster.jpg")     
            self.poster_NFSR_show = ImageTk.PhotoImage(self.poster_NFSR_im)
            self.button_NFSR_im = Image.open("Images/NFSR_Button.jpg")     
            self.button_NFSR_show = ImageTk.PhotoImage(self.button_NFSR_im)
            self.descrição = "Need for Speed: Rivals é um jogo eletrônico de corrida em mundo aberto que foi desenvolvido pela desenvolvedora sueca Ghost Games e que é publicado pela Electronic Arts. Foi lançado em Novembro de 2013 para Xbox 360, Xbox One, Microsoft Windows, PlayStation 3 e PlayStation 4."
            self.dict_game_info[self.game_ID] = {"nome": "Need for Speed Rivals", "short":"NFSR", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : self.descrição, "poster" : self.poster_NFSR_show, "button": self.button_NFSR_show}                    
              
        elif number == 10:
            
            self.games_data = self.info.read_games("SFV")
            self.read_games()
            self.game_ID = "{0}".format(number)
            self.poster_SFV_im = Image.open("Images/SFV_poster.jpg")     
            self.poster_SFV_show = ImageTk.PhotoImage(self.poster_SFV_im)
            self.button_SFV_im = Image.open("Images/SFV_Button.jpg")     
            self.button_SFV_show = ImageTk.PhotoImage(self.button_SFV_im)
            self.descrição = "Street Fighter V (ストリートファイターV, Sutorīto Faitā Faibu?) é um videojogo de luta publicado pela Capcom, que o produziu em colaboração com o estúdio Dimps. O quinto capitulo da série Street Fighter, foi lançado a 16 de Fevereiro de 2016 para Microsoft Windows e PlayStation 4. Uma versão para Linux tem lançamento previsto para o segundo trimestre de 2016."
            self.dict_game_info[self.game_ID] = {"nome": "Street Fighter V", "short":"SFV", "melhor preco" : self.price, "plataforma" : self.platform_ind, "melhor preco imagem" : self.site_im  , "melhor preco link" : self.site_link, "descrição" : self.descrição, "poster" : self.poster_SFV_show, "button": self.button_SFV_show}
     
        return self.dict_game_info    
 
    def read_games(self):    
        self.preco = self.games_data[0]
        self.site_link = self.games_data[1]
        self.transform = int(self.games_data[2])
        self.site_im = self.sites_pictures[self.transform]           
        self.preco_l = "R${0}".format(self.preco)
        self.inter = self.preco_l.split(".", 2)    
        self.price = "{0},{1}".format(self.inter[0], self.inter[1])
        self.platform = int(self.games_data[3])
        self.platform_ind = self.plataformas_pictures[self.platform]
        return
