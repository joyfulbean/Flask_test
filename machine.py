from flask import *
from flask_restful import Resource, Api, abort
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from serializer import MachineSchema
from models import Machine
from config import BaseConfig

DATABASE_URI = BaseConfig.DATABASE_URI
engine = create_engine(DATABASE_URI)
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
s = Session()

class Machine_function(Resource):

    # read
    def get(self):
        data = request.get_json()
        requested_data = s.query(Machine).filter_by(port=data['port']).first()
        output = MachineSchema().dump(requested_data)
        if requested_data:
            return jsonify({'data': output})
        else:
            return jsonify({"failed": "entry not found"}), 404

    # update
    def put(self):
        data = request.get_json()
        try:
            m = s.query(Machine).filter_by(port=data['port']).first()
            m.left_capacity = data['left_capacity']
            s.commit()
        except Exception as e:
            print(e)
            abort(500)

        return jsonify({'successfully put data': True})

    # delete
    def delete(self):
        data = request.get_json()
        try:
            m = s.query(Machine).filter_by(port=data['port']).first()
            s.delete(m)
            s.commit()
        except Exception as e:
            print(e)
            abort(500)
        return jsonify({'successfully deleted': True})

    # create
    def post(self):
        data = request.get_json()
        try:
            new_data = Machine(port=data['port'], root_path=data['root_path'],
                               max_capacity=data['max_capacity'],
                               left_capacity=data['left_capacity'])
            s.add(new_data)
            s.commit()
        except Exception as e:
            print(e)
            abort(500)
        return jsonify({'successfully created data': True})
