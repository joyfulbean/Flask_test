from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from config import BaseConfig

class Machine(declarative_base()):
    __tablename__ = 'machine'
    port = Column(Integer, primary_key=True)
    root_path = Column(String(200))
    max_capacity = Column(Integer)
    left_capacity = Column(Integer)

    def __repr__(self):
        return "<Machine(port='{}', root_path='{}', max_capacity={}, left_capacity={})>"\
            .format(self.port, self.root_path, self.max_capacity, self.left_capacity)
