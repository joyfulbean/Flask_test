from sqlalchemy import *
from flask_restful import Resource, Api, abort
from flask import *

from machine import Machine_function

app = Flask(__name__)
api = Api(app)

print('successfully connected to postgres and flask server\n')

api.add_resource(Machine_function, '/')

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port = 62334)
    
    

