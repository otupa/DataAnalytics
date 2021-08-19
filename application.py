from scripts.dir_manager import create_dirs, remove_dirs
from scripts.extract_csv import extract
from scripts.write_sql import write
from scripts.insert_sqlite import csv_inject

# directory_talks = input()

if __name__ == '__main__':
    remove_dirs()
    create_dirs()
    print("Diretorios criados")
    extract('dados', 'G4 MOBILE', 'reais')
    write()
    input()
    csv_inject()
    remove_dirs()

