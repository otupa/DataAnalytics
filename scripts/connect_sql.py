
# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
class Connect():
    def __init__(self):
        try:
            self.conn = mariadb.connect(
                user="tupa",
                password="admin",
                host="localhost",
                port=3306,
                database="database_g4")
            print('base de dados conectada')
            #self.conn.autocommit = False
            self.cursor = self.conn.cursor()

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    def commit_db(self): 
        self.conn.commit()

    def close_db(self): 
        self.conn.close()
