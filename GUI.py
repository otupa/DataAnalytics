<<<<<<< HEAD
from SoftBackend import *
import pathlib
import shutil
=======
from SoftScript import *
import pathlib
>>>>>>> flask
from math import ceil
# Tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkcalendar import Calendar, DateEntry
from datetime import datetime


<<<<<<< HEAD
window = Tk()

class Funcoes():

    def inicializar(self, arg):

        self.SoftG4 = SoftG4()

        self.SoftG4.extract_csv(arg)

        self.SoftG4.Sql_scripts()

        self.SoftG4.Sql_insert()

    def connect_sql(self):
        self.connect = Connect()
        return True

    def select_tb(self, nome_moto, data):

=======

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

        pdf_destiny = filedialog.askdirectory()

        for file in os.listdir('data_csv'):

            nome = file[:-4].replace(" ", "_")

            paterns = "{}".format(file[:-4]), " ", str(self.data_1), str(self.data_2)

            [self.select_tb(nome, date) for date in dates]

            result = self.calculate_runs(self.calc_)

            result.insert(0, paterns)

            result.insert(1, ("valor","viajens","total","porcentagem"))

            local = os.path.join('result', nome+'.csv')

            [pd.DataFrame(result).to_csv(local, header=False, encoding='utf-8', index=False)]

            self.calc_.clear()

        self.Result_db_serch.delete(*self.Result_db_serch.get_children())
        self.Resultado.delete(*self.Resultado.get_children())

        self.generator.main(pdf_destiny)


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
        
>>>>>>> flask
        self.connect_sql()

        schema = open('sql/SEARCH_'+nome_moto+'.sql').read()

        lista_treeview = self.connect.cursor.execute(schema, (data,))

<<<<<<< HEAD
        [self.listaCli.insert("", END, values=info) for info in lista_treeview]
=======
        [self.Result_db_serch.insert("", END, values=info) for info in lista_treeview]
>>>>>>> flask

        lista = self.connect.cursor.execute(schema, (data,))

        for i in lista:
            self.calc_.append(i)
    
        self.connect.close_db()

<<<<<<< HEAD
    def calcular_viajens(self , lista):
        # Lista que recebe o conteudo do Treeview
        lista_master = []

        # Total de viajens
        total_viajens = []

        # Lista que recebe o valor de cada viajem
        viajens_moto = []

        # Porcrntagem paga pelo motorista
        lucro = []
        
        def receber_pesquisa():
            lista_resultados = []
            [lista_resultados.append(item[3]) for item in lista if item[3][:1] == "R"]
            return lista_resultados

        def receber_pesquisa_desc():
            lista_descontos = []
            [lista_descontos.append(item[3]) for item in lista if item[3][:1] == "D"]
            return lista_descontos

        def variaveis_precos():
            lista_valor = []
            [lista_valor.append(item) for item in receber_pesquisa() if item not in lista_valor]
            lista_valor = sorted(lista_valor)
            return lista_valor

        def variaveis_precos_descontos():
            lista_valor_desc = []
            [lista_valor_desc.append(item) for item in receber_pesquisa_desc() if item not in lista_valor_desc]    
            lista_valor_desc = sorted(lista_valor_desc)
            return lista_valor_desc

        def calcular_porcentagens(p_valor, p_total):
=======
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
>>>>>>> flask
            p_valor = int(p_valor[2:][:-3])
            
            if p_valor == 10:
                porcent = p_total * 0.10
                porcent = round(porcent, 2)
                return porcent

<<<<<<< HEAD
            elif p_valor <= 20:
=======
            elif p_valor <= 19:
>>>>>>> flask
                porcent = p_total * 0.15
                porcent = round(porcent, 2)
                return porcent

            elif p_valor >= 20:
                porcent = p_total * 0.20
                porcent = round(porcent, 2)
                return porcent

<<<<<<< HEAD
        def calcular_porcentagens_desc(p_valor, p_total):
=======
        def calc_desc_porcent(p_valor, p_total):
>>>>>>> flask

            p_valor = int(p_valor[3:][:-3])

            if p_valor == 10:
                porcent = p_total * -0.90
                porcent = round(porcent, 2)
                return porcent
            
<<<<<<< HEAD
            elif p_valor <= 20:
=======
            elif p_valor <= 19:
