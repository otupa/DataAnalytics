
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