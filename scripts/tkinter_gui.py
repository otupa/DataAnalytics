import os

# Scripts
from scripts.calculating import calculation
from scripts.extract_csv import extract
from scripts.connect_sql import show_tables, search_runs, insert_data, create_sql_table
from scripts.date_genarator import date_generator

# Tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkcalendar import Calendar, DateEntry
from datetime import datetime



class Funcoes():
    def list_motorists(self):
        motorists = show_tables()
        if motorists == []:
            motorists = ["not motorists"]
        return motorists

    def clear_frames(self):
        self.treeview_data_list.delete(
            *self.treeview_data_list.get_children())
        self.treeview_one.delete(
            *self.treeview_one.get_children())

    def insert_treeviw_data(self, result_list):
        [self.treeview_data_list.insert(
            "", END, values=(data[0], data[1], data[2]))
                                for data in result_list]
    
    def insert_treeview_one(self, argument):
        [self.treeview_one.insert(
            "", END, values=(data[0], data[1], data[2], data[3]))
                                            for data in argument]

    def name(self):
        return self.drop_.get()

    def date_one(self):
        return date_generator(self.calendar_1.get())

    def date_two(self):
        return date_generator(self.calendar_2.get())

    def search_sql(self):
        return search_runs(self.name(), self.date_one(), self.date_two())

    def porcents(self):
        return (0.10, -0.90, 0.15, -0.85, 0.20, -0.80)

    def calculation_(self):
        return calculation(self.search_sql(), self.porcents())

    def search_(self):
        self.clear_frames()       
        print(self.calculation_()) 
        self.insert_treeview_one(self.calculation_())
        self.insert_treeviw_data(self.search_sql())

    def search_all():
        pass
        

    def importar(self):
        origem = filedialog.askdirectory()
        extract(origem, 'G4 MOBILE', 'reais')
        create_sql_table()
        insert_data()
        self.list_motorists()
        self.menu_moto()

        
