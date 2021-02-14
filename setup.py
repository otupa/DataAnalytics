from cx_Freeze import setup, Executable
import sys



base = "Win32GUI"    

# Permite que sejá executado em diversas versoes do windows
#if sys.platform == "win32":
#    base = "Win32GUI"

# Arquivo para criar executavel
executables = [Executable("main.pyw", base=base), icon="icon.ico"]

# Bibliotecas do programa
packages = ["tkinter", "tkcalendar", "pandas", "sqlite3"]

# Arquivos nescessarios
files = ['SoftBackend.pyw', 'GUI.pyw']

# Opções do cx_Freeze
options = {
    # Construir o programa 
    'build_exe': {    

        # Bibliotecas
        'packages':packages,

        # Arqiovos
        'include_files':files,

        # Incluir Microsoft Visual Studio 
        "include_msvcr": True, 

    },    
}

# Configurações do ch_Freeze
setup(
    # Nome do programa
    name = "SoftG4",

    # Opções
    options = options,

    # Versão
    version = "BETE 1.0",

    # Descrição
    description = 'Softwere de genrenciamento de corridas de aplicativo',
    
    # Configurações do arquivo executavel
    executables = executables 
    )