from scripts.dir_manager import create_dirs, remove_dirs
from scripts.write_sql import write
from scripts.tkinter_gui import Application
# directory_talks = input()

if __name__ == '__main__':
    remove_dirs()
    create_dirs()
    Application()
    write()
    remove_dirs()

