import psycopg2
from dotenv import load_dotenv
import os


load_dotenv("creds.env")
conn_credentials = os.environ.get("psql_creds")

def create_table():
    conn = psycopg2.connect(conn_credentials)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (email TEXT, password BYTEA, salt TEXT, user_id UUID)")
    conn.commit()
    cur.close()
    conn.close()