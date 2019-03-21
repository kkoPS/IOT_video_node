import json

configfile = 'config.json'

class Configuration:

    def __init__(self):
        pass

    def load(self):
        with open(configfile) as json_data_file:
            data = json.load(json_data_file)

        self.val1 = data['val1']
        self.val2 = data['val2']

    def store(self):
        data = json
        data['val1'] = self.val1
        data['val2'] = self.val2

        with open(configfile, 'w') as outfile:
            json.dump(data, outfile)