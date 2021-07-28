from scripts.connect_sql import Connect
import csv
import os

def csv_inject():
    db = Connect()

    schemas = open(os.path.join('sql', 'schema_table.sql')).read()
    db.cursor.executescript(schemas)
    db.commit_db()

    for file in os.listdir('data_csv'):

        sql_archive = open(
            os.path.join('sql', file[:-4]+'.sql'), 'r').read()

        csv_archive = csv.reader(open(
            os.path.join('data_csv', file), 'rt'), delimiter=',')

        for line in csv_archive:
            db.cursor.execute(sql_archive, line)
        db.commit_db()
        db.close_db()



