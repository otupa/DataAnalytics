
# Module Imports
import mariadb
import sys

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
    
def show_tables():
    connect = Connect()
    connect.cursor.execute(
        "select table_name \
        FROM information_schema.tables \
        WHERE table_schema = 'database_g4';")
    list_ = [tables[0] for tables in connect.cursor.fetchall()]
    connect.close_db()
    return list_

def search_runs(table_name, initial_date, final_date):
    connect = Connect()
    connect.cursor.execute(
        "SELECT DATE_FORMAT(date_time, '%d/%m/%Y %H:%i'), valor \
        FROM database_g4.{} \
        WHERE date_time \
        BETWEEN '{}' AND '{}';".format(table_name, initial_date, final_date))
    list_ = [[tables[0], tables[1]] for tables in connect.cursor.fetchall()]
    connect.close_db()
    return list_
    




    

    
