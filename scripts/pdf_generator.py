from fpdf import FPDF
import os

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

    pdf.cell(col_width, row_height*spacing, '{}'.format(name), border=1)
    pdf.cell(col_width, row_height*spacing, '', border=0)
    pdf.cell(col_width, row_height*spacing, '{}'.format(date_one), border=0)
    pdf.cell(col_width, row_height*spacing, '{}'.format(date_two), border=0)
    pdf.ln(pdf.font_size)

    for i in string_list(argument):
        for item in i:
            pdf.cell(col_width, row_height*spacing, '{}'.format(item), border=1)
        pdf.ln(pdf.font_size)
                       
        

    pdf.ln(row_height*spacing)           

    pdf.output(os.path.join(directory,'{}.pdf'.format(name)))
        
    pdf.close()                                 

export_to_pdf('motorista', '446546', '456465', list_, "C:/Users/tupa/Workspace/SoftG4")

from datetime import date
from os import name
from jinja2 import Template, Environment, FileSystemLoader, BaseLoader
from jinja2.nodes import With
from os.path import join
# from weasyprint import HTML, CSS
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')  
path = 'C:/Users/tupa/Workspace/SoftG4/scripts/view/'

def piker(argument):
    return [[
        locale.currency(item[0]),
        item[1],
        locale.currency(item[2]),
        locale.currency(item[3])] for item in argument]

def piker_total(item):
    return [item[0], locale.currency(item[1]), locale.currency(item[2])]
    
def render_html(argument, name, date_one, date_two):
    archive = open(join(path, 'index.html'))
    template_ = Template(archive.read())
    total_ = piker_total(argument.pop(-1))
    runs_ = piker(argument)
    return template_.render(name=name, date=date_one, date_=date_two, argument=runs_, total=total_)

def save_pdf(argument, date_one, date_two, directory):
#     html = render_html(argument, name, date_one, date_two)
#     HTML(string=html, stylesheets=[CSS('./view/css/bootstrap.css'), CSS('/view/css/mdb.css')])
    pass

