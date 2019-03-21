#!/usr/bin/env python3

from flask import Flask, json
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class base(Resource):
  
  def get(self):
    response = app.response_class(
      response=json.dumps({'routes':{'/':'base', '/config':'change config'}}),
      status=200,
      mimetype='application/json'
    )
    return response

class config(Resource):
  """interracting with configuration file"""

  def get(self):
    return 'hello'

api.add_resource(base, '/')
api.add_resource(config, '/config')

if __name__ == "__main__":
    app.run(port='2000')

