from SoftScript import *
import pathlib
from math import ceil
# Tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkcalendar import Calendar, DateEntry
from datetime import datetime



class Connections:

    def start_extract(self):

        self.directory = filedialog.askdirectory()

        self.backend.read_directory(self.backend.extract_archives, self.directory, state=1)

        self.database.sql_scripts()

        self.database.sql_insert()

        self.Menu_moto()

    def search_all(self):

        self.data_1 = self.calendar_one.get()
        self.data_2 = self.calendar_two.get()

        dates = self.backend.date_generator(self.data_1, self.data_2)

        destiny = filedialog.askdirectory()

        try:
            for file in os.listdir('data_csv'):

                nome = file[:-4].replace(" ", "_")

                paterns = "{}".format(nome), str(self.data_1), str(self.data_2), " "

                [self.select_tb(nome, date) for date in dates]

                result = self.calculate_runs(self.calc_)

                result.insert(0, paterns)

                result.insert(1, ("Valor","N viajens","total","Porcentagem"))

                local = os.path.join(destiny, nome+'.csv')

                [pd.DataFrame(result).to_csv(local, header=False, encoding='utf-8', index=False)]

                self.calc_.clear()

            self.Result_db_serch.delete(*self.Result_db_serch.get_children())
            self.Resultado.delete(*self.Resultado.get_children())

        except Exception as error:
            print("error: ", error)


    def search(self):

        self.calc_.clear()

        self.Result_db_serch.delete(*self.Result_db_serch.get_children())
        self.Resultado.delete(*self.Resultado.get_children())

        self.date_one = self.calendar_one.get()
        self.date_two = self.calendar_two.get()

        name = self.drop_.get()

        dates = self.backend.date_generator(self.date_one, self.date_two)

        [self.select_tb(name, date) for date in dates]

        self.calculate_runs(self.calc_)

    def connect_sql(self): self.connect = Sqlite_3()

    def select_tb(self, nome_moto, data):
        
        self.connect_sql()

        schema = open('sql/SEARCH_'+nome_moto+'.sql').read()

        lista_treeview = self.connect.cursor.execute(schema, (data,))

        [self.Result_db_serch.insert("", END, values=info) for info in lista_treeview]

        lista = self.connect.cursor.execute(schema, (data,))

        for i in lista:
            self.calc_.append(i)
    
        self.connect.close_db()

    def calculate_runs(self , lista):
        # Lista que recebe o conteudo do Treeview
        master_list = []

        # Total de viajens
        total_runs = []

        # Lista que recebe o valor de cada viajem
        moto_runs = []

        # Porcrntagem paga pelo motorista
        moto_porcent = []
        
        def recive_search():
            result_list = []
            [result_list.append(item[3]) for item in lista if item[3][:1] == "R"]
            return result_list

        def recive_desc_search():
            descont_list = []
            [descont_list.append(item[3]) for item in lista if item[3][:1] == "D"]
            return descont_list

        def valor_variant():
            valor_list = []
            [valor_list.append(item) for item in recive_search() if item not in valor_list]
            valor_list = sorted(valor_list)
            return valor_list

        def valor_variant_desc():
            desc_valor_list = []
            [desc_valor_list.append(item) for item in recive_desc_search() if item not in desc_valor_list]    
            desc_valor_list = sorted(desc_valor_list)
            return desc_valor_list

        def calc_porcent(p_valor, p_total):
            p_valor = int(p_valor[2:][:-3])
            
            if p_valor == 10:
                porcent = p_total * 0.10
                porcent = round(porcent, 2)
                return porcent

            elif p_valor <= 19:
                porcent = p_total * 0.15
                porcent = round(porcent, 2)
                return porcent

            elif p_valor >= 20:
                porcent = p_total * 0.20
                porcent = round(porcent, 2)
                return porcent

        def calc_desc_porcent(p_valor, p_total):

            p_valor = int(p_valor[3:][:-3])

            if p_valor == 10:
                porcent = p_total * -0.90
                porcent = round(porcent, 2)
                return porcent
            
            elif p_valor <= 19:
                porcent = p_total * -0.85
                porcent = round(porcent, 2)
                return porcent

            elif p_valor >= 20:
                porcent = p_total * -0.80
                porcent = round(porcent, 2)
                return porcent

        def mult(valor, amount):
            total_mult = int(valor[2:][:-3]) * amount
            return total_mult

        def mult_desc(valor, amount):
            total_mult = int(valor[3:][:-3]) * amount
            return total_mult

        def schema_pesquisa():
            # Percorre a lista valor calculando o que será exibido no  Treview do tkinter 
            for valor in valor_variant():

                # Conta a quantidade de viajens
                amount_runs = recive_search().count(valor)

                total_runs.append(amount_runs)

                # Multiplicando o valor pela quantidade de viajens
                mult_total = mult(valor, amount_runs)
                
                # Soma ao valor total
                moto_runs.append(mult_total)

                # Calcula a porcentagem para cada valor
                porcenting = calc_porcent(valor, mult_total)

                moto_porcent.append(porcenting)

                # Esquema que será exibido no Treview do tkinter 
                schema = [
                    valor,                                  # valor
                    "x "+str(amount_runs)+"  =",     # quantidade de vianjens
                    "R$"+str(mult_total)+",00",             # valor total das viajens
                    "R$"+str(porcenting)                   # porcentagem da empresa
                    ]

                master_list.append(schema)

        def schema_search_desc():
            # Percorre a lista valor calculando o que será exibido no  Treview do tkinter 
            for valor in valor_variant_desc():

                # Conta a quantidade de viajens
                amount_runs = recive_desc_search().count(valor)

                total_runs.append(amount_runs)

                # Multiplicando o valor pela quantidade de viajens
                mult_total = mult_desc(valor, amount_runs)
                
                # Soma ao valor total
                moto_runs.append(mult_total)

                # Calcula a porcentagem para cada valor
                porcent_desc = calc_desc_porcent(valor, mult_total)

                moto_porcent.append(porcent_desc)

                # Esquema que será exibido no Treview do tkinter 
                schema = [
                    valor,                                  # valor
                    "x "+str(amount_runs)+"  =",            # quantidade de vianjens
                    "R$"+str(mult_total)+",00",             # valor total das viajens
                    "R$"+str(porcent_desc)              # porcentagem da empresa
                    ]

                master_list.append(schema)

        def schema_search_total():

            # Soma o valor total do lucro da empresa
            sum_total_runs = sum(moto_runs)

            # Insere na lista principal o esquema com:
            master_list.append([
                "Total:",                                       #
                "x "+str(sum(total_runs)),                   # total de viajens
                "R$"+str(sum_total_runs)+",00",             # total faturada pelo motorista
                "R$"+str(round(sum(moto_porcent), 2))                            # total da porcentagem da empresa
                ])

        def main():
            schema_pesquisa()
            schema_search_desc()
            schema_search_total()
            [self.Resultado.insert("", END, values=info) for info in master_list]

        main()
        return master_list


