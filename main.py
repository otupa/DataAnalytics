import pandas as pd

from datetime import datetime, date, timedelta

import sqlite3
import csv
import os
import re

try:
    [os.remove('sql/schema_table.sql')]
    [os.remove('BaseG4.db')]
except:
    True

# Diretorio das conversas do whatsapp
dir_conversas = 'conversas/'

# Diretorio dos arquivos csv
dir_csv = 'data_csv/'

# Diretorio dos arquivos sql
dir_sql = 'sql/'

# Trata e salva os dados em csv's
class SoftG4():
    
    def extract_csv(self):
        self.data_frame = []

        def filtrar(arg):

            # Separa apenas as informações desejadas
            data = re.findall(r"\d+/\d+/\d+", arg)
            hora = re.findall(r"\d+\:\d+", arg)
            valor = re.findall(r"\d+\sreais", arg)
            r = [data, hora, valor]

            # Remove caracteres indesejados
            try:
                for i, j in enumerate(r):
                    r[i] = j[0].replace(',','[').replace('!',']').replace('.','')
            except Exception as e:
                print('Erro inesperado ao filtrar conversa: ', e)
                print(r)
                return True

            # Incere os dados em uma lista usada pelo Pandas
            self.data_frame.append(r)

        def extrair(file):
            # Abre a conversa e cria uma lista que separa cada linha.
            conversa = open(dir_conversas+file, 'r', 
                encoding = 'utf-8').read().splitlines()

            # Captura o nome que será usado para salvar o arquivo
            nome_csv = os.path.basename(dir_conversas+file)[:-4][25:]

            print("Analisando: ", nome_csv)

            # Filtra apenas as mensagens com G4 MOBILE.
            data_conversa_mobile = [linha for linha in conversa if 'G4 MOBILE:' in linha]

            # Filtra apenas as mensagens com reais.
            data_conversa_reais = [linha for linha in data_conversa_mobile if 'reais' in linha]

            # Estrutura de laço que invoca a função filtrar.
            [filtrar(str(i)) for i in data_conversa_reais]

            # Cria e salva um DataFrame Pandas em um arquico csv.
            [pd.DataFrame(self.data_frame).to_csv(dir_csv+nome_csv+'.csv', header=False, encoding='utf-8', index=False)]
            
            #Fecha o DataFrame
            self.data_frame.clear()

        [extrair(file) for file in os.listdir(dir_conversas)]

        print()

    def Sql_scripts(self):

        def write_sql_table(arg):
            table = open(dir_sql+"schema_table.sql", "a")
            schema_ = "CREATE TABLE {} (cod INTEGER PRIMARY KEY, data TEXT NOT NULL, hora INTEGER, valor VARCHAR(11) NOT NULl);\n".format(arg)
            table.write(schema_)

        def write_sql_insert(tb_name, name):

            table = open('sql/'+name+".sql", "w")

            schema_ = "INSERT INTO {} (data, hora, valor) VALUES (?,?,?)".format(tb_name)

            table.write(schema_)

        def write_sql_search(tb_name):

            table = open('sql/SEARCH_'+tb_name+'.sql', "w")

            schema_ = "SELECT cod, data, hora, valor FROM {} WHERE data=?".format(tb_name)

            table.write(schema_)

            

        # Para cada .csv em dir_csv aciona loop_dir
        for file in os.listdir(dir_csv):
            nome_csv = os.path.basename(dir_csv+file)[:-4]

            # Substitui espaços por _ para instanciar dentro do sqlite3
            name = nome_csv.replace(" ", "_")

            # Invoca as funções write
            write_sql_table(name)
            write_sql_insert(name, nome_csv)
            write_sql_search(name)

    def Sql_insert(self):

        # Cria as tabelas coms os scripts .sql
        def create_tables():
            schemas = open('sql/schema_table.sql').read()
            self.db.cursor.executescript(schemas)

        # Incere os dados do csv na respectiva tabela
        def csv_inject(arg):

            # Captura o nome do arquivo
            name_csv = os.path.basename(dir_csv+arg)[:-4]

            # Abrir script Sqlite3
            x = open('sql/'+name_csv+'.sql', 'r').read()

            # Abrir arquivo csv
            reader = csv.reader(open(dir_csv+name_csv+'.csv', 'rt'), delimiter=',')

            # Executa os camandos sql instanciando os dados do csv.
            [self.db.cursor.execute(x, linha) for linha in reader]
            self.db.commit_db()

        self.db = Connect()

        create_tables()

        #Looping que chama as funções
        [csv_inject(file) for file in os.listdir('data_csv')]

        self.db.close_db()

    def date_generator(self, data, data_final):

        data_dd = data[:2]
        data_dd = int(data_dd)

        data_mm = data[3:]
        data_mm = data_mm[:2]
        data_mm = int(data_mm)

        data_yy = data[6:]
        data_yy = int(data_yy)

        data_final_dd = data_final[:2]
        data_final_dd = int(data_final_dd)

        data_final_mm = data_final[3:]
        data_final_mm = data_final_mm[:2]
        data_final_mm = int(data_final_mm)

        data_final_yy = data_final[6:]
        data_final_yy = int(data_final_yy)


        data_inicio = date(data_yy, data_mm, data_dd)

        data_fim = date(data_final_yy, data_final_mm, data_final_dd)

        delta = data_fim - data_inicio

        lista_datas = []

        for i in range(delta.days + 1):
            day = data_inicio + timedelta(days=i)
            lista_datas.append(day.strftime('%d/%m/%y'))

        return lista_datas


class Connect():

    def __init__(self):

        try:
            # conectando...
            self.conn = sqlite3.connect('BaseG4.db')
            self.cursor = self.conn.cursor()

            # imprimindo nome do banco
            print("Banco:", 'BaseG4.db')

            # lendo a versão do SQLite
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()

            # imprimindo a versão do SQLite
            print("SQLite version: %s" % self.data, "\n")

        except sqlite3.Error:
            print("Erro ao abrir banco.")
            return False
        
    # Salva modificações na db
    def commit_db(self):
        if self.conn:
            self.conn.commit()

    # Fecha conexão com a base de dados
    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")


