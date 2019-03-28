#!/usr/bin/python3

import json

configfile = 'config.json'

# TODO : use logging

class Configuration():

    def __init__(self):
      self._values = {}

    def load(self):  
      ## if not exist create ou null
      #  
      with open(configfile) as json_data_file:
        data = json.load(json_data_file)
        self._values = data
      
    def store(self):
        data = self._values

        with open(configfile, 'w') as json_data_file:
            json.dump(data, json_data_file)

    def get(self, key):
      try:
        value = self._values[key]
      except KeyError as error:
        print ("Key not fount : %s" % error)
        value = None
        
      return value
    
    def set(self, key, value):
      self._values[key] = value
      