import os
import psycopg2
import dotenv

dotenv.load_dotenv()

conn = psycopg2.connect(
    host="localhost",
    database="todoapppython",
    user=os.environ["DB_USERNAME"],
    password=os.environ["DB_PASSWORD"],
)

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS todos;")
cur.execute(
    "CREATE TABLE todos (id serial PRIMARY KEY,"
    "title varchar (255) NOT NULL,"
    "description varchar (255) NOT NULL,"
    "date_added timestamp DEFAULT CURRENT_TIMESTAMP);"
)

cur.execute(
    "INSERT INTO todos (title, description)" "VALUES (%s, %s)",
    ("TestTitle", "test"),
)

conn.commit()

cur.close()
conn.close()
