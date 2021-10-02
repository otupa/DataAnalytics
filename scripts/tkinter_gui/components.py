
class Components():
    ''' Window Components '''
    def __init__(self, window) -> None:
        self.window = window
    
    def menu_bar(self):
        menuBar = Menu(self.window, tearoff=0)
        self.window.config(menu=menuBar)
        archives = Menu(menuBar, tearoff=0)
        helpMenu = Menu(menuBar, tearoff=0)
        archives.add_command(label="Importar", command=self.importar)
        archives.add_command(label="Exportar", command=None)
        archives.add_command(label="sair", command=None)
        menuBar.add_cascade(label="Arquivo", menu=archives)
        menuBar.add_cascade(label="Ajuda", menu=helpMenu)

    def dataView(self):
        self.dataFrame = Frame(
            self.window, 
            bd=4, bg='#dfe3ee',
            highlightbackground='#759fe6', 
            highlightthickness=3)

        self.dataFrame.place(
            relx=0.51, 
            rely=0.03, 
            relwidth=0.47, 
            relheight=0.95)

        self.dataTreeview = ttk.Treeview(
            self.dataFrame, 
            height=2,
            column=("coll1", "coll2", "coll3"))

        self.dataTreeview.place(
            relx=0.02, 
            rely=0.51, 
            relwidth=0.96, 
            relheight=0.47)

        self.scrollData = Scrollbar(
            self.dataTreeview, 
            orient='vertical',
            command=self.dataTreeview.yview)

        self.scrollData.place(
            relx=0.96, 
            rely=0.016, 
            relwidth=0.03, 
            relheight=0.97)

        self.dataTreeview.configure(
            yscrollcommand=self.scrollData.set)
        
        self.dataTreeview.heading("#0", text="")
        self.dataTreeview.heading("#1", text="date-time")
        self.dataTreeview.heading("#2", text="valor")
        self.dataTreeview.heading("#3", text="type")

        self.dataTreeview.column("#0", width=1)
        self.dataTreeview.column("#1", width=45)
        self.dataTreeview.column("#2", width=200)
        self.dataTreeview.column("#3", width=50)

        # -------------------------------------- #
        self.resultTreeview = ttk.Treeview(
            self.dataFrame, height=3, 
            column=("coll1", "coll2", "coll3", "coll4"))

        self.resultTreeview.place(
            relx=0.02, 
            rely=0.02, 
            relwidth=0.96, 
            relheight=0.47)

        self.scrollResult = Scrollbar(
            self.resultTreeview, 
            orient='vertical', 
            command=self.resultTreeview.yview)

        self.scrollResult.place(
            relx=0.96, 
            rely=0.016, 
            relwidth=0.03, 
            relheight=0.97)

        self.resultTreeview.configure(
            yscrollcommand=self.scrollResult.set)

        self.resultTreeview.heading("#0", text="")
        self.resultTreeview.heading("#1", text="Valores")
        self.resultTreeview.heading("#2", text="N° de viajens")
        self.resultTreeview.heading("#3", text="Total")
        self.resultTreeview.heading("#4", text="Porcentagens")

        self.resultTreeview.column("#0", width=0)
        self.resultTreeview.column("#1", width=50)
        self.resultTreeview.column("#2", width=50)
        self.resultTreeview.column("#3", width=75)
        self.resultTreeview.column("#4", width=75)

    def menuView(self):

        self.leftFrame = Frame(
            self.window, 
            bd=4, bg='#dfe3ee',
            highlightbackground='#759fe6', 
            highlightthickness=3)

        self.leftFrame.place(
            relx=0.02, 
            rely=0.03, 
            relwidth=0.47, 
            relheight=0.95)

        self.menuFrame = Frame(
            self.leftFrame, 
            bd=1, bg='#dfe3ee',)

        self.menuFrame.place(
            relx=0.02, 
            rely=0.55, 
            relwidth=0.96, 
            relheight=0.40)

        self.leftCalendar = DateEntry(
            self.menuFrame, 
            width=12, 
            background='#3D51C3', 
            foreground='white', 
            borderwidth=2, 
            font="Arial 12", 
            selectmode='day', 
            cursor="hand1", 
            year=2021, month=1, day=31, 
            date_pattern='dd/mm/Y')

        self.leftCalendar.place(
            relx=0.02, 
            rely=0.02, 
            relwidth=0.47, 
            relheight=0.20)

        self.rightCalendar = DateEntry(
            self.menuFrame, 
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

        self.rightCalendar.place(
            relx=0.52,
            rely=0.02,
            relwidth=0.46,
            relheight=0.20)
            
        stringVar = StringVar()
        stringVar.set("MOTORISTAS")

        self.dropMenu = OptionMenu(
            self.menuFrame, 
            stringVar, 
            *self.listMoto())

        self.dropMenu.place(
            relx = 0.02, 
            rely = 0.27, 
            relwidth = 0.96, 
            relheight = 0.18)

        btSearch = Button(
            self.menuFrame, 
            text="PESQUISAR", 
            bd=2, 
            bg='#364094', 
            fg='white', 
            font=('verdana', 10, 'bold'), 
            command=self.search_)

        btSearch.place(
            relx=0.02,
            rely=0.50,
            relwidth=0.47,
            relheight=0.23)

        self.btExport = Button(
            self.menuFrame, 
            text="EXPORTAR PDF", 
            bd=2, 
            bg='#364094', 
            fg='white', 
            font=('verdana', 8, 'bold'), 
            command=None)

        self.btExport.place(
            relx=0.51,
            rely=0.50,
            relwidth=0.47,
            relheight=0.23)

        self.btExportAll = Button(
            self.menuFrame, 
            text="EXPORT ALL", 
            bd=2, 
            bg='#D92A2A', 
            fg='white', 
            font=('verdana', 8, 'bold'), 
            command=self.export_all)

        self.btExportAll.place(
            relx=0.02,
            rely=0.75,
            relwidth=0.96,
            relheight=0.23)

    def listBox(self):
        self.listBoxFrame = Frame(
            self.leftFrame, 
            bd=1, bg='#dfe3ee',)

        self.listBoxFrame.place(
            relx=0.02, 
            rely=0.02, 
            relwidth=0.96, 
            relheight=0.49)

        self.fistListBox = Listbox(self.listBoxFrame)

        self.fistListBox.place(
            relx=0.02,
            rely=0.02,
            relwidth=0.43,
            relheight=0.96)
        
        self.scroll = Scrollbar(
            self.fistListBox, 
            orient='vertical',
            command=self.fistListBox.yview)

        self.scroll.place(
            relx=0.9, 
            rely=0.016, 
            relwidth=0.07, 
            relheight=0.97)

        self.secondListBox = Listbox(self.listBoxFrame)

        self.secondListBox.place(
            relx=0.54,
            rely=0.02,
            relwidth=0.43,
            relheight=0.96)

        self.scroll = Scrollbar(
            self.secondListBox, 
            orient='vertical',
            command=self.secondListBox.yview)

        self.scroll.place(
            relx=0.9, 
            rely=0.016, 
            relwidth=0.07, 
            relheight=0.97)

        self.moveButtonRight = Button(
            self.listBoxFrame, 
            text=">", 
            bd=2, 
            bg='#364094', 
            fg='white', 
            font=('verdana', 10, 'bold'), 
            command=self.moveRight)
        
        self.moveButtonRight.place(
            relx=0.47, 
            rely=0.35, 
            relwidth=0.055, 
            relheight=0.05)

        self.moveButtonLeft = Button(
            self.listBoxFrame, 
            text="<", 
            bd=2, 
            bg='#364094', 
            fg='white', 
            font=('verdana', 10, 'bold'), 
            command=self.moveLeft)
        
        self.moveButtonLeft.place(
            relx=0.47, 
            rely=0.5, 
            relwidth=0.055, 
            relheight=0.05)

        self.porcentButton = Button(
            self.listBoxFrame, 
            text="%", 
            bd=2, 
            bg='#364094', 
            fg='white', 
            font=('verdana', 10, 'bold'), 
            command=self.windowPorcent)
        
        self.porcentButton.place(
            relx=0.47, 
            rely=0.7, 
            relwidth=0.055, 
            relheight=0.05)

    