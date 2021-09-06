from fpdf import FPDF
import os
    
list_ = [[13, 57, 741, 111.0], [15, 23, 345, 52.0], [11, 175, 1925, 289.0], [25, 19, 475, 95.0], [22, 7, 154, 31.0], [34, 1, 34, 7.0], [50, 2, 100, 20.0], [35, 1, 35, 7.0], [40, 3, 120, 24.0], [60, 1, 60, 12.0], [11, 1, 11, -9.0], [44, 1, 44, 9.0], [12, 151, 1812, 272.0], [20, 1, 20, 3.0], [28, 2, 56, 11.0], [0, 445, 5932, 934.0]]
def string_list(argument):
    return [['R$'+str(int(valor))+',00' 
                    for valor in item] 
                    for item in argument]

def export_to_pdf(name, date_one, date_two, argument, directory):
    pdf = FPDF()                                # New  pdf object
    pdf.set_font("Arial", size=12)              # Font style
    whitd = pdf.w - 2*pdf.l_margin              # Witdh of document
    col_width = pdf.w / 4.5                     # Column width in table
    row_height = pdf.font_size * 1.5            # Row height in table
    spacing = 1.3                               # Space in each cell

    pdf.add_page()                              # add new page

    pdf.cell(whitd, 0.0, 'Fatura Semanal - G4 Mobile', align='C')
    pdf.ln(row_height*spacing)                  

    pdf.cell(col_width, row_height*spacing, '{}'.format(name), border=0)
    pdf.cell(col_width, row_height*spacing, '', border=0)
    pdf.cell(col_width, row_height*spacing, '{}'.format(date_one), border=0)
    pdf.cell(col_width, row_height*spacing, '{}'.format(date_two), border=0)
    pdf.ln(pdf.font_size)


    for i in string_list(argument):
        for item in i:
            pdf.cell(col_width, row_height*spacing, '{}'.format(item), border=0)
        pdf.ln(pdf.font_size)
                       
        

    pdf.ln(row_height*spacing)           

    pdf.output(os.path.join(directory,'{}.pdf'.format(name)))
        
    pdf.close()                                 

export_to_pdf('motorista', '446546', '456465', list_, "C:/Users/tupa/Workspace/SoftG4")