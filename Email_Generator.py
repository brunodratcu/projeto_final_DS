#  -*- coding: utf-8 -*-
"""
Created on Wed May 18 18:16:49 2016

@author: Gabriel
"""

import smtplib
from datetime import datetime


class create_email:
    
    def __init__(self):
        self.time_now = datetime.today()
        #self.new_time = self.time_now.replace(day=self.time_now.day+1, hour=0, minute = self.time_now.minute+5, second=0, microsecond=0)
        #self.new_time = self.time_now.replace(minute=self.time_now.minute+11)
        #self.delta_t= self.new_time-self.time_now
        #self.secs= self.delta_t.seconds+1


    def mandar_email(self, email, site):  
    
               self.fromaddr = "games@nerdnucleus.com"
               self.toaddrs = email
            
               self.msg = "Obrigado por utilizar o Synchromatic.\
               Hoje, dada a sua escolha de jogo, o melhor site para a compra do seu jogo favorito é: {0}".format(site).encode("UTF-8")
            
               self.server = smtplib.SMTP("insper.edu.br")
               self.server.set_debuglevel(1)
               self.server.sendmail(self.fromaddr, self.toaddrs, self.msg)
               self.server.quit()    
    
    def reset_senha(self, email, senha):           
               
               self.fromaddr = "games@nerdnucleus.com"
               self.toaddrs = email
            
               self.msg = "Obrigado por utilizar o Synchromatic.\
               A sua nova senha é {0}. Caso queira alterar ela, use o botão alterar senha na aba Minha Conta.".format(senha).encode("UTF-8")
            
               self.server = smtplib.SMTP('insper.edu.br')
               self.server.set_debuglevel(1)
               self.server.sendmail(self.fromaddr, self.toaddrs, self.msg)
               self.server.quit()    
