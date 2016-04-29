# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:20:17 2016

@author: Bruno Dratcu
"""

import projeto_final
import webbrowser


gta_poster = webbrowser.open("http://cdn.atl.clicrbs.com.br/wp-content/uploads/sites/27/2015/04/actual_1410520494.jpg")
gta_trailer = webbrowser.open("https://www.youtube.com/watch?v=VjZ5tgjPVfU")

mario_poster = webbrowser.open("https://i.ytimg.com/vi/1dhrHlol3SM/maxresdefault.jpg")
mario_trailer = webbrowser.open("https://www.youtube.com/watch?v=eO8xe2AUY4c")


GTA = projeto_final.Pagina("GTA", 
                           "Jogo que mata pessoas", 
                           "gta_poster", 
#                           "http://cdn.atl.clicrbs.com.br/wp-content/uploads/sites/27/2015/04/actual_1410520494.jpg"
                           "R$200,00", 
                           "gta_trailer")
#                           "https://www.youtube.com/watch?v=VjZ5tgjPVfU")
                           
#print(GTA.title)

mario_bros = projeto_final.Pagina("Super Mario Bros", 
                                  "Jogo de um encanador psicodelico", 
                                  "mario_poster", 
#                                  "https://i.ytimg.com/vi/1dhrHlol3SM/maxresdefault.jpg"
                                  "R$150,00", 
                                  "mario_trailer")
#                                  "https://www.youtube.com/watch?v=eO8xe2AUY4c")

#print(mario_bros.preco)

GTA.show_trailer()