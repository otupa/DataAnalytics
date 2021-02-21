import shutil
import sqlite3
import pandas as pd
import csv
import os
import re




class SoftScript():
    def __init__(self):
        self.data_frame = []

    def filter_infos(self, arg):
        def pick_regex(arg, state=None):
            try:
                data = re.findall(r"\d+/\d+/\d+", arg)
                hora = re.findall(r"\d+\:\d+", arg)
                valor = re.findall(r"\d+\s+reais", arg)
                r = [data[0], hora[0], valor[0]]

                if not r[0]: r[0] = self.data_frame[-1][0]

                if state == 1: r[2] = "DR$"+r[2][:-6]+",00" 
                else: r[2] = "R$"+r[2][:-6]+",00"
                    
                self.data_frame.append(r)

            except Exception as error: print(error)
               
        if 'desconto no boleto' in arg: pick_regex(arg, state=1)
        else: pick_regex(arg)
            

    def extract_archives(self, file, directory):

        def capture_info(file, arg):
            info = [i for i in file if arg in i]
            return info

        archive = open(os.path.join(directory, file), 'r', 
            encoding = 'utf-8').read().splitlines()

        info = capture_info(archive, "G4 MOBILE:")
        trated_info = capture_info(info, "reais")

        archive_name = os.path.basename(directory+file)[6:][:-4][25:]
        csv_name = os.path.join('data_csv', archive_name+'.csv')

        for i in trated_info:
            self.filter_infos(i)

        pd.DataFrame(self.data_frame).to_csv(
            (csv_name), header=False, encoding='utf-8', index=False)

        self.data_frame.clear()


    def read_directory(self, func, directory, state=None):
        for i in os.listdir(directory):
            func(i) if state == None else func(i, directory) 


    def create_dirs(self):
        os.mkdir('data_csv') if True else None
        os.mkdir('sql') if True else None


    def delete_files(self):
        shutil.rmtree('data_csv', ignore_errors=True, onerror=None)
        shutil.rmtree('sql', ignore_errors=True, onerror=None)
        try: os.remove('database.db')
        except: pass


class Sqlite_3(SoftScript):
    def __init__(self):
        try:
            # conectando...
            self.conn = sqlite3.connect('database.db')
            self.cursor = self.conn.cursor()
        except sqlite3.Error:
            print(" --> Erro ao abrir banco.")
            return False
        
    # Salva modificações na db
    def commit_db(self):
        if self.conn:self.conn.commit()
            

    # Fecha conexão com a base de dados
    def close_db(self):
        if self.conn:self.conn.close()

    def sql_scripts(self):

        def write_sql_table(arg):
            table = open(os.path.join('sql', "schema_table.sql"), "a")
            schema_ = "CREATE TABLE IF NOT EXISTS {} (cod INTEGER PRIMARY KEY, data TEXT NOT NULL, hora INTEGER, valor VARCHAR(11) NOT NULl);\n".format(arg)
            table.write(schema_)

        def write_sql_insert(tb_name, name):

            table = open('sql/'+name+'.sql', "w")

            schema_ = "INSERT INTO {} (data, hora, valor) VALUES (?,?,?)".format(tb_name)

            table.write(schema_)

        def write_sql_search(tb_name):
            table = open(os.path.join('sql', 'SEARCH_'+tb_name+'.sql'), "w")
            schema_ = "SELECT cod, data, hora, valor FROM {} WHERE data=?".format(tb_name)
            table.write(schema_)

        def main(arg):
            nome_csv = os.path.basename(arg)[:-4]
            # Substitui espaços por _ para instanciar dentro do sqlite3
            name = nome_csv.replace(" ", "_")
            # Invoca as funções write
            write_sql_table(name)
            write_sql_insert(name, nome_csv)
            write_sql_search(name)

        self.read_directory(main, 'data_csv')

    def sql_insert(self):

        # Cria as tabelas coms os scripts .sql
        def create_tables():
            schemas = open(os.path.join('sql', 'schema_table.sql')).read()
            self.db.cursor.executescript(schemas)

        # Incere os dados do csv na respectiva tabela
        def csv_inject(file):

            # Abrir script Sqlite3
            sqlite_script = open(
                os.path.join('sql', file[:-4]+'.sql'), 'r').read()

            # Abrir arquivo csv
            reader = csv.reader(open(
                os.path.join('data_csv', file), 'rt'), delimiter=',')

            # Executa os camandos sql instanciando os dados do csv.
            [self.db.cursor.execute(sqlite_script, info) for info in reader]
            self.db.commit_db()

        self.db = Sqlite_3()

        create_tables()

        #Looping que chama as funções
        self.read_directory(csv_inject, 'data_csv')

        self.db.close_db()
