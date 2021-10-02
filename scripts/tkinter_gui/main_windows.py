from tkinter import Tk



class ClasseEx():
    ''' class exemple'''
    
    def test():
        return 'ok'


class Application(ClasseEx):
    '''Render UI
    :param - ClasseEx: class with functions of UI
    '''
    def __init__(self):
        self.window = Tk()
        self.window.title("Soft G4")
        self.window.configure(background='#1e3743')
        self.window.geometry('1000x600')
        self.window.resizable(True, True)
        self.window.mainloop()