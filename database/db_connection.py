import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="DATABASE URL",
        database="neondb",
        user="neondb_owner",
        password="*********",
        sslmode="require"
    )
    return conn