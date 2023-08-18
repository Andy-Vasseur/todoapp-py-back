import os
import psycopg2
from flask import Flask
import dotenv

dotenv.load_dotenv()


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="todoapppython",
        user=os.environ["DB_USERNAME"],
        password=os.environ["DB_PASSWORD"],
    )

    return conn
