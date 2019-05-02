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

class paramRecord(Resource):
  """interracting with configuration file"""

  @api.response(200, 'Successing')
  def get(self):
    config = Configuration()
    config.load()
    record_values = {}
    record_values['t_before'] = config.get("record", "t_before")
    record_values['t_after'] = config.get("record", "t_after")

    return json.dumps(record_values), 200
  
  @api.response(201, 'Key created successfully')
  def post(self):
    config = Configuration()
    config.load()

    # TODO: check sent value is an integer
    try:
      t_before = request.form['t_before']
    except:
      t_before = None
    try:
      t_after = request.form['t_after']
    except:
      t_after = None

    if t_before != None:
      config.set(route='record', key='t_before', value=t_before)
    if t_after != None:
      config.set(route='record', key='t_after', value=t_after)
    config.store()
    
    return None, 201

class Record(Resource):  

  api.response(200, 'record started')   
  def get(self):
    config = Configuration()
    config.load() 
    t_before = config.get('record', 't_before')
    t_after = config.get('record', 't_after')
    # appel du script qui lance l'enregistrement

    return None, 200

            
api.add_resource(base, '/')
api.add_resource(Record, '/record', methods=['GET']) # Route_Record
api.add_resource(paramRecord, '/param/record')

if __name__ == "__main__":
    app.run(port='2000')

