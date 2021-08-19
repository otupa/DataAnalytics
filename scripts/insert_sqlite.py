from scripts.connect_sql import Connect
import csv
import os

def csv_inject():
    db = Connect()

    schemas = open(os.path.join('sql', 'schema_table.sql'))
    for line in schemas:
        db.cursor.execute(line)
    print('tabelas')
    db.commit_db()

    for file in os.listdir('data_csv'):
        print(file)

        sql_archive = open(
            os.path.join('sql/insert', file[:-4]+'.sql'), 'r').read()
        print(sql_archive)

        csv_archive = csv.reader(open(
            os.path.join('data_csv', file), 'rt'), delimiter=',')

        for line in csv_archive:
            scheme = sql_archive.format(line[0], str(line[1]))
            print(scheme)
            db.cursor.execute(scheme)
    
    db.commit_db()
    db.close_db()



