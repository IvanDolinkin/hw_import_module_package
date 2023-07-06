import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')

# Для теста создал запрос к базе данных из прошлого дз "dvdrental"

conn = psycopg.connect(dbname=db, user=user, password=password)
cursor = conn.cursor()

cursor.execute('SELECT first_name, last_name FROM actor LIMIT 10')
records = cursor.fetchall()

print(records)

cursor.close()
conn.close()
