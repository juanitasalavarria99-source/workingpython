import sqlite3

def get_connection():
    conn = sqlite3.connect('database/studentsuleam.db')

    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            curso TEXT,
            carrera TEXT,
            facultad TEXT
        )
    ''')
    conn.commit()
    conn.close()
