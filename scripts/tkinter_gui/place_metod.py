''' Place Object in Frame Tkinter '''

from tkinter import Tk

class PlaceMethod():
    ''' Adapter For Place Tkinter '''
    def __init__(self, object_class, component, method, relx, rely, relwidth, relheight):
        ''' Construct objects to place '''
        self.component =  
        self.component = component

        self.relx = relx
        self.rely = rely
        self.relwidth = relwidth
        self.relheight = relheight
    
    def place_in(self):
        self.component.method(
            self.relx,
            self.rely,
            self.relwid
        )

if __name__ == '__main__':
    app = Tk()