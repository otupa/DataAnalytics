from main import *

# Tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry



window = Tk()

class Funcoes():

    def list_moto(self):
        list_ = []
        arquivos = os.listdir('data_csv/')
        [list_.append(str(i)[:-4].replace(" ", "_")) for i in arquivos]
        return list_

    # Backend Data Screpping e Criação do banco de dados
    def data_screrping(self):
        #Extrai as conversas do whatsapp
        self.SoftG4 = SoftG4()
        # Cria os scripts sql
        self.scripts = Sql_scripts()
        # Aloca os dados do Banco de dados
        self.cliente = Sql_insert()

    # Conectar ao banco de dados
    def connect_sql(self):
        self.connect = Connect()
        return True

    # desconectar do banco de dados
    def disconect_sql(self):
        self.connect.close_db()
        return True

    # Selecionar tabela
    def select_tb(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.connect_sql()
        lista = self.connect.cursor.execute(""" SELECT cod, data, hora, valor FROM MOT_CARLOS_HONDA_AMARELO """)
        i=0
        for info in lista:
            print(info)
            self.listaCli.insert("", END, values=info)
        self.disconect_sql()

    # recebe a string do dropdawn
    def drop_data(self, selection):
        print(selection)
        return True
        

class Application(Funcoes):

    def __init__(self):
        self.data_screrping()
        self.window = window

        self.tela()
        self.frames_tela()
        self.textos()
        self.menu_moto()
        self.calendario()
        self.botoes()
        self.Treeview_frame_1()
        self.Treeview_frame_2()
        self.select_tb()

        window.mainloop()

    def tela(self):
        self.window.title("Soft G4")
        self.window.configure(background='#1e3743')
        self.window.geometry('700x500')
        self.window.resizable(True, True)
        self.window.maxsize(width=800, height=600)
        self.window.minsize(width=500, height=400)

    def frames_tela(self):

        # Frame que exibe as funções
        self.frame_1 = Frame(
            self.window, 
            bd=4, 
            bg='#dfe3ee',
            highlightbackground='#759fe6', 
            highlightthickness=3
            )

        # Frame que exibe o banco de dados
        self.frame_2 = Frame(
            self.window, 
            bd=4, 
            bg='#dfe3ee',
            highlightbackground='#759fe6', 
            highlightthickness=3
            )

        # Empacotando de forma responsiva
        self.frame_1.place(
            relx=0.02, 
            rely=0.02, 
            relwidth=0.96,
            relheight=0.46
            )

        # Empacotando de forma responsiva
        self.frame_2.place(
            relx=0.02, 
            rely=0.5, 
            relwidth=0.96, 
            relheight=0.46
            )

    def menu_moto(self):

        options = self.list_moto()

        self.drop_ = StringVar()

        self.drop_.set("MOTORISTA")

        self.drop = OptionMenu(self.frame_1, self.drop_, *options, command=self.drop_data)

        self.drop.place(relx=0.05, rely = 0.1, relwidth = 0.40, relheight = 0.15)

    def calendario(self):
        
        # Criando calendario
        self.calendar_1 = DateEntry(self.frame_1, width=12, background='#3D51C3', foreground='white', 
            borderwidth=2, font="Arial 12", selectmode='day', cursor="hand1", year=2020, month=2, day=5)

        self.calendar_2 = DateEntry(self.frame_1, width=12, background='#3D51C3',foreground='white', 
            borderwidth=2, font="Arial 12", selectmode='day', cursor="hand1", year=2020, month=2, day=5)

        self.calendar_1.place(relx=0.05, rely=0.35, relwidth=0.19, relheight=0.1)

        self.calendar_2.place(relx=0.26, rely=0.35, relwidth=0.19, relheight=0.1)

    def botoes(self):

        self.bt_pesquisar = Button(self.frame_1, text="PESQUISAR", bd=2, 
            bg='#364094', fg='white', font=('verdana', 10, 'bold'), command=None)

        self.bt_export_pdf = Button(self.frame_1, text="EXPORTAR PDF", bd=2, 
            bg='#364094', fg='white', font=('verdana', 8, 'bold'), command=None)

        self.bt_exportar_todos = Button(self.frame_1, text="EXPORTAR TUDO", bd=2, 
            bg='#D92A2A', fg='white', font=('verdana', 8, 'bold'), command=None)

        self.bt_pesquisar.place(relx=0.05, rely=0.5, relwidth=0.4, relheight=0.2)

        self.bt_export_pdf.place(relx=0.05, rely=0.725, relwidth=0.19, relheight=0.15)

        self.bt_exportar_todos.place(relx=0.26, rely=0.725, relwidth=0.19, relheight=0.15)

    def textos(self):

        self.lb_motorista = Label(self.frame_1, text="Escolha o motorista: ", bg='#dfe3ee', font=('Arial', 10, 'bold'))

        self.lb_resultado = Label(self.frame_1, text="Analise dos resultados", bg='#dfe3ee', font=('Arial', 10, 'bold'))

        self.lb_data_inicial = Label(self.frame_1, text = "Data inicial:", bg = '#dfe3ee')

        self.lb_data_final = Label(self.frame_1, text = "Data final:", bg = '#dfe3ee')


        self.lb_motorista.place(relx=0.05, rely=0.005)

        self.lb_resultado.place(relx=0.5, rely=0.005)

        self.lb_data_inicial.place(relx = 0.05, rely = 0.27)

        self.lb_data_final.place(relx = 0.26, rely = 0.27)

    def Treeview_frame_1(self):
        self.Resultado = ttk.Treeview(self.frame_1)
        
        self.Resultado.place(relx=0.50, rely=0.1, relwidth=0.435, relheight=0.785)

    def Treeview_frame_2(self):

        self.listaCli = ttk.Treeview(self.frame_2, height=3, 
            column=("coll1", "coll2", "coll3", "coll4"))

        self.scroll_list = Scrollbar(self.frame_2, orient='vertical', command=self.listaCli.yview)

        self.listaCli.configure(yscrollcommand=self.scroll_list.set)

        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="cod")
        self.listaCli.heading("#2", text="data")
        self.listaCli.heading("#3", text="hora")
        self.listaCli.heading("#4", text="valor")

        self.listaCli.column("#0", width=0)
        self.listaCli.column("#1", width=10)
        self.listaCli.column("#2", width=45)
        self.listaCli.column("#3", width=45)
        self.listaCli.column("#4", width=45)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroll_list.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)


a = Application()



