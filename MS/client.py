#!/usr/bin/env python3

from flask import Flask, json, request
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



api.add_resource(base, '/')
api.add_resource(param, '/param')

if __name__ == "__main__":
    app.run(port='2000')