>>>>>>> flask
                porcent = p_total * -0.85
                porcent = round(porcent, 2)
                return porcent

            elif p_valor >= 20:
                porcent = p_total * -0.80
                porcent = round(porcent, 2)
                return porcent

<<<<<<< HEAD
        def multiplicar(valor, quantidade):
            total_mult = int(valor[2:][:-3]) * quantidade
            return total_mult

        def multiplicar_desc(valor, quantidade):
            total_mult = int(valor[3:][:-3]) * quantidade
=======
        def mult(valor, amount):
            total_mult = int(valor[2:][:-3]) * amount
            return total_mult

        def mult_desc(valor, amount):
            total_mult = int(valor[3:][:-3]) * amount
>>>>>>> flask
            return total_mult

        def schema_pesquisa():
            # Percorre a lista valor calculando o que será exibido no  Treview do tkinter 
<<<<<<< HEAD
            for valor in variaveis_precos():

                # Conta a quantidade de viajens
                quantidade_viajens = receber_pesquisa().count(valor)

                total_viajens.append(quantidade_viajens)

                # Multiplicando o valor pela quantidade de viajens
                mult_total = multiplicar(valor, quantidade_viajens)
                
                # Soma ao valor total
                viajens_moto.append(mult_total)

                # Calcula a porcentagem para cada valor
                porcentagem = calcular_porcentagens(valor, mult_total)

                lucro.append(porcentagem)
=======
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
>>>>>>> flask

                # Esquema que será exibido no Treview do tkinter 
                schema = [
                    valor,                                  # valor
<<<<<<< HEAD
                    "x "+str(quantidade_viajens)+"  =",     # quantidade de vianjens
                    "R$"+str(mult_total)+",00",             # valor total das viajens
                    "R$"+str(porcentagem)                   # porcentagem da empresa
                    ]

                lista_master.append(schema)

        def schema_pesquisa_desc():
            # Percorre a lista valor calculando o que será exibido no  Treview do tkinter 
            for valor in variaveis_precos_descontos():

                # Conta a quantidade de viajens
                quantidade_viajens = receber_pesquisa_desc().count(valor)

                total_viajens.append(quantidade_viajens)

                # Multiplicando o valor pela quantidade de viajens
                mult_total = multiplicar_desc(valor, quantidade_viajens)
                
                # Soma ao valor total
                viajens_moto.append(mult_total)

                # Calcula a porcentagem para cada valor
                porcentagem_desc = calcular_porcentagens_desc(valor, mult_total)

                lucro.append(porcentagem_desc)
