# from datetime import datetime
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from models import Machine


class MachineSchema(ModelSchema):
    class Meta:
        model = Machine
