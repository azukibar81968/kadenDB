import psycopg2
import os

def get_connection():
    connection = psycopg2.connect(
        database = 'postgres',
        user = 'postgres',
        password='passw0rd',
        host='0.0.0.0',
        port = 5432
    )
    return connection

conn = get_connection()
cursor = conn.cursor()

sql = """select * from weather;"""
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)
