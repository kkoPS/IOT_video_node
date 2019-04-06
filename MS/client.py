#!/usr/bin/env python3

from flask import Flask, json, request
from flask_restplus import Resource, Api
from flask_restplus import Resource, Api
from values import Configuration

app = Flask(__name__)
api = Api(app, version='1.0', title='PiVideoAPI',
    description='Expose the PiVideo functionality interraction',
)

ns = api.namespace('pivideo', description='Interraction with the PiVideo')

class base(Resource):
  
  def get(self):
    response = app.response_class(
      response=json.dumps({'routes':{'/':'base', '/config':'change config'}}),
      status=200,
      mimetype='application/json'
    )
    return response

class paramRecod(Resource):
  """interracting with configuration file"""

  @api.response(200, 'Successing')
  def get(self):
    config = Configuration()
    config.load()

    record_values = config.get("Record")
    return record_values, 200  
  
  @api.response(201, 'Key created successfuly')
  def post(self):
    config = Configuration()
    config.load()

    t_before = request.forms['t_before']
    t_after = request.forms['t_after']
    
    if t_before != None:
      config.set(route='record', key='t_before', value=key_before)
    if t_after != None:
      config.set(route='record', key='t_after', value=key_after)
    config.store()
    
    if
    config.set(route='param', key=request.args['key'], value=request.form['value'])
    config.store()
    return None, 201

@ns.route('/record', methods=['GET', 'POST'])
@ns.response(200, 'successing')
class Record(Resource):  
       
    def get(self):
        config = Configuration()
        config.load() 

        key_before = request.args.get('t_before')
        key_after = request.args.get('t_after')
        list_value = config.get('record')

        #get the attribute of t_before
        if key_before != None:
          for dict_value in list_value:
            if 't_before' in dict_value.keys():
              return dict_value['t_before'], 200
        #get the attribute of t_after
        if key_after != None:
          for dict_value in list_value:
            if 't_after' in dict_value.keys():
              return dict_value['t_after']
        #get all attributes of record
        if key_before == None and key_after == None:
          return config.get('record')

        # appel du script qui lance l'enregistrement




    @api.response(201, 'Key created successfuly')
            
api.add_resource(base, '/')
api.add_resource(Record, '/record', methods=['GET']) # Route_Record
api.add_resource(Stream, '/stream')
api.add_resource(paramRecord, '/param/record')
api.add_resource(parmBackend, '/param/backend')

if __name__ == "__main__":
    app.run(port='2000')

