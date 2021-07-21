import os

def write_sql_table(arg):
    table = open(os.path.join('sql', "schema_table.sql"), "a")
    schema_ = "CREATE TABLE {} (cod INTEGER PRIMARY KEY, data TEXT NOT NULL, hora INTEGER, valor VARCHAR(11) NOT NULl);\n".format(arg)
    table.write(schema_)

def write_sql_insert(tb_name, name):
    table = open('sql/insert/'+name+'.sql', "w")
    schema_ = "INSERT INTO {} (data, hora, valor) VALUES (?,?,?)".format(tb_name)
    table.write(schema_)

def write_sql_search(tb_name):
    table = open(os.path.join('sql/search/', 'SEARCH_'+tb_name+'.sql'), "w")
    schema_ = "SELECT cod, data, hora, valor FROM {} WHERE data=?".format(tb_name)
    table.write(schema_)

def write():
    for file in os.listdir('data_csv'):
        nome_csv = os.path.basename(file)[:-4]
        name = nome_csv.replace(" ", "_")
        write_sql_table(name)
        write_sql_insert(name, nome_csv)
        write_sql_search(name)