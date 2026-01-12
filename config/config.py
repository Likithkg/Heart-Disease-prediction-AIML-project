import os
from dotenv import load_dotenv

load_dotenv()

def get_db_config():
    host = os.getenv('HOST')
    database = os.getenv('DATA_BASE')
    password = os.getenv('PASSWORD')
    user = os.getenv('USER')

    return host, database, password, user