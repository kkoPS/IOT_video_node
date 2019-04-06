#!/usr/bin/python3
 # -*- coding: utf-8 -*-

import os.path
from shutil import copyfile
import json

configfile = 'config_file.json'
configDefault = 'config_default.json'

# TODO : use logging

class Configuration():

    def __init__(self):
      self._values = {}

    def load(self):  
      #create config file if don't exist
      if not os.path.exists(configfile):
        print("file doesn't exist")
        open(configfile, 'a').close()
      
        #copy default config file
        copyfile(configDefault, configfile)    

      with open(configfile) as json_data_file:
        data = json.load(json_data_file)
        self._values = data
              
    def store(self):
      data = self._values

      with open(configfile, 'w') as json_data_file:
        json.dump(data, json_data_file)
        
    def get(self, route, key):
      data = self._values
      try:          
        value = data[route][key]

      except KeyError as error:
        print ("Key not fount : %s" % error)

      return value
    
    def set(self, route, key, value):
      data = self._values
      data[route][key] = value
      self._value = data
      #
      #i = 0
      ##parcourt le dico à la recherche de la route
      #if route in self._values.keys():
      #  #pour chaque route on a une liste de dictionnaire
      #  for key_dic in self._values[route]:
      #    #regarde si la clé de l'url est contenue dans la liste
      #    if key in key_dic.keys():
      #      print(key)
      #      #changement de la valeur
      #      self._values[route][i][key] = float(value)
      #    i += 1
 
#======================================================
# TESTS
#======================================================
config = Configuration()
config.load()
print config.get('record', 't_before')


