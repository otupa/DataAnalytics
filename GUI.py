import SoftG4 as G4

# Tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry



window = Tk()

class Funcoes():
    def limpar(self):
        self.lb_codigo_entry.delete(0, END)
        self.lb_nome_entry.delete(0, END)
        self.lb_telefone_entry.delete(0, END)
        self.lb_cidade_entry.delete(0, END)

class Application(Funcoes):

    def __init__(self):
        self.window = window
        self.tela()
        self.frames_tela()
        self.widgets_frame_1()
        self.list_frame_2()
        window.mainloop()

    def tela(self):
        self.window.title("Soft G4")
        self.window.configure(background='#1e3743')
        self.window.geometry('700x500')
        self.window.resizable(True, True)
        self.window.maxsize(width=800, height=600)
        self.window.minsize(width=500, height=400)

    def frames_tela(self):

        # Criando Frames
        self.frame_1 = Frame(self.window, bd=4, bg='#dfe3ee',
            highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2 = Frame(self.window, bd=4, bg='#dfe3ee',
            highlightbackground='#759fe6', highlightthickness=3)

        # Empacotando Frames de forma responsiva
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

    def widgets_frame_1(self):

        # Labels e entrada do codigo
        self.lb_codigo = Label(self.frame_1, text="Código", bg='#dfe3ee')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.lb_codigo_entry = Entry(self.frame_1)
        self.lb_codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        # Label e entrada do nome
        self.lb_nome = Label(self.frame_1, text="nome", bg='#dfe3ee')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.lb_nome_entry = Entry(self.frame_1)
        self.lb_nome_entry.place(relx=0.05, rely=0.45, relwidth=0.80)

        # Label e entrada do telefone  
        self.lb_telefone = Label(self.frame_1, text="telefone", bg='#dfe3ee')
        self.lb_telefone.place(relx=0.05, rely=0.55)

        self.lb_telefone_entry = Entry(self.frame_1)
        self.lb_telefone_entry.place(relx=0.05, rely=0.65, relwidth=0.25)

        # Label e entrada do cidade
        self.lb_cidade = Label(self.frame_1, text="cidade", bg='#dfe3ee')
        self.lb_cidade.place(relx=0.35, rely=0.55)

        self.lb_cidade_entry = Entry(self.frame_1)
        self.lb_cidade_entry.place(relx=0.35, rely=0.65, relwidth=0.5)

        # Botão limpar
        self.bt_limpar = Button(self.frame_1, text="limpar", bd=2, bg='#76BCDD', 
            fg='white', font=('verdana', 7, 'bold'), command=self.limpar)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão buscar
        self.bt_buscar = Button(self.frame_1, text="buscar", bd=2, bg='#76BCDD', 
            fg='white', font=('verdana', 7, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão novo
        self.bt_novo = Button(self.frame_1, text="novo", bd=2, bg='#76BCDD', 
            fg='white', font=('verdana', 7, 'bold'))
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão alterar
        self.bt_alterar = Button(self.frame_1, text="alterar", bd=2, bg='#76BCDD', 
            fg='white', font=('verdana', 7, 'bold'))
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão apagar
        self.bt_apagar = Button(self.frame_1, text="apagar", bd=2, bg='#76BCDD', 
            fg='white', font=('verdana', 7, 'bold'))
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

    def list_frame_2(self):

        self.scroll_list = Scrollbar(self.frame_2, orient='vertical')
        
        self.listaCli = ttk.Treeview(self.frame_2, height=3, column=("coll1", "coll2", "coll3", "coll4"), yscroll=self.scroll_list)
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")


        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        self.scroll_list.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)











Application()




