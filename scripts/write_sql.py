import os

def write_sql_table(arg):
    table = open(os.path.join('sql', "schema_table.sql"), "a")
    schema_ = "CREATE TABLE IF NOT EXISTS {}(\
date_time DATETIME, valor VARCHAR(11) NOT NULl);\n".format(arg)
    table.write(schema_)

def write_sql_insert(tb_name, name):
    table = open('sql/insert/'+name+'.sql', "w")
    schema_ = "INSERT IGNORE INTO {} (date_time, valor) \
VALUES ('{}','{}')".format(tb_name, {}, {})
    table.write(schema_)

def write_sql_search(tb_name):
    table = open(os.path.join('sql/search/', 'SEARCH_'+tb_name+'.sql'), "w")
    schema_ = "SELECT * FROM database_g4.{} WHERE date_time\
BETWEEN ('{}') AND ('{}');".format(tb_name, {}, {})
    table.write(schema_)

def write():
    for file in os.listdir('data_csv'):
        nome_csv = os.path.basename(file)[:-4]
        name = nome_csv.replace(" ", "_")
        write_sql_table(name)
        write_sql_insert(name, nome_csv)
        write_sql_search(name)