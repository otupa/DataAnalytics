



    def windowPorcent(self):
        windowPorcent = Toplevel(self.window)
        windowPorcent.geometry('400x250')

        btConfirm = Button(
            windowPorcent, 
            text="Confirmar", 
            bd=2, 
            bg='#364094', 
            fg='white', 
            font=('verdana', 10, 'bold'), 
            command=None)
        
        btConfirm.place(
            relx=0.38,
            rely=0.82,
            relheight=0.12,
            relwidth=0.2
        )

        framePorcent = Frame(
            windowPorcent, 
            bd=4, 
            bg='#dfe3ee',
            highlightbackground='#759fe6', 
            highlightthickness=3)
        
        framePorcent.place(
            relx=0.02,
            rely=0.02,
            relheight=0.76,
            relwidth=0.46)
        
        # --------- Labels ----------- #

        lbTitle = Label(
            framePorcent, 
            text = "Definir Porcentagens", 
            bg = '#dfe3ee'
        )

        lbTitle.place(
            relx=0.2,
            rely=0.02,
        )

        lbValor = Label(
            framePorcent,
            text='Valor',
            bg = '#dfe3ee'
        )

        lbValor.place(
            relx=0.02,
            rely=0.2
        )

        lbTypeOne = Label(
            framePorcent,
            text='Porcent',
            bg = '#dfe3ee')

        lbTypeOne.place(
            relx=0.35,
            rely=0.2)

        lbTypeTwo = Label(
            framePorcent,
            text='P. Desc.',
            bg = '#dfe3ee')

        lbTypeTwo.place(
            relx=0.70,
            rely=0.2)

        lbPorcentOne = Label(
            framePorcent, 
            text = "R$10 >=", 
            bg = '#dfe3ee')

        lbPorcentOne.place(
            relx=0.02,
            rely=0.4)

        lbPorcentTwo = Label(
            framePorcent, 
            text = "R$12", 
            bg = '#dfe3ee')

        lbPorcentTwo.place(
            relx=0.02,
            rely=0.6)

        lbPorcentTree = Label(
            framePorcent, 
            text = "R$20", 
            bg = '#dfe3ee')

        lbPorcentTree.place(
            relx=0.02,
            rely=0.8)


        # -------- Entry -------- #

        porcentEntryOne = Entry(framePorcent)
        porcentEntryOne.place(
            relx=0.4, 
            rely=0.4, 
            relwidth=0.14, 
            relheight=0.12)

        porcentEntryTwo = Entry(framePorcent)
        porcentEntryTwo.place(
            relx=0.4, 
            rely=0.6, 
            relwidth=0.14, 
            relheight=0.12)        
            
        porcentEntryTree = Entry(framePorcent)
        porcentEntryTree.place(
            relx=0.7, 
            rely=0.8, 
            relwidth=0.14, 
            relheight=0.12)

        porcentEntryOneDesc = Entry(framePorcent)
        porcentEntryOneDesc.place(
            relx=0.7, 
            rely=0.4, 
            relwidth=0.14, 
            relheight=0.12)

        porcentEntryTwoDesc = Entry(framePorcent)
        porcentEntryTwoDesc.place(
            relx=0.7, 
            rely=0.6, 
            relwidth=0.14, 
            relheight=0.12)        
            
        porcentEntryTreeDesc = Entry(framePorcent)
        porcentEntryTreeDesc.place(
            relx=0.4, 
            rely=0.8, 
            relwidth=0.14, 
            relheight=0.12)

        # -------- Frame Special Porcent -------- #

        framePorcentTwo = Frame(
            windowPorcent, 
            bd=4, 
            bg='#dfe3ee',
            highlightbackground='#759fe6', 
            highlightthickness=3)
        
        framePorcentTwo.place(
            relx=0.50,
            rely=0.02,
            relheight=0.76,
            relwidth=0.48)

        
        # --------- Labels ----------- #

        lbTitleSpecial = Label(
            framePorcentTwo, 
            text = "Definir Porcentagens", 
            bg = '#dfe3ee'
        )

        lbTitleSpecial.place(
            relx=0.2,
            rely=0.02,
        )

        lbValorSpecial = Label(
            framePorcentTwo,
            text='Valor',
            bg = '#dfe3ee'
        )

        lbValorSpecial.place(
            relx=0.02,
            rely=0.2
        )

        lbTypeOneSpecial = Label(
            framePorcentTwo,
            text='Porcent',
            bg = '#dfe3ee')

        lbTypeOneSpecial.place(
            relx=0.35,
            rely=0.2)

        lbTypeTwoSpecial = Label(
            framePorcentTwo,
            text='P. Desc.',
            bg = '#dfe3ee')

        lbTypeTwoSpecial.place(
            relx=0.70,
            rely=0.2)

        lbPorcentOneSpecial = Label(
            framePorcentTwo, 
            text = "R$10 >=", 
            bg = '#dfe3ee')

        lbPorcentOneSpecial.place(
            relx=0.02,
            rely=0.4)

        lbPorcentTwoSpecial = Label(
            framePorcentTwo, 
            text = "R$19 >=", 
            bg = '#dfe3ee')

        lbPorcentTwoSpecial.place(
            relx=0.02,
            rely=0.6)

        lbPorcentTreeSpecial = Label(
            framePorcentTwo, 
            text = "R$20 <=", 
            bg = '#dfe3ee')

        lbPorcentTreeSpecial.place(
            relx=0.02,
            rely=0.8)

        

        # -------- Entry -------- #

        porcentEntryOneSpecial = Entry(framePorcentTwo)
        porcentEntryOneSpecial.place(
            relx=0.4, 
            rely=0.4, 
            relwidth=0.14, 
            relheight=0.12)

        porcentEntryTwoSpecial = Entry(framePorcentTwo)
        porcentEntryTwoSpecial.place(
            relx=0.4, 
            rely=0.6, 
            relwidth=0.14, 
            relheight=0.12)        
            
        porcentEntryTreeSpecial = Entry(framePorcentTwo)
        porcentEntryTreeSpecial.place(
            relx=0.7, 
            rely=0.8, 
            relwidth=0.14, 
            relheight=0.12)

        porcentEntryOneDescSpecial = Entry(framePorcentTwo)
        porcentEntryOneDescSpecial.place(
            relx=0.7, 
            rely=0.4, 
            relwidth=0.14, 
            relheight=0.12)

        porcentEntryTwoDescSpecial = Entry(framePorcentTwo)
        porcentEntryTwoDescSpecial.place(
            relx=0.7, 
            rely=0.6, 
            relwidth=0.14, 
            relheight=0.12)        
            
        porcentEntryTreeDescSpecial = Entry(framePorcentTwo)
        porcentEntryTreeDescSpecial.place(
            relx=0.4, 
            rely=0.8, 
            relwidth=0.14, 
            relheight=0.12)