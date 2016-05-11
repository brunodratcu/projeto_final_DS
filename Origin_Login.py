# -*- coding: utf-8 -*-
"""
Created on Fri May  6 18:55:19 2016

@author: Gabriel
"""

import pickle

cadastros = {"Gabriel": "123","Felipe":"1234"}

database = open("cadastros.data", "wb")

pickle.dump(cadastros, database)

database.close()