class Application(Connections):
    def __init__(self):
        self.calc_ = []

        self.window = window = Tk()

        self.backend = SoftScript()
        self.database = Sqlite_3()

        self.backend.delete_files()
        self.backend.create_dirs()

        self.Master_window()
        self.Frames_window()

        self.Treeview_frame_1()
        self.Treeview_frame_2()

        self.Menu_top()
        self.Labels()
        self.Menu_moto()
        self.Calendar()
        self.Buttons()

        self.window.mainloop()

        self.database.close_db()
        self.backend.delete_files()


    def Master_window(self):
        self.window.title("Soft G4")
        self.window.configure(background='#1e3743')
        self.window.geometry('800x700')
        self.window.resizable(True, True)
        self.window.maxsize(width=800, height=600)
        self.window.minsize(width=500, height=400)


    def Menu_top(self):

        menubar = Menu(self.window, tearoff=0)

        self.window.config(menu=menubar)

        menu_arquivos = Menu(menubar, tearoff=0)
        menu_ajuda = Menu(menubar, tearoff=0)

        menu_arquivos.add_command(label="Importar", command=self.start_extract)
        menu_arquivos.add_command(label="Exportar", command=None)
        menu_arquivos.add_command(label="sair", command=None)

        menubar.add_cascade(label="Arquivo", menu=menu_arquivos)
        menubar.add_cascade(label="Ajuda", menu=menu_ajuda)


    def Frames_window(self):

        self.frame_1 = Frame(self.window, bd=4, bg='#dfe3ee',
            highlightbackground='#759fe6', highlightthickness=3)

        self.frame_2 = Frame(self.window, bd=4, bg='#dfe3ee',
            highlightbackground='#759fe6', highlightthickness=3)

        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96,relheight=0.46)

        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)


    def Menu_moto(self):

        def list_moto():
            list_ = [""]
            directory = os.listdir('data_csv/')
            [list_.append(str(i)[:-4].replace(" ", "_")) for i in directory]
            return list_

        self.options_menu_moto = list_moto()

        self.drop_ = StringVar()

        self.drop_.set("MOTORISTA")

        self.drop = OptionMenu(self.frame_1, self.drop_, *self.options_menu_moto)

        self.drop.place(relx=0.05, rely = 0.1, relwidth = 0.40, relheight = 0.15)


    def Calendar(self):
        
        # Criando calendario
        self.calendar_one = DateEntry(self.frame_1, width=12, background='#3D51C3', foreground='white', 
            borderwidth=2, font="Arial 12", selectmode='day', cursor="hand1", year=2021, month=1, day=31, date_pattern='dd/mm/Y')

        self.calendar_two = DateEntry(self.frame_1, width=12, background='#3D51C3',foreground='white', 
            borderwidth=2, font="Arial 12", selectmode='day', cursor="hand1", year=2021, month=2, day=7, date_pattern='dd/mm/Y')

        self.calendar_one.place(relx=0.05, rely=0.35, relwidth=0.19, relheight=0.1)

        self.calendar_two.place(relx=0.26, rely=0.35, relwidth=0.19, relheight=0.1)


    def Buttons(self):

        self.bt_pesquisar = Button(self.frame_1, text="PESQUISAR", bd=2, 
            bg='#364094', fg='white', font=('verdana', 10, 'bold'), command=self.search)

        self.bt_export_pdf = Button(self.frame_1, text="EXPORTAR PDF", bd=2, 
            bg='#364094', fg='white', font=('verdana', 8, 'bold'), command=None)

        self.bt_exportar_todos = Button(self.frame_1, text="EXPORTAR TUDO", bd=2, 
            bg='#D92A2A', fg='white', font=('verdana', 8, 'bold'), command=self.search_all)

        self.bt_pesquisar.place(relx=0.05, rely=0.5, relwidth=0.4, relheight=0.2)

        #self.bt_export_pdf.place(relx=0.05, rely=0.725, relwidth=0.19, relheight=0.15)

        self.bt_exportar_todos.place(relx=0.05, rely=0.725, relwidth=0.4, relheight=0.15)


    def Labels(self):

        self.lb_motorista = Label(self.frame_1, text="Escolha o motorista: ", bg='#dfe3ee', font=('Arial', 10, 'bold'))

        self.lb_resultado = Label(self.frame_1, text="Analise dos resultados", bg='#dfe3ee', font=('Arial', 10, 'bold'))

        self.lb_data_inicial = Label(self.frame_1, text = "Data inicial:", bg = '#dfe3ee')

        self.lb_data_final = Label(self.frame_1, text = "Data final:", bg = '#dfe3ee')


        self.lb_motorista.place(relx=0.05, rely=0.005)

        self.lb_resultado.place(relx=0.5, rely=0.005)

        self.lb_data_inicial.place(relx = 0.05, rely = 0.27)

        self.lb_data_final.place(relx = 0.26, rely = 0.27)


    def Treeview_frame_1(self):
        self.Resultado = ttk.Treeview(self.frame_1, height=3, 
            column=("coll1", "coll2", "coll3", "coll4"))

        self.scroll_list = Scrollbar(self.frame_1, orient='vertical', command=self.Resultado.yview)
        self.Resultado.configure(yscrollcommand=self.scroll_list.set)

        self.Resultado.heading("#0", text="")
        self.Resultado.heading("#1", text="Valores")
        self.Resultado.heading("#2", text="N° de viajens")
        self.Resultado.heading("#3", text="Total")
        self.Resultado.heading("#4", text="Porcentagens")

        self.Resultado.column("#0", width=0)
        self.Resultado.column("#1", width=50)
        self.Resultado.column("#2", width=50)
        self.Resultado.column("#3", width=75)
        self.Resultado.column("#4", width=75)
        
        self.Resultado.place(relx=0.50, rely=0.1, relwidth=0.435, relheight=0.85)
        self.scroll_list.place(relx=0.93, rely=0.1, relwidth=0.025, relheight=0.85)


    def Treeview_frame_2(self):

        self.Result_db_serch = ttk.Treeview(self.frame_2, height=3, 
            column=("coll1", "coll2", "coll3", "coll4"))

        self.scroll_list = Scrollbar(self.frame_2, orient='vertical', command=self.Result_db_serch.yview)

        self.Result_db_serch.configure(yscrollcommand=self.scroll_list.set)

        self.Result_db_serch.heading("#0", text="")
        self.Result_db_serch.heading("#1", text="cod")
        self.Result_db_serch.heading("#2", text="data")
        self.Result_db_serch.heading("#3", text="hora")
        self.Result_db_serch.heading("#4", text="valor")

        self.Result_db_serch.column("#0", width=0)
        self.Result_db_serch.column("#1", width=10)
        self.Result_db_serch.column("#2", width=45)
        self.Result_db_serch.column("#3", width=45)
        self.Result_db_serch.column("#4", width=45)

        self.Result_db_serch.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroll_list.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)
