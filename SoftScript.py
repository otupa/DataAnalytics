import shutil
import sqlite3
import pandas as pd
import os
import re




class SoftScript():
    def __init__(self):

        self.data_frame = []

        self.delete_files()
        self.create_dirs()
        
        a = self.read_directory(self.extract_archives, "C:\\Users\\User\\Desktop\\so")

        
        #self.delete_files()


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


    def read_directory(self, func, directory):
        for i in os.listdir(directory):
            func(i, directory)


    def create_dirs(self):
        os.mkdir('data_csv') if True else None
        os.mkdir('sql') if True else None


    def delete_files(self):
        shutil.rmtree('data_csv', ignore_errors=True, onerror=None)
        shutil.rmtree('sql', ignore_errors=True, onerror=None)
        try: os.remove('BaseG4.db')
        except: True