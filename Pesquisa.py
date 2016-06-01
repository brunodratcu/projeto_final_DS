# -*- coding: utf-8 -*-
"""
Created on Mon May 30 00:29:36 2016

@author: Gabriel
"""

import dados

class pesquisa:
    
    def __init__(self):
        
        self.info = dados.data()
        self.game_list = self.info.list_games()
    
    def find_game(self, find):
        
        self.games_found = []
        for s in range(len(find)):
            for i in range(len(self.game_list[0])):
                for r in range(len(self.game_list[0][i])):
                    if self.game_list[0][i][r] == find[s]:
                        if not self.game_list[2][i] in self.games_found:
                            self.games_found.append(self.game_list[2][i])
        return self.games_found                
                    
                    
                
        