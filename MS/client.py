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
    config.set(key=request.args['key'], value=request.form['value'])
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
        #get the attribute of t_before
        if key_before != None:
            value = config.get('record')
            return value[0]
        #get the attribute of t_after
        elif key_after != None:
            value = config.get('record')
            return value[1]
        #get all attributes of record
        else:
            value = config.get('record')

        return value
    
    def post(self):
        config = Configuration()
        config.load() 

        value_t_before = request.args.get('t_before')
        value_t_after = request.args.get('t_after')

        '''if value_t_before != None:
            #config.set('record', 't_before', value_t_before)
            
        #get the attribute of t_after
        elif value_t_after != None:
            #config.set('record', 't_after', value_t_after)'''
            
api.add_resource(Record, '/record', methods=['GET', 'POST']) # Route_Record
api.add_resource(base, '/')
api.add_resource(param, '/param')

if __name__ == "__main__":
    app.run(port='2000')

