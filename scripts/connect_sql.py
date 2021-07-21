import sqlite3

class Connect():
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        
    # Salva modificações na db
    def commit_db(self):
        if self.conn:
            self.conn.commit()

    # Fecha conexão com a base de dados
    def close_db(self):
        if self.conn:
            self.conn.close()
