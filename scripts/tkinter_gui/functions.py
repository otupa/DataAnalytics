
import tkinter as tk

from datetime import datetime, date
from json_config import ConfigJson
from connect_sql import show_tables
from calculating import calculate

def date_generator(argument):
    date_ = datetime.strptime(argument, '%d/%m/%Y').date()
    return str(date_)+" 00:00:00"

class TkListBox(ConfigJson):
    def __init__(self):
        self.config = ConfigJson()

    def insert_listbox(self, listbox_left, listbox_right):
        self.config.loopModMotorists(show_tables())
        motorists = self.config.getMoto()
        for item in motorists:
            if item[1] == 0:
                listbox_left.insert(tk.END, item[0])
            elif item[1] == 1:
                listbox_right.insert(tk.END, item[0])
    
    def move_listbox(self, listbox_left, listbox_right, state):
        if state == 0:
            indice = listbox_left.curselection()[0]
            name = listbox_left.get(indice)
            listbox_right.insert(tk.END, name)
            listbox_left.delete(indice)
            self.config.modMotorist(name, 1)

        elif state == 1:
            indice = listbox_right.curselection()[0]
            name = listbox_right.get(indice)
            listbox_left.insert(tk.END, name)
            listbox_right.delete(indice)
            self.config.modMotorist(name, 0)
        else: return False

    def list_moto(self):
        data = self.config.get_json_records()
        list_ = [item[0] for item in data]
        if list_ == []: list_ = ["not motorists"]
        return list_

    def insert_treeview(self, argument, state):
        if state == 0:
            self.dataTreeview.delete(
                *self.dataTreeview.get_children())
            [self.dataTreeview.insert(
                "", END, values=(data[0], data[1], data[2]))
                                    for data in argument]
        elif state == 1:
            self.dataTreeview.delete(
                *self.dataTreeview.get_children())
            [self.dataTreeview.insert(
                "", END, values=(data[0], data[1], data[2], data[3]))
                                                for data in argument]

    def pick_date(self, argument):
        if argument == 0:
            return date_generator(self.leftCalendar.get())
        elif argument == 1:
            return date_generator(self.rightCalendar.get())

    def porcents(self):
        return (0.10, -0.90, 0.15, -0.85, 0.20, -0.80)
        
    def search_(self, name, initial_date, final_date):
        list_ = self.search_runs(name, initial_date, final_date)
        dict_ = calculate(list_, self.porcents())
        self.insert_treeview(list_, 0)
        self.insert_treeview(dict_, 1)

    def export_pdf(self):
        save_pdf(
            self.calculate(self.dropMenu.get()), 
            self.pick_date(0), 
            self.pick_date(1), 
            filedialog.askdirectory())   

    def export_all(self):
        for table in self.listMoto():
            save_pdf(
                self.calculate_(table), 
                self.pick_date(0), 
                self.pick_date(1), 
                filedialog.askdirectory())      
                
    def importar(self):
        extract(filedialog.askdirectory(), 'G4 MOBILE', 'reais')
        create_sql_table()
        insert_data()
        self.listMoto()