class Application(Funcoes):
    def __init__(self):
        window = Tk()
        self.window = window
        self.tela()
        self.menu_topo()
        self.frames_tela()
        self.textos()
        self.menu_moto()
        self.calendario()
        self.botoes()
        self.treeview_one()
        self.treeview_data()

        window.mainloop()

    def tela(self):
        self.window.title("Soft G4")
        self.window.configure(background='#1e3743')
        self.window.geometry('800x700')
        self.window.resizable(True, True)
        self.window.maxsize(width=800, height=600)
        self.window.minsize(width=500, height=400)

    def window_task():
        self.window.title("Window Task")
        self.window.configure(background='#1e3743')
        self.window.geometry('800x700')
        self.window.resizable(True, True)
        self.window.maxsize(width=800, height=600)
        self.window.minsize(width=500, height=400)

    def menu_topo(self):
        menubar = Menu(self.window, tearoff=0)
        self.window.config(menu=menubar)
        menu_arquivos = Menu(menubar, tearoff=0)
        #menu_ajuda = Menu(menubar, tearoff=0)
        menu_arquivos.add_command(label="Importar", command=self.importar)
        menu_arquivos.add_command(label="Exportar", command=None)
        # menu_arquivos.add_command(label="sair", command=None)
        menubar.add_cascade(label="Arquivo", menu=menu_arquivos)
        #menubar.add_cascade(label="Ajuda", menu=menu_ajuda)

    def frames_tela(self):
        self.frame_1 = Frame(
            self.window, 
            bd=4, bg='#dfe3ee',
            highlightbackground='#759fe6', 
            highlightthickness=3)

        self.frame_2 = Frame(
            self.window, 
            bd=4, bg='#dfe3ee',
            highlightbackground='#759fe6', 
            highlightthickness=3)

        self.frame_1.place(
            relx=0.02, 
            rely=0.02, 
            relwidth=0.96, 
            relheight=0.46)

        self.frame_2.place(
            relx=0.02, 
            rely=0.5, 
            relwidth=0.96, 
            relheight=0.46)

    def menu_moto(self):
        self.options_menu_moto = self.list_motorists()
        self.drop_ = StringVar()
        self.drop_.set("MOTORISTA")

        self.drop = OptionMenu(
            self.frame_1, 
            self.drop_, 
            *self.options_menu_moto)

        self.drop.place(
            relx=0.05, 
            rely = 0.1, 
            relwidth = 0.40, 
            relheight = 0.15)

    def calendario(self):
        self.calendar_1 = DateEntry(
            self.frame_1, 
            width=12, 
            background='#3D51C3', 
            foreground='white', 
            borderwidth=2, 
            font="Arial 12", 
            selectmode='day', 
            cursor="hand1", 
            year=2021, month=1, day=31, 
            date_pattern='dd/mm/Y')

        self.calendar_2 = DateEntry(
            self.frame_1, 
            width=12, 
            background='#3D51C3',
            foreground='white', 
            borderwidth=2, 
            font="Arial 12", 
            selectmode='day', 
            cursor="hand1", 
            year=2021, 
            month=2, day=7,
            date_pattern='dd/mm/Y')

        self.calendar_1.place(
            relx=0.05, 
            rely=0.35, 
            relwidth=0.19, 
            relheight=0.1)

        self.calendar_2.place(
            relx=0.26, 
            rely=0.35, 
            relwidth=0.19, 
            relheight=0.1)

    def botoes(self):
        self.bt_pesquisar = Button(
            self.frame_1, 
            text="PESQUISAR", 
            bd=2, 
            bg='#364094', 
            fg='white', 
            font=('verdana', 10, 'bold'), 
            command=self.search_)

        self.bt_export_pdf = Button(
            self.frame_1, 
            text="EXPORTAR PDF", 
            bd=2, 
            bg='#364094', 
            fg='white', 
            font=('verdana', 8, 'bold'), 
            command=None)

        self.bt_exportar_todos = Button(
            self.frame_1, 
            text="EXPORT ALL", 
            bd=2, 
            bg='#D92A2A', 
            fg='white', 
            font=('verdana', 8, 'bold'), 
            command=None) #self.gerar_analise

        self.bt_pesquisar.place(
            relx=0.05, 
            rely=0.5, 
            relwidth=0.4, 
            relheight=0.2)

        self.bt_export_pdf.place(
            relx=0.05, 
            rely=0.725, 
            relwidth=0.19, 
            relheight=0.15)

        self.bt_exportar_todos.place(
            relx=0.26, 
            rely=0.725, 
            relwidth=0.19, 
            relheight=0.15)

    def textos(self):
        self.lb_motorista = Label(
            self.frame_1, 
            text="Escolha o motorista: ", 
            bg='#dfe3ee', 
            font=('Arial', 10, 'bold'))

        self.lb_resultado = Label(
            self.frame_1, 
            text="Analise dos resultados", 
            bg='#dfe3ee', 
            font=('Arial', 10, 'bold'))

        self.lb_data_inicial = Label(
            self.frame_1, 
            text = "Data inicial:", 
            bg = '#dfe3ee')

        self.lb_data_final = Label(
            self.frame_1, 
            text = "Data final:", 
            bg = '#dfe3ee')

        self.lb_motorista.place(
            relx=0.05, 
            rely=0.005)

        self.lb_resultado.place(
            relx=0.5, 
            rely=0.005)

        self.lb_data_inicial.place(
            relx = 0.05, 
            rely = 0.27)

        self.lb_data_final.place(
            relx = 0.26, 
            rely = 0.27)

    def treeview_one(self):
        self.treeview_one = ttk.Treeview(self.frame_1, height=3, 
            column=("coll1", "coll2", "coll3", "coll4"))

        self.scroll_list = Scrollbar(self.frame_1, orient='vertical', 
            command=self.treeview_one.yview)
        self.treeview_one.configure(yscrollcommand=self.scroll_list.set)

        self.treeview_one.heading("#0", text="")
        self.treeview_one.heading("#1", text="Valores")
        self.treeview_one.heading("#2", text="N° de viajens")
        self.treeview_one.heading("#3", text="Total")
        self.treeview_one.heading("#4", text="Porcentagens")

        self.treeview_one.column("#0", width=0)
        self.treeview_one.column("#1", width=50)
        self.treeview_one.column("#2", width=50)
        self.treeview_one.column("#3", width=75)
        self.treeview_one.column("#4", width=75)
        
        self.treeview_one.place(
            relx=0.50, 
            rely=0.1, 
            relwidth=0.435, 
            relheight=0.85)

        self.scroll_list.place(
            relx=0.93, 
            rely=0.1, 
            relwidth=0.025, 
            relheight=0.85)

    def treeview_data(self):

        self.treeview_data_list = ttk.Treeview(
            self.frame_2, 
            height=2, 
            column=("coll1", "coll2", "coll3"))

        self.scroll_list = Scrollbar(
            self.frame_2, 
            orient='vertical', 
            command=self.treeview_data_list.yview)

        self.treeview_data_list.configure(yscrollcommand=self.scroll_list.set)

        
        self.treeview_data_list.heading("#0", text="")
        self.treeview_data_list.heading("#1", text="date-time")
        self.treeview_data_list.heading("#2", text="valor")
        self.treeview_data_list.heading("#3", text="type")

        self.treeview_data_list.column("#0", width=1)
        self.treeview_data_list.column("#1", width=45)
        self.treeview_data_list.column("#2", width=200)
        self.treeview_data_list.column("#3", width=50)


        self.treeview_data_list.place(
            relx=0.01, 
            rely=0.1, 
            relwidth=0.95, 
            relheight=0.85)

        self.scroll_list.place(
            relx=0.96, 
            rely=0.1, 
            relwidth=0.03, 
            relheight=0.85)
    

         







