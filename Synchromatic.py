# -*- coding: utf-8 -*-

"""
Created on Fri Apr 29 14:13:19 2016

@author: Gabriel
"""

import tkinter as tk
import pickle
import webbrowser
import Email_Generator
import banco_de_dados
import Pesquisa
from PIL import Image, ImageTk
import random
import string

class Main_Window:
    
    def __init__(self):
        
        self.core = tk.Tk()            
        self.core.resizable(height = False, width=False)
        self.core.title("Synchromatic")
        self.core.geometry("650x670")
        
        self.Email_gen = Email_Generator.create_email()
        
        self.image1 = Image.open("Images/Main_Button.jpg")     
        self.init = ImageTk.PhotoImage(self.image1)
        self.image2 = Image.open("Images/syn.jpg")     
        self.init2 = ImageTk.PhotoImage(self.image2)
        
        self.Main_Menu_im = Image.open("Images/Main_Menu.png")  
        self.Main_Menu = ImageTk.PhotoImage(self.Main_Menu_im) 

        self.My_Fav_im = Image.open("Images/Meus_Favoritos.png")  
        self.My_Fav = ImageTk.PhotoImage(self.My_Fav_im) 
        
        self.minha_conta_im = Image.open("Images/Minha_conta.png")
        self.minha_conta = ImageTk.PhotoImage(self.minha_conta_im)
        
        self.Pesquisa_im = Image.open("Images/Pesquisa.png")
        self.Pesquisa_show = ImageTk.PhotoImage(self.Pesquisa_im)

        self.bg_pages_im = Image.open("Images/Pagina_jogos.png")     
        self.bg_pages_show = ImageTk.PhotoImage(self.bg_pages_im)
        
        self.avatar_im = Image.open("Images/Login_avatar.jpg")     
        self.avatar_im_show = ImageTk.PhotoImage(self.avatar_im)
        
        self.default_im = Image.open("Images/defaultavatar.jpg")     
        self.default = ImageTk.PhotoImage(self.default_im)
 
        self.fav_im = Image.open("Images/Favorite.png")
        self.fav = ImageTk.PhotoImage(self.fav_im)
        
        self.not_fav_im = Image.open("Images/Not_Favorite.jpg")
        self.not_fav = ImageTk.PhotoImage(self.not_fav_im)  
        
        self.alterar_im = Image.open("Images/alterar.jpg")
        self.alterar = ImageTk.PhotoImage(self.alterar_im)  
        
        self.alterar_senha_im = Image.open("Images/alterar_senha.png")
        self.alterar_senha_image = ImageTk.PhotoImage(self.alterar_senha_im)  
        
        self.salvar_alt_im = Image.open("Images/salvar_alt.png")
        self.salvar_alt = ImageTk.PhotoImage(self.salvar_alt_im)  
        
        self.discartar_im = Image.open("Images/disc_alt.png")
        self.discartar_alt = ImageTk.PhotoImage(self.discartar_im) 
        
        self.avatar_0_im = Image.open("Images/Darth.jpeg")
        self.avatar_0 = ImageTk.PhotoImage(self.avatar_0_im)         
        
        self.avatar_1_im = Image.open("Images/Kirby_hat.png")
        self.avatar_1 = ImageTk.PhotoImage(self.avatar_1_im) 
        
        self.avatar_2_im = Image.open("Images/Eric.png")
        self.avatar_2 = ImageTk.PhotoImage(self.avatar_2_im) 
        
        self.avatar_3_im = Image.open("Images/Homer.png")
        self.avatar_3 = ImageTk.PhotoImage(self.avatar_3_im) 
        
        self.avatar_4_im = Image.open("Images/Yoda.png")
        self.avatar_4 = ImageTk.PhotoImage(self.avatar_4_im) 
        
        self.avatar_sel_im = Image.open("Images/Avatar_select.png")
        self.avatar_sel = ImageTk.PhotoImage(self.avatar_sel_im)
        
        self.left_im = Image.open("Images/Button_left.png")
        self.left = ImageTk.PhotoImage(self.left_im) 
        
        self.right_im = Image.open("Images/Button_right.png")
        self.right = ImageTk.PhotoImage(self.right_im) 
        
        self.Jogos_canvas = Image.open("Images/Pagina_canvas.png")
        self.jogos_canvas = ImageTk.PhotoImage(self.Jogos_canvas) 

        self.all_games = banco_de_dados.Games()        
        
        self.var = 0        
        
        self.game_entry = tk.StringVar()  
        self.game_entry.set("Procure jogos aqui")
        
        self.username = tk.StringVar()        
        self.Login = tk.StringVar()
        self.Senha = tk.StringVar()
        self.email = tk.StringVar()
        self.Login_show = tk.StringVar()
        self.Login_my_acc = tk.StringVar()
        self.email_show = tk.StringVar()
        self.user_my_acc = tk.StringVar()
        self.Senha_conf = tk.StringVar()
        
        self.avatar_var = [self.avatar_0, self.avatar_1, self.avatar_2, self.avatar_3, self.avatar_4]        
        
        for linhas in range (0,15):
           self.core.rowconfigure(linhas, weight=1)
        for colunas in range (0,8):        
           self.core.columnconfigure(colunas, weight=1)
        self.Main_BG = tk.Label(self.core, image = self.init2)
        self.Main_BG.configure(bg = "black")      
        self.Main_BG.grid(row=0, column=0, columnspan=8, rowspan = 15 ,sticky="nsew") 
        self.Button_Main = tk.Button(self.core,image=self.init, bg = "black", width = 130, height = 120,command = self.Begin)
        self.Button_Main.place(x = 256, y = 230) 
        self.database = open("cadastros.data", "rb")
        self.meus_cadastros = pickle.load(self.database)
        self.database.close()
                
    def Begin(self):
        self.Button_Main.grid_forget()        
        self.Main_BG.grid_forget()
        self.Login_screen()
        
    def Login_screen(self):
 
        self.BG = tk.Label(self.core, bg = "black")
        self.BG.grid(row=0, column=0, columnspan = 8, rowspan = 16, sticky="nsew")          
        
        self.Login_button = tk.Button(self.core,text="Login", fg = "green2", bg = "black", height = 3, width = 19, command = self.Load_account)              
        self.Login_button.place(x = 250, y = 300)       
        
        self.Sign_in_button = tk.Button(self.core,text="Cadastro", fg = "green2", bg = "black", height = 3, width = 19, command = self.Cadastro_label)              
        self.Sign_in_button.place(x = 250, y = 380)   
        
    def Load_account(self):   
        
        self.var = 1       
        
        self.Login_button.grid_forget()
        self.Sign_in_button.grid_forget()
        
        self.BG = tk.Label(self.core, bg = "black")
        self.BG.grid(row=0, column=0, columnspan = 8, rowspan = 16, sticky="nsew")          
        
        self.Label_nome_1 = tk.Label(self.core,text="Login:", font = "Helvetica", fg = "green2", bg = "black", height = 3, width = 4)        
        self.Label_nome_1.place(x = 110, y = 132)      
        
        self.Textbox_1 = tk.Entry(self.core, textvariable=self.Login,font = "Helvetica 20")
        self.Textbox_1.place(x = 200, y = 150)   
        
        self.Label_nome_2 = tk.Label(self.core,text="Senha:", font = "Helvetica", fg = "green2", bg = "black", height = 3, width = 5)        
        self.Label_nome_2.place(x = 110, y = 232)           
        
        self.Textbox_2 = tk.Entry(self.core, textvariable=self.Senha, font = "Helvetica 20", show='*')
        self.Textbox_2.place(x = 200, y= 250)            

        self.Login_button = tk.Button(self.core,text="Entrar", fg = "green2", bg = "black", height = 3, width = 19, command = self.Login_command)              
        self.Login_button.place(x = 250, y = 500)
        
        self.esqueci_button = tk.Button(self.core,text="Esqueci minha senha", fg = "green2", bg = "black", height = 3, width = 19, command = self.Esqueci_minha_senha)              
        self.esqueci_button.place(x = 340, y = 580)  
        
        self.Voltar_button = tk.Button(self.core,text="Voltar", fg = "green2", bg = "black", height = 3, width = 19, command = lambda n=100: self.erase_labels(n))              
        self.Voltar_button.place(x = 160, y = 580)   

        self.Label_error = tk.Label(self.core, font = "Helvetica", fg = "green2", bg = "black")        
        self.Label_error.place(x = 100, y = 430)        
    
    def Esqueci_minha_senha(self):
        
        self.Textbox_1.place_forget()
        self.Label_nome_1.place_forget()
        self.esqueci_button.place_forget()
        self.Voltar_button.place_forget()
        self.Label_error.place_forget()
        self.email.set("")
        self.Label_nome_2.configure(text="Digite o seu email no campo abaixo para receber um email com a sua nova senha", font = "Helvetica 8", width = 20)        
        self.Label_nome_2.place(x = 300, y = 132)
        self.Textbox_2.configure(textvariable=self.email, font = "Helvetica 20", show = "")
        self.Textbox_2.place(x = 200, y= 250)       
        self.Login_button.configure(text="Mandar email", height = 3, width = 19, command = self.Checar_email)              
        self.Login_button.place(x = 250, y = 500)
    
    def Checar_email(self):
      
       for pessoas in self.meus_cadastros:
               if self.meus_cadastros[pessoas]["email"] == self.email.get():
                   first = str(random.randint(0,9))
                   second = random.choice(string.ascii_letters)
                   third = str(random.randint(0,9))
                   fourth =  random.choice(string.ascii_letters)
                   fifth = str(random.randint(0,9))
                   sixth = str(random.randint(0,9))
                   seventh = str(random.randint(0,9))
                   eighth =  random.choice(string.ascii_letters)
                   ninth =  random.choice(string.ascii_letters)
                   self.new_pass = first + second + third + fourth + fifth + sixth + seventh + eighth + ninth
                   self.Email_gen.reset_senha(self.email.get(), self.new_pass)
                   self.meus_cadastros[pessoas]["senha"] = self.new_pass
                   self.database = open("cadastros.data", "rb")
                   self.meus_cadastros = pickle.load(self.database)
                   self.database.close()
                   self.Load_account()
       self.Label_error.configure(text="Esse email não está vinculado a uma conta.")                
       self.Label_error.place(x = 100, y = 430)       
        
    def Login_command(self):       
                  
        self.Login_var_temp = self.Login.get()
        self.Senha_var_temp = self.Senha.get()
        if self.Login_var_temp in self.meus_cadastros:
            if self.meus_cadastros.get(self.Login_var_temp)["senha"] == self.Senha_var_temp:
                self.Usuario_var_temp = self.meus_cadastros[self.Login_var_temp]["username"]         
                self.Email_var_temp = self.meus_cadastros[self.Login_var_temp]["email"]  
                self.Login_show.set(self.Usuario_var_temp)       
                self.user_my_acc.set(self.Usuario_var_temp)
                self.Senha_t = self.Senha_var_temp
                self.var = 3
                self.oferta_list = []
                while len(self.oferta_list) < 9:                 
                    self.oferta_n = random.randint(1,9)
                    if not self.oferta_n in self.oferta_list:
                        self.oferta_list.append(self.oferta_n)
                self.erase_labels(100)
            else:
                self.Label_error.configure(text="A senha foi digitada incorretamente")                
                self.Label_error.place(x = 100, y = 430)
        else:
            self.Label_error.configure(text="O Login não existe, cadastre-se para acessá-lo")               
            self.Label_error.place(x = 100, y = 430)
    
    def Cadastro_label(self):         
 
        self.var = 2       
 
        self.BG = tk.Label(self.core, bg = "black")
        self.BG.grid(row=0, column=0, columnspan = 8, rowspan = 16, sticky="nsew")          
        
        self.Label_nome_1 = tk.Label(self.core,text="Login:", font = "Helvetica", fg = "green2", bg = "black", height = 3, width = 4)        
        self.Label_nome_1.place(x = 110, y = 202)     
        
        self.Textbox_1 = tk.Entry(self.core, textvariable=self.Login,font = "Helvetica 20")
        self.Textbox_1.place(x = 200, y = 220)   
        
        self.Label_nome_2 = tk.Label(self.core,text="Senha:", font = "Helvetica", fg = "green2", bg = "black", height = 3, width = 5)        
        self.Label_nome_2.place(x = 110, y = 342)         
        
        self.Textbox_2 = tk.Entry(self.core, textvariable=self.Senha, font = "Helvetica 20", show='*')
        self.Textbox_2.place(x = 200, y= 360)            

        self.Login_button = tk.Button(self.core,text="Finalizar o Cadastro", fg = "green2", bg = "black", height = 3, width = 19, command = self.Cadastro)              
        self.Login_button.place(x = 250, y = 500)
        
        self.Voltar_button = tk.Button(self.core,text="Voltar", fg = "green2", bg = "black", height = 3, width = 19, command = lambda n=100: self.erase_labels(n))              
        self.Voltar_button.place(x = 250, y = 580)

        self.Label_error = tk.Label(self.core,text="O Login não existe, cadastre-se para acessá-lo", font = "Helvetica", fg = "green2", bg = "black")                
        
        self.user_label = tk.Label(self.core,text="Usuário:", font = "Helvetica", fg = "green2", bg = "black", height = 3, width = 6)        
        self.user_label.place(x = 100, y = 132)        
        
        self.userTextbox = tk.Entry(self.core, textvariable=self.username, font = "Helvetica 20")
        self.userTextbox.place(x = 200, y = 150)
        
        self.email_label = tk.Label(self.core,text="E-mail:", font = "Helvetica", fg = "green2", bg = "black", height = 3, width = 5)        
        self.email_label.place(x = 110, y = 272)  
        self.emailTextbox = tk.Entry(self.core, textvariable=self.email, font = "Helvetica 20")
        self.emailTextbox.place(x = 200, y = 290)         

        
    def Cadastro(self):
        self.Label_error.grid_forget()
        self.Login_var_temp = self.Login.get()
        self.Senha_var_temp = self.Senha.get()
        self.Email_var_temp = self.email.get()
        self.Usuario_var_temp = self.username.get()
        self.database = open("cadastros.data", "rb")
        self.meus_cadastros = pickle.load(self.database)
        self.database.close()
        if self.Login_var_temp in self.meus_cadastros:
            self.Label_error.configure(text="Este cadastro já está vinculado a uma conta")                
            self.Label_error.place(x = 100, y = 430)

        elif self.Login_var_temp == "":
            if self.Senha_var_temp == "":
                self.Label_error.configure(text="Digite um nome de usuário e uma senha")           
                self.Label_error.place(x = 100, y = 430)
            else:
                self.Label_error.configure(text="Digite um nome de usuário")           
                self.Label_error.place(x = 100, y = 430)
        
        elif self.Usuario_var_temp == "":
            self.Label_error.configure(text="Digite um nome de Usuario")           
            self.Label_error.place(x = 100, y = 430) 

        elif self.Email_var_temp == "":
            self.Label_error.configure(text="Digite um endereço de email")           
            self.Label_error.place(x = 100, y = 430)   
        
        elif self.Senha_var_temp == "":
            self.Label_error.configure(text="Digite uma senha")           
            self.Label_error.place(x = 100, y = 430)       
            
        elif self.Email_var_temp in self.meus_cadastros:
            self.Label_error.configure(text="Este endereço de email já está vinculado a uma conta")                
            self.Label_error.place(x = 80, y = 430)
        
        else:
            self.Label_error.grid_forget()
            self.meus_cadastros[self.Login_var_temp] = {"senha": self.Senha_var_temp, "jogos" : [], "email": self.Email_var_temp, "username": self.Usuario_var_temp, "useravatar": "0"}
            self.database = open("cadastros.data", "wb")
            pickle.dump(self.meus_cadastros,self.database)
            print(self.meus_cadastros)        
            self.database.close()
            self.erase_labels(100)    
    
    def erase_labels(self,numero):
        
        if self.var == 1:
            self.BG.grid_forget()        
            self.Label_nome_1.grid_forget()
            self.Label_nome_2.grid_forget()       
            self.Textbox_1.grid_forget()
            self.Textbox_2.grid_forget()
            self.Login_button.grid_forget()
            self.Label_error.grid_forget()
            self.esqueci_button.grid_forget()
            self.Login_screen()  
            
        elif self.var == 2:
            self.BG.grid_forget()        
            self.Label_nome_1.grid_forget()
            self.Label_nome_2.grid_forget()       
            self.Textbox_1.grid_forget()
            self.Textbox_2.grid_forget()
            self.Login_button.grid_forget()
            self.Voltar_button.grid_forget()
            self.Label_error.grid_forget()
            self.user_label.grid_forget()
            self.userTextbox.grid_forget()
            self.email_label.grid_forget()
            self.emailTextbox.grid_forget()
            self.Login_screen() 
            
        elif self.var == 3:
             
            self.BG.grid_forget()        
            self.Label_nome_1.grid_forget()
            self.Label_nome_2.grid_forget()       
            self.Textbox_1.grid_forget()
            self.Textbox_2.grid_forget()
            self.Login_button.grid_forget()
            self.Sign_in_button.grid_forget()
            self.Label_error.grid_forget()
            self.loading_screen()
        
        elif self.var == 4:  
            
            for i in range(0,9):            
                self.gaming_list[i].place_forget()  
            self.Games_entry.place_forget()
            self.Pesqui_av.place_forget()   
                
        elif self.var == 5:  
            
            self.alterar_login.place_forget()
            self.alterar_email.place_forget()
            self.alterar_senha.place_forget()
            self.email_label.place_forget()
            self.user_label.place_forget()
            self.login_label.place_forget()
            self.alterar_usuario.place_forget()
            self.salvar_alterações.place_forget()
            self.discartar_alterações.place_forget()
            self.Login_my_acc.set(self.Login_var_temp)
            self.email_show.set(self.Email_var_temp)
            self.user_my_acc.set(self.Usuario_var_temp)
            
        elif self.var == 6:    
            
            self.n_games = len(self.meus_cadastros[self.Login_var_temp]["jogos"])
            for i in range(self.n_games):                                         
                self.favorite_list[i].place_forget()
            self.Games_entry.place_forget()
            self.Pesqui_av.place_forget()      
        
        elif self.var == 7:
            
            self.Canvas_master.delete("all")
            self.poster.place_forget()
            self.Melhor_preço.place_forget()
            self.FAV.place_forget()
            self.plataforma.place_forget()
        
        elif self.var == 8:

            for i in range(len(self.found_games)):            
                self.found_games[i].place_forget()  
            self.Games_entry.place_forget()
            self.Pesqui_av.place_forget() 
        
        if numero == 0:
            self.main_screen()
                
        elif numero == 1:
            self.my_conta()
            
        elif numero == 2:
            self.my_fav()       

        elif numero == 3:
            self.pesquisa_labels()
            
        elif numero == 4:
            self.Login_screen()
        
        elif numero >= 5:
            if numero < 100:    
                self.choose_game = numero - 4
                self.access_games(self.choose_game)          
            elif numero == 100:
                self.tick = 1
                
    def loading_screen(self):
        
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
        
        self.var = 4
        
        self.BG = tk.Label(self.core, bg = "black", image = self.Main_Menu)
        self.BG.grid(row=0, column=0, columnspan = 8, rowspan = 16, sticky="nsew")   

        self.main_buttons()        

        self.gaming_list = []
        
        for i in range(0,9):
            
            self.var_gaming = self.oferta_list[i]
            self.var_erasing = self.var_gaming + 4
            self.actual = self.all_games.games(self.var_gaming)
            self.var_str = "{0}".format(self.var_gaming)
            self.game_var = tk.Button(self.core, bg = "black", height = 100, width = 100 ,image = self.actual[self.var_str]["button"], command = lambda n = self.var_erasing: self.erase_labels(n))
            self.game_var.place(x = i*140 + 225 - (i//3)*420 , y = (i//3)*120 + 200)
            self.gaming_list.append(self.game_var)        
        
        #self.Pesqui_av= tk.Button(self.core, bg = "black",  fg = "green2", text = "Pesquisa Avançada" , height = 2, width = 56, command = lambda n=4: self.access_games(n))              
        #self.Pesqui_av.place(x = 219, y = 60) 
        
        self.Games_entry = tk.Entry(self.core, width = 30, bg = "black", fg= "green2", textvariable=self.game_entry ,font = "Helvetica 18")
        self.Games_entry.bind("<Return>", self.pesquisa)           
        self.Games_entry.place(x = 220, y = 19)               
    
    def pesquisa(self, event):        
        self.achar_jogos = Pesquisa.pesquisa()
        self.name_sliced = (self.game_entry.get()).split()
        self.achar_list = self.achar_jogos.find_game(self.name_sliced)
        self.erase_labels(3)
        
    def pesquisa_labels(self):
        
        self.var = 4
        
        self.BG = tk.Label(self.core, bg = "black", image = self.Pesquisa_show)
        self.BG.grid(row=0, column=0, columnspan = 8, rowspan = 16, sticky="nsew")   

        self.main_buttons()        
       
        self.found_games = []
       
        for i in range(len(self.achar_list)):
           
            self.var_gaming = int(self.achar_list[i])
            self.var_erasing = self.var_gaming + 4
            self.actual = self.all_games.games(self.var_gaming)
            self.var_str = self.achar_list[i]
            self.game_var = tk.Button(self.core, bg = "black", height = 100, width = 100 ,image = self.actual[self.var_str]["button"], command = lambda n = self.var_erasing: self.erase_labels(n))
            self.game_var.place(x = i*140 + 225 - (i//3)*420 , y = (i//3)*120 + 200)
            self.found_games.append(self.game_var)        
        
        #self.Pesqui_av= tk.Button(self.core, bg = "black",  fg = "green2", text = "Pesquisa Avançada" , height = 2, width = 56, command = lambda n=4: self.access_games(n))              
        #self.Pesqui_av.place(x = 219, y = 60) 
        
        self.Games_entry = tk.Entry(self.core, width = 30, bg = "black", fg= "green2", textvariable=self.game_entry ,font = "Helvetica 18")
        self.Games_entry.bind("<Return>", self.pesquisa)           
        self.Games_entry.place(x = 220, y = 19) 
    
    def my_conta(self):

        self.var = 5
        self.choice_ind = 0
        
        self.BG = tk.Label(self.core, bg = "black", image = self.minha_conta)
        self.BG.grid(row=0, column=0, columnspan = 8, rowspan = 16, sticky="nsew")          
        
        self.database = open("cadastros.data", "rb")
        self.meus_cadastros = pickle.load(self.database)
        self.database.close()
        self.email_show.set(self.meus_cadastros[self.Login_var_temp]["email"])
        self.Login_my_acc.set(self.Login_var_temp)
              
        self.main_buttons()              
        
        self.alterar_login = tk.Button(self.core, bg = "black", image = self.alterar, width = 100, command = lambda n=0: self.alterar_dados(n))              
        self.alterar_login.place(x = 509, y = 295)
        
        self.login_label = tk.Label(self.core, fg = "green2", bg = "black", textvariable = self.Login_my_acc, width = 15, height = 2)  
        self.login_label.place(x = 370, y = 295)   
        
        self.email_label = tk.Label(self.core, fg = "green2", bg = "black", textvariable = self.email_show, width = 20, height = 2)  
        self.email_label.place(x = 335, y = 350)   
        
        self.user_label = tk.Label(self.core, fg = "green2", bg = "black", textvariable = self.user_my_acc, width = 15, height = 2)  
        self.user_label.place(x = 370, y = 405)   
        
        self.alterar_usuario = tk.Button(self.core, bg = "black", image = self.alterar, width = 100, command = lambda n=2: self.alterar_dados(n))              
        self.alterar_usuario.place(x = 509, y = 405)
        
        self.alterar_avatar = tk.Button(self.core, bg = "black",  image = self.avatar_sel, width = 135, height = 120,  command = lambda n=4: self.alterar_dados(n))              
        self.alterar_avatar.place(x = 345, y = 118)        
        
        self.alterar_email = tk.Button(self.core, bg = "black",  image = self.alterar, width = 100, command = lambda n=1: self.alterar_dados(n))              
        self.alterar_email.place(x = 509, y = 350)
        
        self.alterar_senha = tk.Button(self.core, bg = "black",  image = self.alterar_senha_image, width = 120, command = lambda n=3: self.alterar_dados(n))              
        self.alterar_senha.place(x = 360, y = 470)
        
        self.salvar_alterações = tk.Button(self.core, bg = "black", fg = "green2" , image = self.salvar_alt, width = 150, command = self.salvar_alterações)              
        self.salvar_alterações.place(x = 345, y = 525)
        
        self.discartar_alterações = tk.Button(self.core, bg = "black", fg = "green2" , image = self.discartar_alt, width = 150, command = self.discartar_alterações)              
        self.discartar_alterações.place(x = 345, y = 574)            
    
    def alterar_dados(self,numero):

        self.alterar_w = tk.Toplevel()
        self.alterar_w.title("Synchromatic")
        self.alterar_w.geometry("400x300")
        self.alterar_w.resizable(height = False, width=False)
        self.BG = tk.Label(self.alterar_w, bg = "black", width = 300, height = 300)
        self.BG.place(x = 0, y = 0)   
        
        if numero == 0:
            self.Label_Login = tk.Label(self.alterar_w,text="Novo Login", font = "Helvetica", fg = "green2", bg = "black", height = 3, width = 10)        
            self.Label_Login.place(x = 130, y = 30)           
            self.Insert_Login = tk.Entry(self.alterar_w, textvariable=self.Login, font = "Helvetica 20")
            self.Insert_Login.place(x = 55, y= 100)  
            self.alterar_loginn = tk.Button(self.alterar_w, bg = "black", image = self.alterar, width = 100, command = lambda n=0: self.alterar_click(n))              
            self.alterar_loginn.place(x = 150, y = 200)
            
        if numero == 1:
 
            self.Label_Email = tk.Label(self.alterar_w,text="Novo Email", font = "Helvetica", fg = "green2", bg = "black", height = 3, width = 10)        
            self.Label_Email.place(x = 130, y = 30)           
            self.Insert_Email = tk.Entry(self.alterar_w, textvariable=self.email, font = "Helvetica 20")
            self.Insert_Email.place(x = 55, y= 100)  
            self.alterar_emaill = tk.Button(self.alterar_w, bg = "black", image = self.alterar, width = 100, command = lambda n=1: self.alterar_click(n))              
            self.alterar_emaill.place(x = 150, y = 200)
        
        if numero == 2:
            self.Label_User = tk.Label(self.alterar_w,text="Novo Usuário", font = "Helvetica", fg = "green2", bg = "black", height = 3, width = 10)        
            self.Label_User.place(x = 130, y = 30)           
            self.Insert_User = tk.Entry(self.alterar_w, textvariable=self.username, font = "Helvetica 20")
            self.Insert_User.place(x = 55, y= 100)                 
            self.alterar_usuarioo = tk.Button(self.alterar_w, bg = "black", image = self.alterar, width = 100, command = lambda n=2: self.alterar_click(n))              
            self.alterar_usuarioo.place(x = 150, y = 200)    
        
        if numero == 3:
            self.Label_Senha = tk.Label(self.alterar_w,text="Nova Senha", font = "Helvetica", fg = "green2", bg = "black", height = 3, width = 10)        
            self.Label_Senha.place(x = 130, y = 30)           
            self.Insert_Senha = tk.Entry(self.alterar_w, textvariable=self.Senha, font = "Helvetica 20", show='*')
            self.Insert_Senha.place(x = 55, y= 100)  
            self.alterar_senhaa = tk.Button(self.alterar_w, bg = "black", image = self.alterar, width = 100, command = lambda n=3: self.alterar_click(n))              
            self.alterar_senhaa.place(x = 150, y = 200)    
        
        if numero == 4:
            self.Label_Avatar = tk.Label(self.alterar_w,text="Escolha o seu avatar", font = "Helvetica", fg = "green2", bg = "black", height = 3, width = 20)        
            self.Label_Avatar.place(x = 100, y = 15)           
            
            self.alterar_avatar_left = tk.Button(self.alterar_w, bg = "black", image = self.left, width = 50, command = lambda n=0: self.cycle_choices(n))              
            self.alterar_avatar_left.place(x = 60, y = 150) 

            self.alterar_avatar_right = tk.Button(self.alterar_w, bg = "black", image = self.right, width = 50, command = lambda n=1: self.cycle_choices(n))              
            self.alterar_avatar_right.place(x = 290, y = 150)  
            
            self.alterar_avatar_photo = tk.Label(self.alterar_w, bg = "black",  image = self.avatar_var[self.choice_ind], width = 100, height = 100)              
            self.alterar_avatar_photo.place(x = 150, y = 100)       
            
            self.alterar_avatar = tk.Button(self.alterar_w, bg = "black", image = self.alterar, width = 100, command = lambda n=4: self.alterar_click(n))              
            self.alterar_avatar.place(x = 150, y = 250)        
    
    def cycle_choices(self,numero):    
        if numero == 0:
            self.choice_ind -= 1
        else:
            self.choice_ind += 1
        
        if self.choice_ind < 0:
            self.choice_ind += 5

        elif self.choice_ind > 4:
            self.choice_ind -= 5 
            
        self.alterar_avatar_photo.configure(image = self.avatar_var[self.choice_ind])             
 
    def discartar_alterações(self):
          
        self.Senha.set(self.meus_cadastros[self.Login_var_temp]["senha"])
        self.Login_my_acc.set(self.Login_var_temp)
        self.email_show.set(self.meus_cadastros[self.Login_var_temp]["email"])
        self.user_my_acc.set(self.meus_cadastros[self.Login_var_temp]["username"])
        
    def salvar_alterações(self):
        
        self.alterar_w = tk.Toplevel()
        self.alterar_w.title("Synchromatic")
        self.alterar_w.geometry("400x400")
        self.alterar_w.resizable(height = False, width=False)
        self.BG = tk.Label(self.alterar_w, bg = "black", width = 300, height = 300)
        self.BG.place(x = 0, y = 0) 
        
        self.Rest_User = tk.Label(self.alterar_w,text="Digite a sua senha antiga para confirmar as alterações", font = "Helvetica 8", fg = "green2", bg = "black", height = 3, width = 45)        
        self.Rest_User.place(x = 70, y = 30)      
        self.Error_senha = tk.Label(self.alterar_w,text="Digite a senha correta", font = "Helvetica 8", fg = "green2", bg = "black", height = 3, width = 18)
        self.Insert_Senha = tk.Entry(self.alterar_w, textvariable=self.Senha_conf, font = "Helvetica 20", show='*')
        self.Insert_Senha.place(x = 60, y = 100)                 
        self.alterar_tudo = tk.Button(self.alterar_w, bg = "black", image = self.alterar, width = 100, command = self.salvar_accept)              
        self.alterar_tudo.place(x = 150, y = 300)    
    
    def salvar_accept(self): 
        
        self.Senha_check = self.Senha_conf.get()
        if self.meus_cadastros.get(self.Login_var_temp)["senha"] == self.Senha_check:
            self.jogos_favoritos = self.meus_cadastros.get(self.Login_var_temp)["jogos"]          
            del self.meus_cadastros[self.Login_var_temp]
            self.number_ind = str(self.choice_ind)              
            self.meus_cadastros[self.Login_my_acc.get()] = {"senha": self.Senha_t, "jogos" : self.jogos_favoritos, "email": self.email_show.get(), "username": self.user_my_acc.get(), "useravatar": self.number_ind}
            self.database = open("cadastros.data", "wb")
            pickle.dump(self.meus_cadastros,self.database)
            print(self.meus_cadastros)        
            self.database.close()
            self.Login_show.set(self.user_my_acc.get()) 
            self.Login_var_temp = self.Login_my_acc.get()
            self.alterar_w.destroy()
            self.my_conta()
        else:
            self.Error_senha.place(x = 150, y = 200)
            
    def alterar_click(self, numero):
        
        if numero == 0:
            self.Login_temp = self.Login.get()
            self.Login_my_acc.set(self.Login_temp)
        elif numero == 1:
            self.Email_tempp = self.email.get()
            self.email_show.set(self.Email_tempp)
        elif numero == 2:
            self.Uservow = self.username.get()            
            self.user_my_acc.set(self.Uservow)
        elif numero == 3:
            self.Senha_t = self.Senha.get()
        elif numero == 4:
            self.alterar_avatar.configure(image = self.avatar_var[self.choice_ind])
        self.alterar_w.destroy()   
    
    def my_fav(self):
        
        self.var = 6
        self.BG = tk.Label(self.core, bg = "black", image = self.My_Fav) 
        self.BG.grid(row=0, column=0, columnspan = 8, rowspan = 16, sticky="nsew")                  
        self.main_buttons()        
        #self.Pesqui_av= tk.Button(self.core, bg = "black",  fg = "green2", text = "Pesquisa Avançada" , height = 2, width = 56, command = lambda n=4: self.access_games(n))              
        #self.Pesqui_av.place(x = 219, y = 60) 
        self.Games_entry = tk.Entry(self.core, width = 30, bg = "black", fg= "green2", textvariable=self.game_entry ,font = "Helvetica 18")
        self.Games_entry.bind("<Return>", self.pesquisa)           
        self.Games_entry.place(x = 220, y = 19)             
        self.n_games = len(self.meus_cadastros[self.Login_var_temp]["jogos"])
        self.favorite_list = []        
        for i in range(self.n_games):                
            self.games_var = self.meus_cadastros[self.Login_var_temp]["jogos"][i] 
            self.game_ID = int(self.games_var)
            self.actual = self.all_games.games(self.game_ID)                    
            self.var_erasing = self.game_ID + 4
            self.game_buttons = tk.Button(self.core, bg = "black", height = 100, width = 100 ,image = self.actual[self.games_var]["button"], command = lambda n = self.var_erasing: self.erase_labels(n))
            self.game_buttons.place(x = i*140 + 225 - (i//3)*420 , y = (i//3)*120 + 200)             
            self.favorite_list.append(self.game_buttons)         
        
    def favorite_new(self, game_id):
        
        self.meus_cadastros[self.Login_var_temp]["jogos"].append(str(game_id))
        self.database = open("cadastros.data", "wb")
        pickle.dump(self.meus_cadastros,self.database)
        print(self.meus_cadastros)        
        self.database.close()
        #self.email_timer = Timer(self.Email_gen.secs, self.Email_gen.mandar_email(self.Email_var_temp, self.gta_site))
        #self.email_timer.start()
        self.FAV.place_forget()
        self.FAV = tk.Button(self.core, bg = "black", image = self.fav , height = 50, width = 50, command = lambda n=game_id: self.des_favorite(n))              
        self.FAV.place(x = 499, y = 507)         
    
    def des_favorite(self, numero):
        
        self.meus_cadastros[self.Login_var_temp]["jogos"].remove(str(numero))
        self.database = open("cadastros.data", "wb")
        pickle.dump(self.meus_cadastros,self.database)
        print(self.meus_cadastros)        
        self.database.close()
        self.FAV.place_forget()
        self.FAV = tk.Button(self.core, bg = "black", image = self.not_fav , height = 50, width = 50, command = lambda n=numero: self.favorite_new(n))              
        self.FAV.place(x = 499, y = 507) 
    
    def main_buttons(self):
        
        self.choice_ind = int(self.meus_cadastros[self.Login_var_temp]["useravatar"])  
        self.avatar = tk.Label(self.core, bg = "black", image = self.avatar_var[self.choice_ind], height = 85, width = 100)  
        self.avatar.place(x = 42, y = 7)        
        self.name_login = tk.Label(self.core, fg = "green2", bg = "black", textvariable = self.Login_show, width = 12)  
        self.name_login.place(x = 57, y = 108)                     
        self.My_account = tk.Button(self.core, bg = "black", fg = "green2" , text= "Minha Conta", width = 12, command = lambda n=1: self.erase_labels(n))              
        self.My_account.place(x = 50, y = 170) 
        self.My_Favor = tk.Button(self.core, bg = "black", fg = "green2" , text= "Meus Favoritos", width = 12, command = lambda n=2: self.erase_labels(n))              
        self.My_Favor.place(x = 50, y = 200)                 
        self.Menu_Principal = tk.Button(self.core, bg = "black", fg = "green2" , text= "Destaques", width = 12, command = lambda n=0: self.erase_labels(n))              
        self.Menu_Principal.place(x = 50, y = 230) 
        self.Logout = tk.Button(self.core, bg = "black", fg = "green2" , text= "Log out", width = 12, command = lambda n=4: self.erase_labels(n) )              
        self.Logout.place(x = 50, y = 260)          
                 
        
    def access_games(self, numero): 
        
        self.var = 7        
        self.BG = tk.Label(self.core, bg = "black", image = self.bg_pages_show)
        self.BG.grid(row=0, column=0, columnspan = 8, rowspan = 16, sticky="nsew") 
        self.main_buttons()        
            
        self.actual = self.all_games.games(numero)
        
        self.Canvas_master= tk.Canvas(self.core, highlightthickness=0, width=464, height=670)
        self.Canvas_master.place(x = 186, y = 0)
        
        self.game_ID = "{0}".format(numero)        
        
        self.Canvas_master.create_image(232, 334, image = self.jogos_canvas)
        self.Canvas_master.create_text(230, 30, fill = "green2", font = "Engravers 20", text = self.actual[self.game_ID]["nome"])
        self.Canvas_master.create_text(235, 587, fill = "green2", text = self.actual[self.game_ID]["melhor preco"])
        self.Canvas_master.create_text(215, 383, fill = "green2", text = self.actual[self.game_ID]["descrição"])
            
        self.poster = tk.Label(self.core, bg = "black", image = self.actual[self.game_ID]["poster"])  
        self.poster.place(x = 202, y = 60)          
            
        self.plataforma = tk.Label(self.core, bg = "black", fg = "green2", image = self.actual[self.game_ID]["plataforma"], height = 30, width = 60)  
        self.plataforma.place(x = 385, y = 544)
        
        self.Melhor_preço = tk.Button(self.core, bg = "black", image = self.actual[self.game_ID]["melhor preco imagem"], height = 40, width = 130, command = lambda n= self.game_ID: self.site(self.game_ID))
        self.Melhor_preço.place(x = 470, y = 590)        


        if self.game_ID in self.meus_cadastros[self.Login_var_temp]["jogos"]:
            self.FAV = tk.Button(self.core, bg = "black", image = self.fav , height = 50, width = 50, command = lambda n=numero: self.des_favorite(n))              
            self.FAV.place(x = 499, y = 507)            
        else:
            self.FAV = tk.Button(self.core, bg = "black", image = self.not_fav , height = 50, width = 50, command = lambda n=numero: self.favorite_new(n))              
            self.FAV.place(x = 499, y = 507)                
            
        
    def site(self, jogo):
            webbrowser.open(self.actual[jogo]["melhor preco link"])
            
    def loop(self):
        self.core.mainloop()

Main = Main_Window()
Main.loop()       
