# -*- coding: utf-8 -*-

"""
Created on Fri Apr 29 14:13:19 2016

@author: Gabriel
"""

import tkinter as tk
import pickle
import webbrowser
from PIL import Image, ImageTk

class Main_Window:
    
    def __init__(self):
        
        self.core = tk.Tk()            
        self.core.resizable(height = False, width=False)
        self.core.title("Synchromatic")
        self.core.geometry("650x670")

        self.image1 = Image.open("Images/Main_Button.jpg")     
        self.init = ImageTk.PhotoImage(self.image1)
        self.image2 = Image.open("Images/syn.jpg")     
        self.init2 = ImageTk.PhotoImage(self.image2)
        
        self.Main_Menu_im = Image.open("Images/Main_Menu.png")  
        self.Main_Menu = ImageTk.PhotoImage(self.Main_Menu_im) 
        self.My_Fav_im = Image.open("Images/Meus_Favoritos.png")  
        self.My_Fav = ImageTk.PhotoImage(self.My_Fav_im) 

        self.poster_GTA_im = Image.open("Images/GTA_poster.jpg")     
        self.poster_Gta_show = ImageTk.PhotoImage(self.poster_GTA_im)

        self.button_Gta_im = Image.open("Images/Gta_Button.jpg") 
        self.button_Gta_show = ImageTk.PhotoImage(self.button_Gta_im)

        self.poster_CO3_im = Image.open("Images/COD_poster.jpg")     
        self.poster_CO3_show = ImageTk.PhotoImage(self.poster_CO3_im)
        
        self.button_CO3_im = Image.open("Images/COD_Button.jpg")     
        self.button_CO3_show = ImageTk.PhotoImage(self.button_CO3_im)

        self.poster_PAC_im = Image.open("Images/PAC_poster.jpg")     
        self.poster_PAC_show = ImageTk.PhotoImage(self.poster_PAC_im)

        self.button_PAC_im = Image.open("Images/PAC_Button.jpg")     
        self.button_PAC_show = ImageTk.PhotoImage(self.button_PAC_im) 

        self.poster_MARIO_im = Image.open("Images/Mario_poster.jpg")     
        self.poster_MARIO_show = ImageTk.PhotoImage(self.poster_MARIO_im)
        
        self.button_MARIO_im = Image.open("Images/Mario_Button.png")     
        self.button_MARIO_show = ImageTk.PhotoImage(self.button_MARIO_im)
        
        self.avatar_im = Image.open("Images/Login_avatar.jpg")     
        self.avatar_im_show = ImageTk.PhotoImage(self.avatar_im)
 
        self.fav_im = Image.open("Images/Favorite.png")
        self.fav = ImageTk.PhotoImage(self.fav_im)
        self.not_fav_im = Image.open("Images/Not_Favorite.jpg")
        self.not_fav = ImageTk.PhotoImage(self.not_fav_im)           
        self.uz_im = Image.open("Images/uz-games.jpg")
        self.UZ = ImageTk.PhotoImage(self.uz_im)
        self.Login = tk.StringVar()
        self.Senha = tk.StringVar()
        self.Login_show = tk.StringVar()
        for linhas in range (0,15):
           self.core.rowconfigure(linhas, weight=1)
        for colunas in range (0,8):        
           self.core.columnconfigure(colunas, weight=1)
        self.Main_BG = tk.Label(self.core, image = self.init2)
        self.Main_BG.configure(bg = "black")      
        self.Main_BG.grid(row=0, column=0, columnspan=8, rowspan = 15 ,sticky="nsew") 
        self.Button_Main = tk.Button(self.core,image=self.init, bg = "black", width = 130, height = 120,command = self.Begin)
        self.Button_Main.place(x = 256, y = 230) 
        self.lista_games = {"GTA": [self.button_Gta_show, 1], "COD": [self.button_CO3_show, 2], "Mario": [self.button_MARIO_show, 3],"Pac Man": [self.button_PAC_show, 4]} 
        
    def Begin(self):
        self.Button_Main.grid_forget()        
        self.Main_BG.grid_forget()
        self.Load_account()
        
    def Load_account(self):    
        self.BG = tk.Label(self.core, bg = "black")
        self.BG.grid(row=0, column=0, columnspan = 8, rowspan = 16, sticky="nsew")          
        
        self.Label_nome_1 = tk.Label(self.core,text="Login:", font = "Helvetica", fg = "green2", bg = "black")        
        self.Label_nome_1.grid(row=0, column=0, columnspan = 8, rowspan = 2, sticky = "nsew")       
        
        self.Textbox_1 = tk.Entry(self.core)
        self.Textbox_1.configure(textvariable=self.Login,font = "Helvetica 20")
        self.Textbox_1.grid(row=2, column=1, columnspan = 5, sticky="ew", padx =100)     
        
        self.Label_nome_2 = tk.Label(self.core,text="Senha:", font = "Helvetica", fg = "green2", bg = "black")        
        self.Label_nome_2.grid(row=5, column=0, columnspan = 8, rowspan = 2, sticky = "nsew")

        self.Textbox_2 = tk.Entry(self.core)
        self.Textbox_2.configure(textvariable=self.Senha, font = "Helvetica 20", show='*')
        self.Textbox_2.grid(row=7, column=1, columnspan = 5, sticky="ew", padx = 100)            

        self.Login_button = tk.Button(self.core,text="Entrar", fg = "green2", bg = "black", height = 3, command = self.Login_command)              
        self.Login_button.grid(row=13, column=1, columnspan = 5, padx = 100, sticky = "ew")    
        
        self.Sign_in_button = tk.Button(self.core,text="Cadastro", fg = "green2", bg = "black", height = 3, command = self.Cadastro_label)              
        self.Sign_in_button.grid(row=14, column=1, columnspan = 5, padx = 100, sticky = "ew")    

        self.Label_error = tk.Label(self.core,text="O Login não existe, cadastre-se para acessá-lo", font = "Helvetica", fg = "green2", bg = "black")        
        
    def Login_command(self):       
        self.Login_var_temp = self.Login.get()
        self.Senha_var_temp = self.Senha.get()
        self.database = open("cadastros.data", "rb")
        self.meus_cadastros = pickle.load(self.database)
        self.database.close()
        if self.Login_var_temp in self.meus_cadastros:
            if self.meus_cadastros.get(self.Login_var_temp)["senha"] == self.Senha_var_temp:
                self.Login_show.set(self.Login_var_temp)       
                self.loading_screen()
            else:
                self.Label_error.configure(text="A senha foi digitada incorretamente")                
                self.Label_error.grid(row=10, column=0, columnspan =8, rowspan = 2, sticky = "nsew")
        else:
            self.Label_error.configure(text="O Login não existe, cadastre-se para acessá-lo")               
            self.Label_error.grid(row=10, column=0, columnspan =8, rowspan = 2, sticky = "nsew")
            
    def Cadastro_label(self):         
        self.Login_button.configure(text = "Voltar", command = self.Load_account)
        self.Sign_in_button.configure(text = "Finalizar o Cadastro", command = self.Cadastro)
        self.Label_nome_1.configure(text="Digite um nome de usuário:")
        self.Label_nome_2.configure(text= "Digite uma senha:")
        
    def Cadastro(self):
        self.Label_error.grid_forget()
        self.Login_var_temp = self.Login.get()
        self.Senha_var_temp = self.Senha.get()
        self.database = open("cadastros.data", "rb")
        self.meus_cadastros = pickle.load(self.database)
        self.database.close()
        if self.Login_var_temp in self.meus_cadastros:
            self.Label_error.configure(text="Este cadastro já está vinculado a uma conta")                
            self.Label_error.grid(row=10, column=0, columnspan =8, rowspan = 2, sticky = "nsew")
        elif self.Login_var_temp == "":
            if self.Senha_var_temp == "":
                self.Label_error.configure(text="Digite um nome de usuário e uma senha")           
                self.Label_error.grid(row=10, column=0, columnspan =8, rowspan = 2, sticky = "nsew")
            else:
                self.Label_error.configure(text="Digite um nome de usuário")           
                self.Label_error.grid(row=10, column=0, columnspan =8, rowspan = 2, sticky = "nsew")
        elif self.Senha_var_temp == "":
            self.Label_error.configure(text="Digite uma senha")           
            self.Label_error.grid(row=10, column=0, columnspan =8, rowspan = 2, sticky = "nsew")   
        else:
            self.Label_error.grid_forget()
            self.meus_cadastros[self.Login_var_temp] = {"senha": self.Senha_var_temp, "jogos" : []}
            self.database = open("cadastros.data", "wb")
            pickle.dump(self.meus_cadastros,self.database)
            print(self.meus_cadastros)        
            self.database.close()
            self.Load_account()
    
    def loading_screen(self):
        self.BG.grid_forget()        
        self.Label_nome_1.grid_forget()
        self.Label_nome_2.grid_forget()       
        self.Textbox_1.grid_forget()
        self.Textbox_2.grid_forget()
        self.Login_button.grid_forget()
        self.Sign_in_button.grid_forget()
        self.Label_error.grid_forget()
        self.hexagon = Image.open("Images/Loading_hex.png")  
        self.hexagon_load = ImageTk.PhotoImage(self.hexagon)
        self.Hex_l = tk.Label(self.core, image = self.hexagon_load)
        self.Hex_l.configure(bg = "black")
        self.Hex_l.grid(row=0, column=0, columnspan=8, rowspan = 16 ,sticky="nsew")
        self.angle = 0 
        self.core.after(150, self.rotate1, self.angle)

    def rotate1(self, angle):      
        self.angle += 60    
        self.new_hex = ImageTk.PhotoImage(self.hexagon.rotate(self.angle))
        self.Hex_l.configure(image = self.new_hex)
        self.Hex_l.grid(row=0, column=0, columnspan=8, rowspan = 16 ,sticky="nsew")
        self.core.update()
        self.count = 0
        self.core.after(150, self.rotate2,self.angle,self.new_hex, self.count)
    
    def rotate2(self, angle, new_hex, count):      
        self.count += 1        
        self.angle += 60    
        self.new_hex = ImageTk.PhotoImage(self.hexagon.rotate(self.angle))
        self.Hex_l.configure(image = self.new_hex)
        self.Hex_l.grid(row=0, column=0, columnspan=8, rowspan = 16 ,sticky="nsew")
        if self.count < 10:         
            self.core.after(100, self.rotate2, self.angle,self.new_hex,self.count)
        elif self.count == 10:
            self.main_screen()
            
    def main_screen(self):
        
        self.Hex_l.destroy()
        
        self.BG = tk.Label(self.core, bg = "black", image = self.Main_Menu)
        self.BG.grid(row=0, column=0, columnspan = 8, rowspan = 16, sticky="nsew")   

        self.avatar = tk.Label(self.core, bg = "black", image = self.avatar_im_show, height = 50, width = 50)  
        self.avatar.place(x = 27, y = 28)        

        self.name_login = tk.Label(self.core, fg = "green2", bg = "black", textvariable = self.Login_show, width = 9)  
        self.name_login.place(x = 57, y = 98)             
        
        self.My_Favor = tk.Button(self.core, bg = "black", fg = "green2" , text= "Meus Favoritos", width = 12, command = self.my_fav)              
        self.My_Favor.place(x = 50, y = 150)   
        
        self.GTA = tk.Button(self.core, bg = "black", image = self.button_Gta_show , height = 150, width = 150, command = lambda n=1: self.access_games(n))              
        self.GTA.grid(row=9, column=5)    
        
        self.COD = tk.Button(self.core, bg = "black", image = self.button_CO3_show , height = 150, width = 150, command = lambda n=2: self.access_games(n))              
        self.COD.grid(row=12, column=5)
       
        self.MARIO = tk.Button(self.core, bg = "black", image = self.button_MARIO_show , height = 150, width = 150, command = lambda n=3: self.access_games(n))              
        self.MARIO.grid(row=9, column=6)                
       
        self.PAC = tk.Button(self.core, bg = "black", image = self.button_PAC_show , height = 150, width = 150, command = lambda n=4: self.access_games(n))              
        self.PAC.grid(row=12, column=6) 
    
    
    def my_fav(self):
        self.BG.configure(image = self.My_Fav) 
        self.MARIO.grid_forget()
        self.PAC.grid_forget()
        self.GTA.grid_forget()
        self.COD.grid_forget()
        self.Menu_Principal = tk.Button(self.core, bg = "black", fg = "green2" , text= "Menu Principal", width = 12, command = self.main_screen)              
        self.Menu_Principal.place(x = 50, y = 180)   
        self.n_games = len(self.meus_cadastros[self.Login_var_temp]["jogos"])
        for i in range(self.n_games):                
            self.games_var = self.lista_games[self.meus_cadastros[self.Login_var_temp]["jogos"][i]]             
            self.image_var = self.games_var[0]
            self.game_number = self.games_var[1]                
            self.button = "{0}".format(i)
            self.n = i
            self.button = tk.Button(self.core, bg = "black", height = 100, width = 100 ,image = self.image_var, command = lambda n = self.game_number: self.access_games(n)).place(x = i*140 + 225 - (self.n//3)*420 , y = (self.n//3)*120 + 200)             
                     
        
    def favorite_new(self, game_id):
        if game_id == 1:
            self.meus_cadastros[self.Login_var_temp]["jogos"].append("GTA")
            self.database = open("cadastros.data", "wb")
            pickle.dump(self.meus_cadastros,self.database)
            print(self.meus_cadastros)        
            self.database.close()
            self.FAV = tk.Button(self.core, bg = "black", image = self.fav , height = 50, width = 50, command = lambda n=1: self.des_favorite(n))              
            self.FAV.place(x = 50, y = 390) 
            
        if game_id == 2:
            self.meus_cadastros[self.Login_var_temp]["jogos"].append("COD")
            self.database = open("cadastros.data", "wb")
            pickle.dump(self.meus_cadastros,self.database)
            print(self.meus_cadastros)        
            self.database.close()
            self.FAV = tk.Button(self.core, bg = "black", image = self.fav , height = 50, width = 50, command = lambda n=2: self.des_favorite(n))              
            self.FAV.place(x = 50, y = 390)                 
            
        if game_id == 3:
            self.meus_cadastros[self.Login_var_temp]["jogos"].append("Mario")
            self.database = open("cadastros.data", "wb")
            pickle.dump(self.meus_cadastros,self.database)
            print(self.meus_cadastros)        
            self.database.close()
            self.FAV = tk.Button(self.core, bg = "black", image = self.fav , height = 50, width = 50, command = lambda n=3: self.des_favorite(n))              
            self.FAV.place(x = 50, y = 390)    
            
            
        if game_id == 4:
            self.meus_cadastros[self.Login_var_temp]["jogos"].append("Pac Man")
            self.database = open("cadastros.data", "wb")
            pickle.dump(self.meus_cadastros,self.database)
            print(self.meus_cadastros)        
            self.database.close()
            self.FAV = tk.Button(self.core, bg = "black", image = self.fav , height = 50, width = 50, command = lambda n=4: self.des_favorite(n))              
            self.FAV.place(x = 50, y = 390)              
    
    def des_favorite(self, numero):
        
        if numero == 1:
            self.meus_cadastros[self.Login_var_temp]["jogos"].remove("GTA")
            self.database = open("cadastros.data", "wb")
            pickle.dump(self.meus_cadastros,self.database)
            print(self.meus_cadastros)        
            self.database.close()
            self.FAV = tk.Button(self.core, bg = "black", image = self.not_fav , height = 50, width = 50, command = lambda n=1: self.favorite_new(n))              
            self.FAV.place(x = 50, y = 390) 
            
        if numero == 2:
            self.meus_cadastros[self.Login_var_temp]["jogos"].remove("COD")
            self.database = open("cadastros.data", "wb")
            pickle.dump(self.meus_cadastros,self.database)
            print(self.meus_cadastros)        
            self.database.close()
            self.FAV = tk.Button(self.core, bg = "black", image = self.not_fav, height = 50, width = 50, command = lambda n=2: self.favorite_new(n))              
            self.FAV.place(x = 50, y = 390)               
            
        if numero == 3:
            self.meus_cadastros[self.Login_var_temp]["jogos"].remove("Mario")
            self.database = open("cadastros.data", "wb")
            pickle.dump(self.meus_cadastros,self.database)
            print(self.meus_cadastros)        
            self.database.close()
            self.FAV = tk.Button(self.core, bg = "black", image = self.not_fav , height = 50, width = 50, command = lambda n=3: self.favorite_new(n))              
            self.FAV.place(x = 50, y = 390)      
            
        if numero == 4:
            self.meus_cadastros[self.Login_var_temp]["jogos"].remove("Pac Man")
            self.database = open("cadastros.data", "wb")
            pickle.dump(self.meus_cadastros,self.database)
            print(self.meus_cadastros)        
            self.database.close()
            self.FAV = tk.Button(self.core, bg = "black", image = self.not_fav , height = 50, width = 50, command = lambda n=4: self.favorite_new(n))              
            self.FAV.place(x = 50, y = 390) 
        
    def access_games(self, numero): 
        self.GTA.grid_forget()
        self.COD.grid_forget()
        self.PAC.grid_forget()
        self.MARIO.grid_forget()
        self.BG = tk.Label(self.core, bg = "black")
        self.BG.grid(row=0, column=0, columnspan = 8, rowspan = 16, sticky="nsew") 
        
        if numero == 1:
              
            self.poster = tk.Label(self.core, bg = "black", image = self.poster_Gta_show)  
            self.poster.place(x = 25, y = 20)

            self.preco_l = tk.Label(self.core, bg = "black", fg = "green2", text = "Melhor preço:" , height = 3, width = 11)  
            self.preco_l.place(x = 255, y = 400)           
            
            self.preco = tk.Label(self.core, bg = "black", fg = "green2", text = "R$95,00" , height = 3, width = 8)  
            self.preco.place(x = 340, y = 400)
        
            self.Melhor_preço = tk.Button(self.core, bg = "black", image = self.UZ , height = 50, width = 150, command = lambda n=1: self.site(n))
            self.Melhor_preço.place(x = 470, y = 400)        
            
            self.descrição_l = tk.Label(self.core, bg = "black", fg = "green2", text = "Descrição:" , height = 3)  
            self.descrição_l.place(x = 305, y = 520)            
            
            self.descrição = tk.Label(self.core, bg = "black", fg = "green2", text = "Jogo de um maniaco que mata todo mundo" , height = 3)  
            self.descrição.place(x = 215, y = 560)
             
            self.Return = tk.Button(self.core, bg = "black", fg = "green2", text = "Voltar" , height = 2, width = 8, command = self.forget_game)
            self.Return.place(x = 300, y = 620) 

            if "GTA" in self.meus_cadastros[self.Login_var_temp]["jogos"]:
                self.FAV = tk.Button(self.core, bg = "black", image = self.fav , height = 50, width = 50, command = lambda n=1: self.des_favorite(n))              
                self.FAV.place(x = 50, y = 390)            
            else:
                self.FAV = tk.Button(self.core, bg = "black", image = self.not_fav , height = 50, width = 50, command = lambda n=1: self.favorite_new(n))              
                self.FAV.place(x = 50, y = 390)                
            
        elif numero == 2:
            
            self.poster = tk.Label(self.core, bg = "black", image = self.poster_CO3_show)  
            self.poster.place(x = 25, y = 20)
           
            self.preco_l = tk.Label(self.core, bg = "black", fg = "green2", text = "Melhor preço:" , height = 3, width = 11)  
            self.preco_l.place(x = 255, y = 400)        
            
            self.preco = tk.Label(self.core, bg = "black", fg = "green2", text = "R$79,00" , height = 3, width = 8)  
            self.preco.place(x = 340, y = 400)
        
            self.Melhor_preço = tk.Button(self.core, bg = "black", image = self.UZ , height = 50, width= 150, command = lambda n=2: self.site(n))  
            self.Melhor_preço.place(x = 470, y = 400)         
        
            self.descrição_l = tk.Label(self.core, bg = "black", fg = "green2", text = "Descrição:" , height = 3)  
            self.descrição_l.place(x = 305, y = 520)       
        
            self.descrição = tk.Label(self.core, bg = "black", fg = "green2", text = "Jogo no qual vc pode atirar em outros usuarios online" , height = 3)  
            self.descrição.place(x = 215, y = 560) 
            
            self.Return = tk.Button(self.core, bg = "black", fg = "green2", text = "Voltar" , height = 2, width = 8, command = self.forget_game)
            self.Return.place(x = 300, y = 620) 
            
            if "COD" in self.meus_cadastros[self.Login_var_temp]["jogos"]:
                self.FAV = tk.Button(self.core, bg = "black", image = self.fav , height = 50, width = 50, command = lambda n=2: self.des_favorite(n))              
                self.FAV.place(x = 50, y = 390)            
            else:
                self.FAV = tk.Button(self.core, bg = "black", image = self.not_fav , height = 50, width = 50, command = lambda n=2: self.favorite_new(n))              
                self.FAV.place(x = 50, y = 390)     
        
        elif numero == 3:
            self.poster = tk.Label(self.core, bg = "black", image = self.poster_MARIO_show)  
            self.poster.place(x = 25, y = 20)
          
            self.preco_l = tk.Label(self.core, bg = "black", fg = "green2", text = "Melhor preço:" , height = 3, width = 11)      
            self.preco_l.place(x = 255, y = 400) 
            
            self.preco = tk.Label(self.core, bg = "black", fg = "green2", text = "R$35,50" , height = 3, width = 8)  
            self.preco.place(x = 340, y = 400)
        
            self.Melhor_preço = tk.Button(self.core, bg = "black", image = self.UZ , height = 50, width = 150, command = lambda n=3: self.site(n))  
            self.Melhor_preço.place(x = 470, y = 400)         
        
            self.descrição_l = tk.Label(self.core, bg = "black", fg = "green2", text = "Descrição:" , height = 3)  
            self.descrição_l.place(x = 305, y = 520)         
            
            self.descrição = tk.Label(self.core, bg = "black", fg = "green2", text = "Jogo de um encanador psicodelico" , height = 3)  
            self.descrição.place(x = 235, y = 560)         
            
            self.Return = tk.Button(self.core, bg = "black", fg = "green2", text = "Voltar" , height = 2, width = 8, command = self.forget_game)
            self.Return.place(x = 300, y = 620)  
        
            if "Mario" in self.meus_cadastros[self.Login_var_temp]["jogos"]:
                self.FAV = tk.Button(self.core, bg = "black", image = self.fav , height = 50, width = 50, command = lambda n=3: self.des_favorite(n))              
                self.FAV.place(x = 50, y = 390)             
            else:
                self.FAV = tk.Button(self.core, bg = "black", image = self.not_fav , height = 50, width = 50, command = lambda n=3: self.favorite_new(n))              
                self.FAV.place(x = 50, y = 390)    
                
        elif numero == 4:
            self.poster = tk.Label(self.core, bg = "black", image = self.poster_PAC_show)  
            self.poster.place(x = 25, y = 20)
            
            self.preco_l = tk.Label(self.core, bg = "black", fg = "green2", text = "Melhor preço:" , height = 3, width = 11)  
            self.preco_l.place(x = 255, y = 400) 
          
            self.preco = tk.Label(self.core, bg = "black", fg = "green2", text = "R$3,67" , height = 3, width = 8)  
            self.preco.place(x = 340, y = 400)
        
            self.Melhor_preço = tk.Button(self.core, bg = "black", image = self.UZ , height = 50, width = 150, command = lambda n=4: self.site(n))  
            self.Melhor_preço.place(x = 470, y = 400) 
            
            self.descrição_l = tk.Label(self.core, bg = "black", fg = "green2", text = "Descrição:" , height = 3)  
            self.descrição_l.place(x = 305, y = 520)
        
            self.descrição = tk.Label(self.core, bg = "black", fg = "green2", text = "\
            Bolinha amarela que fica numa sala escura e quando come um doce tem poderes para comer fantasmas" , height = 3)  
            self.descrição.place(x = 30, y = 560) 

            self.Return = tk.Button(self.core, bg = "black", fg = "green2", text = "Voltar" , height = 2, width = 8, command = self.forget_game)
            self.Return.place(x = 300, y = 620) 
    
            if "Pac Man" in self.meus_cadastros[self.Login_var_temp]["jogos"]:
                self.FAV = tk.Button(self.core, bg = "black", image = self.fav , height = 50, width = 50, command = lambda n=4: self.des_favorite(n))              
                self.FAV.place(x = 50, y = 390)          
            else:
                self.FAV = tk.Button(self.core, bg = "black", image = self.not_fav , height = 50, width = 50, command = lambda n=4: self.favorite_new(n))              
                self.FAV.place(x = 50, y = 390) 
                
    def forget_game(self):
        self.poster.grid_forget()               
        self.Melhor_preço.grid_forget()
        self.preco_l.grid_forget()
        self.preco.grid_forget()
        self.descrição.grid_forget()
        self.descrição_l.grid_forget()
        self.Return.grid_forget()
        self.main_screen()
        
    def site(self, numero):
        if numero == 1:
            webbrowser.open("http://www.uzgames.com.br/gta?&utmi_p=_games&utmi_pc=BuscaFullText&utmi_cp=gta")
        elif numero == 2:
            webbrowser.open("http://www.uzgames.com.br/call%20of%20duty%20ghosts?&utmi_p=_call+of+duty+gosth&utmi_pc=BuscaFullText&utmi_cp=call%20of%20duty%20ghosts")
        elif numero == 3:
            webbrowser.open("http://www.uzgames.com.br/mario%20bros?&utmi_p=_gta&utmi_pc=BuscaFullText&utmi_cp=mario%20bros")
        elif numero == 4:
            webbrowser.open("http://www.uzgames.com.br/pac%20man?&utmi_p=_gta&utmi_pc=BuscaFullText&utmi_cp=pac%20man")
    def loop(self):
        self.core.mainloop()

Main = Main_Window()
Main.loop()       
