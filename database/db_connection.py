import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="Food_Waste",
        user="postgres",
        password="system",
        port=5432
    )
    return conn