import sys
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import timedelta

basedir = os.path.dirname(os.path.abspath(__file__))
env_path = '.env'
load_dotenv(dotenv_path=env_path)


def is_linux_system():
    return sys.platform == "linux" or sys.platform == "linux2"


if not is_linux_system():
    os.environ['DB_SERVICE'] = "localhost"


class BaseConfig(object):
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_SERVICE = os.environ['DB_SERVICE']
    DB_PORT = os.environ['DB_PORT']
    DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_SERVICE}:{DB_PORT}/{DB_NAME}'
