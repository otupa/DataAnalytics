from GUI import *
from SoftScript import *

def main():
    soft = SoftScript()
    soft.delete_files()
    soft.create_dirs()

def gui():
    gui = Application()
    gui.Master_window()
    gui.Frames_window()

    gui.Treeview_frame_1()
    gui.Treeview_frame_2()

    gui.Menu_top()
    gui.Labels()
    gui.Menu_moto()
    gui.Calendar()
    gui.Buttons()

    gui.window.mainloop()

if __name__ == '__main__':
    main()
    gui()



    
