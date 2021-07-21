

class Pdf_generator(SoftScript):

    def main(self, arg):
        for file in os.listdir('result'):
            self.main_loop(file, arg)
    
    def main_loop(self, arg, destiny):
        archive = open(os.path.join('result', arg))
        nome_csv = os.path.basename(arg)[:-4]
        name = nome_csv.replace(" ", "_")
        a = from_csv(archive)
        header, data = self.get_data_from_prettytable(a)

        self.export_to_pdf(header, data, name, destiny)

    def get_data_from_prettytable(self, data):

        def remove_space(liste):

            list_without_space = []
            for mot in liste:                                       # For each word in list
                word_without_space = mot.replace(' ', '')           # word without space
                list_without_space.append(word_without_space)       # list of word without space
            return list_without_space

        # Get each row of the table
        string_x = str(data).split('\n')                               # Get a list of row
        header = string_x[1].split('|')[1: -1]                      # Columns names
        rows = string_x[3:len(string_x) - 1]                        # List of rows

        list_word_per_row = []
        for row in rows:                                            # For each word in a row
            row_resize = row.split('|')[1:-1]                       # Remove first and last arguments
            list_word_per_row.append(remove_space(row_resize))      # Remove spaces

        return header, list_word_per_row
    

    def export_to_pdf(self, header, data, name, destiny):

        pdf = FPDF()                                # New  pdf object

        pdf.set_font("Arial", size=12)              # Font style
        epw = pdf.w - 2*pdf.l_margin                # Witdh of document
        col_width = pdf.w / 4.5                     # Column width in table
        row_height = pdf.font_size * 1.5            # Row height in table
        spacing = 1.3                               # Space in each cell

        pdf.add_page()                              # add new page

        pdf.cell(epw, 0.0, 'FATURA SEMANAL', align='C') 
        pdf.ln(row_height*spacing)                  

        
        for item in header:                        
            pdf.cell(col_width, row_height*spacing, 
                    txt=item, border=0)
        pdf.ln(row_height*spacing)           

        final = data.pop(-1)

        for row in data:                           
            for item in row:                       
                pdf.cell(col_width, row_height*spacing, 
                        txt=item, border=1)

                
            pdf.ln(row_height*spacing)       
        pdf.ln(row_height*spacing)              

        for i in final:
            pdf.cell(col_width, row_height*spacing,
                        txt=i, border=1)

        pdf.output(os.path.join(destiny,'{}.pdf'.format(name)))
         
        pdf.close()                                 
