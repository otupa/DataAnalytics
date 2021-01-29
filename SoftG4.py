import pandas as pd
import datetime
import sqlite3
import csv
import os
import re

# Diretorio das conversas do whatsapp
dir_conversas = 'conversas/'

# Diretorio dos arquivos csv
dir_csv = 'data_csv/'

# Diretorio dos arquivos sql
dir_sql = 'sql/'

# Lista usada na função SoftG4.filtrar()
data_frame = []


# Trata e salva os dados em csv's
class SoftG4:
    
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
        conversa = open(dir_conversas+file, 'r', encoding = 'utf-8').read().splitlines()

        # Captura o nome que será usado para salvar o arquivo
        nome_csv = os.path.basename(dir_conversas+file)[:-4][25:]

        # Filtra apenas as mensagens com G4 MOBILE.
        data_conversa_mobile = [linha for linha in conversa if 'G4 MOBILE:' in linha]

        # Filtra apenas as mensagens com reais.
        data_conversa_reais = [linha for linha in data_conversa_mobile if 'reais' in linha]

        # Estrutura de laço que invoca a função filtrar.
        [self.filtrar_conversa(str(i)) for i in data_conversa_reais]

        # Cria e salva um DataFrame Pandas em um arquico csv.
        [pd.DataFrame(data_frame).to_csv(dir_csv+nome_csv+'.csv', header=False, encoding='utf-8', index=False)]
        
        #Fecha o DataFrame
        data_frame.clear()

    # Função que execura filtrar() em cada arquivo em dir_conversas
    def main_loop(self):
        [self.filtrar(file) for file in os.listdir(dir_conversas)]

# Conexão e configurações do Sqlite3
class Connect(object):

    def __init__(self, db_name):
        try:
            # conectando...
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()

            # imprimindo nome do banco
            print("Banco:", db_name)

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
class sql_scripts:
        
    # Escreve dentro de um unico arquivo uma tabela com o nome de cada motorista, colunas (data, hora, valor)
    def write_sql_table(self, arg):
        table = open(dir_sql+"schema_table.sql", "a")
        schema_ = "CREATE TABLE {} (data TEXT NOT NULL, hora INTEGER, valor VARCHAR(11) NOT NULl);\n".format(arg)
        table.write(schema_)

    # Escreve em varios arquivo um comando insert para cada motorista 
    def write_sql_insert(self, tb_name, name):
        table = open('sql/'+name+".sql", "w")
        schema_ = "INSERT INTO {} (data, hora, valor) VALUES (?,?,?)".format(tb_name)
        table.write(schema_)

    # Entra no diretorio e retorna o nome dos arquivos
    def loop_dir(self, file):
        nome_csv = os.path.basename(dir_csv+file)[:-4]

        # Substitui espaços por _
        name = nome_csv.replace(" ", "_")

        # Invoca as funções write
        self.write_sql_table(name)
        self.write_sql_insert(name, nome_csv)

    def main_loop(self):

        [os.remove('sql/schema_table.sql')]

        # Para cada .csv em dir_csv aciona loop_dir
        [self.loop_dir(file) for file in os.listdir(dir_csv)]

# Cria as tabelas e incere os arquivos csv na DataBase 
class ClienteDb(object):

    # Conecta a base de dados
    def __init__(self):
        self.db = Connect('BaseG4.db')

    # Fecha a conexão com a base de dados
    def close_connection(self):
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
    
    # Looping principal
    def main_loop(self):
        self.create_tables()
        [self.csv_inject(file) for file in os.listdir('data_csv')]

if __name__ == '__main__':
    SoftG4 = SoftG4()
    SoftG4.main_loop()

    scripts = sql_scripts()
    scripts.main_loop()

    cliente = ClienteDb()
    cliente.main_loop




