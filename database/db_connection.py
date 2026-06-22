import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="ep-shiny-frog-atr05zw4-pooler.c-9.us-east-1.aws.neon.tech",
        database="neondb",
        user="neondb_owner",
        password="npg_5GAOUeQaZp4W",
        sslmode="require"
    )
    return conn