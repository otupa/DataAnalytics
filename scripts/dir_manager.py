import shutil
import os

def create_dirs():
    try:
        os.makedirs("data_csv")
        os.makedirs("sql")
        os.makedirs("sql/search/")
        os.makedirs("sql/insert/")
        #os.makedirs("")
    except: pass

def rm_dirs():
    shutil.rmtree("data_csv")
    shutil.rmtree("sql")