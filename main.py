
from SoftScript import *

def iniciar():

    print()

    print(
        "   ##################################",
        "\n",
        "  - - - - - - - SoftG4 - - - - - - -",
        "\n",
        "  ##################################",
        "\n",
        )

if __name__ == '__main__':
    iniciar()
    a = SoftScript()
    a.delete_files()

    b = Sqlite_3()

    a.create_dirs()
    
    a.read_directory(a.extract_archives, "C:\\Users\\User\\Desktop\\so", state=1)

    b.sql_scripts()
    b.sql_insert()
    b.close_db()

    a.delete_files()
