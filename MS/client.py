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

class param(Resource):
  """interracting with configuration file"""

  @api.response(200, 'Successing')
  def get(self):
    config = Configuration()
    config.load()
    value = config.get(request.args['key'])
    return value, 200  
  
  @api.response(201, 'Key created successfuly')
  def post(self):
    config = Configuration()
    config.load()
    config.set(route='param', key=request.args['key'], value=request.form['value'])
    config.store()
    return None, 201

@ns.route('/record', methods=['GET', 'POST'])
@ns.response(200, 'successing')
@ns.param('t_before', 'time identifier')
@ns.param('t_after', 'time identifier')
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
    
    @api.response(201, 'Key created successfuly')
    def post(self):
        config = Configuration()
        config.load() 

        key_before = request.args.get('t_before')
        key_after = request.args.get('t_after')

        if key_before != None:
          config.set(route='record', key='t_before', value=key_before)
          config.store() 
        #get the attribute of t_after
        if key_after != None:
          print("oke")
          config.set(route='record', key='t_after', value=key_after)
          config.store()

        return None, 201
            
api.add_resource(Record, '/record', methods=['GET', 'POST']) # Route_Record
api.add_resource(base, '/')
api.add_resource(param, '/param')

if __name__ == "__main__":
    app.run(port='2000')

