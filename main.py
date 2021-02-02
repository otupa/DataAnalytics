import pandas as pd

import datetime
import sqlite3
import csv
import os
import re


[os.remove('BaseG4.db')]

# Diretorio das conversas do whatsapp
dir_conversas = 'conversas/'

# Diretorio dos arquivos csv
dir_csv = 'data_csv/'

# Diretorio dos arquivos sql
dir_sql = 'sql/'

# Trata e salva os dados em csv's
class SoftG4:
    
    def __init__(self):


        # Lista usada na função SoftG4.filtrar()
        self.data_frame = []

        # Looping principal da classe
        [self.filtrar(file) for file in os.listdir(dir_conversas)]

    # Função usada para filtrar e tratar as informações.
    def filtrar_conversa(self, arg):

        # Separa apenas as informações desejadas
        r = [re.findall(r"\d+/\d+/\d+", arg), 
            re.findall(r"\d+\:\d+", arg), 
            re.findall(r"\d+\sreais", arg)]

        # Remove caracteres indesejados
        for i, j in enumerate(r):
            r[i] = j[0].replace(',','[').replace('!',']').replace('.','') 

        # Incere os dados em uma lista usada pelo Pandas
        data_frame.append(r)

    def filtrar(self, file):
        
        # Abre a conversa e cria uma lista que separa cada linha.
        conversa = open(dir_conversas+file, 'r', 
            encoding = 'utf-8').read().splitlines()

        # Captura o nome que será usado para salvar o arquivo
        nome_csv = os.path.basename(dir_conversas+file)[:-4][25:]

        # Filtra apenas as mensagens com G4 MOBILE.
        data_conversa_mobile = [linha for linha in conversa if 'G4 MOBILE:' in linha]

        # Filtra apenas as mensagens com reais.
        data_conversa_reais = [linha for linha in data_conversa_mobile if 'reais' in linha]

        # Estrutura de laço que invoca a função filtrar.
        [self.filtrar_conversa(str(i)) for i in data_conversa_reais]

        # Cria e salva um DataFrame Pandas em um arquico csv.
        [pd.DataFrame(self.data_frame).to_csv(dir_csv+nome_csv+'.csv', header=False, encoding='utf-8', index=False)]
        
        #Fecha o DataFrame
        self.data_frame.clear()

# Conexão e configurações do Sqlite3
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
            print("SQLite version: %s" % self.data)

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

# Esvreve os scripts para gerenciamento do DataBase
class Sql_scripts:
    def __init__(self):

        [os.remove('sql/schema_table.sql')]

        # Para cada .csv em dir_csv aciona loop_dir
        for file in os.listdir(dir_csv):
            nome_csv = os.path.basename(dir_csv+file)[:-4]

            # Substitui espaços por _ para instanciar dentro do sqlite3
            name = nome_csv.replace(" ", "_")

            # Invoca as funções write
            self.write_sql_table(name)
            self.write_sql_insert(name, nome_csv)
            self.write_sql_search(name)
        
    # Escreve dentro de um unico arquivo uma tabela com o nome de cada motorista, colunas (data, hora, valor)
    def write_sql_table(self, arg):
        table = open(dir_sql+"schema_table.sql", "a")
        schema_ = "CREATE TABLE {} (cod INTEGER PRIMARY KEY, data TEXT NOT NULL, hora INTEGER, valor VARCHAR(11) NOT NULl);\n".format(arg)
        table.write(schema_)

    # Escreve em varios arquivo um comando insert para cada motorista 
    def write_sql_insert(self, tb_name, name):

        table = open('sql/'+name+".sql", "w")

        schema_ = "INSERT INTO {} (data, hora, valor) VALUES (?,?,?)".format(tb_name)

        table.write(schema_)

    def write_sql_search(self, tb_name):

        table = open('sql/SEARCH_'+tb_name+'.sql', "w")

        schema_ = "SELECT cod, data, hora, valor FROM {} WHERE data=?".format(tb_name)

        table.write(schema_)
 

# Cria as tabelas e incere os arquivos csv na DataBase 
class Sql_insert(object):

    
    def __init__(self):

        # Conecta a base de dados
        self.db = Connect()

        self.create_tables()

        #Looping que chama as funções
        [self.csv_inject(file) for file in os.listdir('data_csv')]

        self.db.close_db()

    # Cria as tabelas coms os scripts .sql
    def create_tables(self):
        schemas = open('sql/schema_table.sql').read()
        self.db.cursor.executescript(schemas)

    # Incere os dados do csv na respectiva tabela
    def csv_inject(self, arg):

        # Captura o nome do arquivo
        name_csv = os.path.basename(dir_csv+arg)[:-4]

        # Abrir script Sqlite3
        x = open('sql/'+name_csv+'.sql', 'r').read()

        # Abrir arquivo csv
        reader = csv.reader(open(dir_csv+name_csv+'.csv', 'rt'), delimiter=',')

        # Executa os camandos sql instanciando os dados do csv.
        [self.db.cursor.execute(x, linha) for linha in reader]
        self.db.commit_db()