=======
                    str(amount_runs),                      # quantidade de vianjens
                    "R$"+str(mult_total)+",00",             # valor total das viajens
                    "R$"+"{:,.2f}".format(porcenting).replace('.',',')   # porcentagem da empresa
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
>>>>>>> flask

                # Esquema que será exibido no Treview do tkinter 
                schema = [
                    valor,                                  # valor
<<<<<<< HEAD
                    "x "+str(quantidade_viajens)+"  =",     # quantidade de vianjens
                    "R$"+str(mult_total)+",00",             # valor total das viajens
                    "R$"+str(porcentagem_desc)                   # porcentagem da empresa
                    ]

                lista_master.append(schema)

        def schema_pesquisa_total():

            # Soma o valor total do lucro da empresa
            soma_total_viajens = sum(viajens_moto)

            # Insere na lista principal o esquema com:
            lista_master.append([
                "Total:",                                       #
                "x "+str(sum(total_viajens)),                   # total de viajens
                "R$"+str(soma_total_viajens)+",00",             # total faturada pelo motorista
                "R$"+str(round(sum(lucro), 2))                            # total da porcentagem da empresa
=======
                    str(amount_runs),                       # quantidade de vianjens
                    "R$"+str(mult_total)+",00",             # valor total das viajens
                    "R$"+"{:,.2f}".format(porcent_desc).replace('.',',') # porcentagem da empresa
                    ]

                master_list.append(schema)

        def schema_search_total():

            # Soma o valor total do lucro da empresa
            sum_total_runs = sum(moto_runs)

            # Insere na lista principal o esquema com:
            master_list.append([
                "Total:",                                       
                str(sum(total_runs)),                        # total de viajens
                "R$"+str(sum_total_runs)+",00",              # total faturada pelo motorista
                "R$"+"{:,.2f}".format(round(sum(moto_porcent), 2)).replace('.',',')
>>>>>>> flask
                ])

        def main():
            schema_pesquisa()
<<<<<<< HEAD
            schema_pesquisa_desc()
            schema_pesquisa_total()
            [self.Resultado.insert("", END, values=info) for info in lista_master]

        main()
        return lista_master

    def gerar_analise(self):

        self.data_1 = self.calendar_1.get()
        self.data_2 = self.calendar_2.get()

        dates = self.SoftG4.date_generator(self.data_1, self.data_2)

        destino = filedialog.askdirectory()

        try:
            for file in os.listdir('data_csv'):

                nome = file[:-4].replace(" ", "_")

                paterns = "{}".format(nome), str(self.data_1), str(self.data_2), " "

                [self.select_tb(nome, date) for date in dates]

                resultado = self.calcular_viajens(self.calc_)

                resultado.insert(0, paterns)

                resultado.insert(1, ("Valor","N viajens","total","Porcentagem"))

                local = os.path.join(destino, nome+'.csv')

                [pd.DataFrame(resultado).to_csv(local, header=False, encoding='utf-8', index=False)]

                self.calc_.clear()

            self.listaCli.delete(*self.listaCli.get_children())
            self.Resultado.delete(*self.Resultado.get_children())

        except Exception as error:
            print("error: ", error)


    def pesquisar(self):

        self.calc_.clear()

        self.listaCli.delete(*self.listaCli.get_children())
        self.Resultado.delete(*self.Resultado.get_children())

        self.data_1 = self.calendar_1.get()
        self.data_2 = self.calendar_2.get()

        nome = self.drop_.get()

        dates = self.SoftG4.date_generator(self.data_1, self.data_2)

        [self.select_tb(nome, date) for date in dates]

        self.calcular_viajens(self.calc_)

    def importar(self):
        origem = filedialog.askdirectory()
        self.inicializar(origem)
        self.menu_moto()

    def create_dirs(self):
        os.mkdir('data_csv')
        os.mkdir('sql') 

    def delete_files(self):
        try:
            shutil.rmtree('data_csv', ignore_errors=False, onerror=None)
        except Exception:
            pass
            
        try:
            shutil.rmtree('sql', ignore_errors=False, onerror=None)
        except Exception:
            pass

        try:
            os.remove('BaseG4.db')
        except Exception:
            pass

class Application(Funcoes):

    def __init__(self):

        self.delete_files()

        self.create_dirs()

        self.calc_ = []

        self.window = window

        self.tela()
        self.menu_topo()
        self.frames_tela()
        self.textos()
        self.menu_moto()
        self.calendario()
        self.botoes()
        self.Treeview_frame_1()
        self.Treeview_frame_2()


        window.mainloop()

        self.delete_files()

    def tela(self):
=======
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
        self.generator = Pdf_generator()

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
>>>>>>> flask
        self.window.title("Soft G4")
        self.window.configure(background='#1e3743')
        self.window.geometry('800x700')
        self.window.resizable(True, True)
        self.window.maxsize(width=800, height=600)
        self.window.minsize(width=500, height=400)

<<<<<<< HEAD
    def menu_topo(self):
=======

    def Menu_top(self):
>>>>>>> flask

        menubar = Menu(self.window, tearoff=0)

        self.window.config(menu=menubar)

        menu_arquivos = Menu(menubar, tearoff=0)
        menu_ajuda = Menu(menubar, tearoff=0)

<<<<<<< HEAD
        menu_arquivos.add_command(label="Importar", command=self.importar)
=======
        menu_arquivos.add_command(label="Importar", command=self.start_extract)
>>>>>>> flask
        menu_arquivos.add_command(label="Exportar", command=None)
        menu_arquivos.add_command(label="sair", command=None)

        menubar.add_cascade(label="Arquivo", menu=menu_arquivos)
        menubar.add_cascade(label="Ajuda", menu=menu_ajuda)

<<<<<<< HEAD
    def frames_tela(self):
=======

    def Frames_window(self):
>>>>>>> flask

        self.frame_1 = Frame(self.window, bd=4, bg='#dfe3ee',
            highlightbackground='#759fe6', highlightthickness=3)

        self.frame_2 = Frame(self.window, bd=4, bg='#dfe3ee',
            highlightbackground='#759fe6', highlightthickness=3)

        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96,relheight=0.46)

        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

