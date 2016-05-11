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
        self.Login = tk.StringVar()
        self.Senha = tk.StringVar()
        for linhas in range (0,15):
           self.core.rowconfigure(linhas, weight=1)
        for colunas in range (0,8):        
           self.core.columnconfigure(colunas, weight=1)
        self.Main_BG = tk.Label(self.core, image = self.init2)
        self.Main_BG.configure(bg = "black")      
        self.Main_BG.grid(row=0, column=0, columnspan=8, rowspan = 15 ,sticky="nsew") 
        self.Button_Main = tk.Button(self.core,image=self.init, bg = "black", width = 170, height = 120,command = self.Begin)
        self.Button_Main.grid(row=0, column=0, columnspan=1, rowspan= 1, pady = 220, padx = 259)        

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
        self.Textbox_2.configure(textvariable=self.Senha, font = "Helvetica 20")
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
            if self.meus_cadastros.get(self.Login_var_temp) == self.Senha_var_temp:
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
        elif self.meus_cadastros.get(self.Login_var_temp) == self.Senha_var_temp:
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
            self.meus_cadastros[self.Login_var_temp] = self.Senha_var_temp
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
        self.hexagon = Image.open("Loading/Loading_hex.png")  
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
        if self.count == 0:
            self.core.after(2000, self.main_screen)
            self.count = 1        
        self.angle += 60    
        self.new_hex = ImageTk.PhotoImage(self.hexagon.rotate(self.angle))
        self.Hex_l.configure(image = self.new_hex)
        self.Hex_l.grid(row=0, column=0, columnspan=8, rowspan = 16 ,sticky="nsew")
        self.core.after(100, self.rotate2, self.angle,self.new_hex,self.count)
        
    def main_screen(self):
        self.Hex_l.destroy()
        self.GTA_im = Image.open("Images/GTA.jpg")     
        self.Gta_show = ImageTk.PhotoImage(self.GTA_im)
        
        self.uz_im = Image.open("Images/uz-games.jpg")
        self.UZ = ImageTk.PhotoImage(self.uz_im)
        
        self.BG = tk.Label(self.core, bg = "black")
        self.BG.grid(row=0, column=0, columnspan = 8, rowspan = 16, sticky="nsew")                  
        
        self.GTA = tk.Button(self.core, bg = "black", image = self.Gta_show , height = 3, command = self.access_games)              
        self.GTA.grid(row=3, column=1, columnspan = 5, rowspan = 8, sticky = "nsew")    
        
    def access_games(self):
        self.GTA.grid_forget()
        self.GTA_poster = tk.Label(self.core, bg = "black", image = self.Gta_show , height = 3)  
        self.GTA_poster.grid(row=0, column=1, columnspan = 5, rowspan = 8, sticky = "nsew")
          
        self.preco = tk.Label(self.core, bg = "black", fg = "green2", text = "Preço: R$95,00" , height = 3)  
        self.preco.grid(row=10, column=1, columnspan = 2, rowspan = 2, sticky = "nsew")
        
        self.Melhor_preço = tk.Button(self.core, bg = "black", image = self.UZ , height = 3, command = self.site)  
        self.Melhor_preço.grid(row=10, column=5, columnspan = 2, rowspan = 2, sticky = "nsew")        
        
        self.descrição = tk.Label(self.core, bg = "black", fg = "green2", text = "Jogo de um maniaco que mata todo mundo" , height = 3)  
        self.descrição.grid(row=13, column=1, columnspan = 5, rowspan = 2, sticky = "nsew")
                                     
    def site(self):
        webbrowser.open("http://www.uzgames.com.br/gta?&utmi_p=_games&utmi_pc=BuscaFullText&utmi_cp=gta")


    
    def loop(self):
        self.core.mainloop()

Main = Main_Window()
Main.loop()       