import psycopg2
import os

def get_connection():
    dsn = os.environ.get('postgresql://')
    return psycopg2.connect(dsn)