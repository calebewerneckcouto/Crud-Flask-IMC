# database.py
import sqlite3

def create_db():
    conn = sqlite3.connect('imc.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS imc_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            height REAL NOT NULL,
            weight REAL NOT NULL,
            imc REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_record(name, height, weight, imc):
    conn = sqlite3.connect('imc.db')
    c = conn.cursor()
    c.execute('INSERT INTO imc_records (name, height, weight, imc) VALUES (?, ?, ?, ?)', (name, height, weight, imc))
    conn.commit()
    conn.close()

def get_all_records():
    conn = sqlite3.connect('imc.db')
    c = conn.cursor()
    c.execute('SELECT * FROM imc_records')
    records = c.fetchall()
    conn.close()
    return records

def get_record(record_id):
    conn = sqlite3.connect('imc.db')
    c = conn.cursor()
    c.execute('SELECT * FROM imc_records WHERE id = ?', (record_id,))
    record = c.fetchone()
    conn.close()
    return record

def update_record(record_id, name, height, weight, imc):
    conn = sqlite3.connect('imc.db')
    c = conn.cursor()
    c.execute('UPDATE imc_records SET name = ?, height = ?, weight = ?, imc = ? WHERE id = ?', (name, height, weight, imc, record_id))
    conn.commit()
    conn.close()

def delete_record(record_id):
    conn = sqlite3.connect('imc.db')
    c = conn.cursor()
    c.execute('DELETE FROM imc_records WHERE id = ?', (record_id,))
    conn.commit()
    conn.close()
