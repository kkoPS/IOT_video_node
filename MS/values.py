#!/usr/bin/python3
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

    def get(self, key):
      try:
        with open(configfile) as json_data_file:
          data = json.load(json_data_file)
          self._values = data
          
          value = self._values[key]

      except KeyError as error:
        print ("Key not fount : %s" % error)

      return value
    
    def set(self, key, value):
      self._values[key] = value

config = Configuration()
config.load()
config.get('record')