<<<<<<< HEAD
    def menu_moto(self):

        def list_moto():
            list_ = [""]
            arquivos = os.listdir('data_csv/')
            [list_.append(str(i)[:-4].replace(" ", "_")) for i in arquivos]
=======

    def Menu_moto(self):

        def list_moto():
            list_ = [""]
            directory = os.listdir('data_csv/')
            [list_.append(str(i)[:-4].replace(" ", "_")) for i in directory]
>>>>>>> flask
            return list_

        self.options_menu_moto = list_moto()

        self.drop_ = StringVar()

        self.drop_.set("MOTORISTA")

        self.drop = OptionMenu(self.frame_1, self.drop_, *self.options_menu_moto)

        self.drop.place(relx=0.05, rely = 0.1, relwidth = 0.40, relheight = 0.15)

<<<<<<< HEAD
    def calendario(self):
        
        # Criando calendario
        self.calendar_1 = DateEntry(self.frame_1, width=12, background='#3D51C3', foreground='white', 
            borderwidth=2, font="Arial 12", selectmode='day', cursor="hand1", year=2021, month=1, day=31, date_pattern='dd/mm/Y')

        self.calendar_2 = DateEntry(self.frame_1, width=12, background='#3D51C3',foreground='white', 
            borderwidth=2, font="Arial 12", selectmode='day', cursor="hand1", year=2021, month=2, day=7, date_pattern='dd/mm/Y')

        self.calendar_1.place(relx=0.05, rely=0.35, relwidth=0.19, relheight=0.1)

        self.calendar_2.place(relx=0.26, rely=0.35, relwidth=0.19, relheight=0.1)

    def botoes(self):

        self.bt_pesquisar = Button(self.frame_1, text="PESQUISAR", bd=2, 
            bg='#364094', fg='white', font=('verdana', 10, 'bold'), command=self.pesquisar)
=======

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
>>>>>>> flask

        self.bt_export_pdf = Button(self.frame_1, text="EXPORTAR PDF", bd=2, 
            bg='#364094', fg='white', font=('verdana', 8, 'bold'), command=None)

<<<<<<< HEAD
        self.bt_exportar_todos = Button(self.frame_1, text="EXPORTAR TUDO", bd=2, 
            bg='#D92A2A', fg='white', font=('verdana', 8, 'bold'), command=self.gerar_analise)
=======
        self.bt_exportar_todos = Button(self.frame_1, text="EXPORTAR CSV", bd=2, 
            bg='#D92A2A', fg='white', font=('verdana', 8, 'bold'), command=self.search_all)
>>>>>>> flask

        self.bt_pesquisar.place(relx=0.05, rely=0.5, relwidth=0.4, relheight=0.2)

        self.bt_export_pdf.place(relx=0.05, rely=0.725, relwidth=0.19, relheight=0.15)

<<<<<<< HEAD
        self.bt_exportar_todos.place(relx=0.26, rely=0.725, relwidth=0.19, relheight=0.15)

    def textos(self):
=======
        self.bt_exportar_todos.place(relx=0.05, rely=0.725, relwidth=0.4, relheight=0.15)


    def Labels(self):
>>>>>>> flask

        self.lb_motorista = Label(self.frame_1, text="Escolha o motorista: ", bg='#dfe3ee', font=('Arial', 10, 'bold'))

        self.lb_resultado = Label(self.frame_1, text="Analise dos resultados", bg='#dfe3ee', font=('Arial', 10, 'bold'))

        self.lb_data_inicial = Label(self.frame_1, text = "Data inicial:", bg = '#dfe3ee')

        self.lb_data_final = Label(self.frame_1, text = "Data final:", bg = '#dfe3ee')


        self.lb_motorista.place(relx=0.05, rely=0.005)

        self.lb_resultado.place(relx=0.5, rely=0.005)

        self.lb_data_inicial.place(relx = 0.05, rely = 0.27)

        self.lb_data_final.place(relx = 0.26, rely = 0.27)

<<<<<<< HEAD
=======

>>>>>>> flask
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

<<<<<<< HEAD
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

        self.scroll_list.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)






=======

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
>>>>>>> flask
