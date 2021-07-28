import pandas
import re
import os

dataframe_list = []

def open_archive(directory, archive):
    try:
        archive_talk = open(os.path.join(
            directory, archive), 'r', encoding = 'utf-8').read().splitlines()
        name_file = archive[:-4][29:]
        return archive_talk, name_file
    except Exception as error:
        print("Erro ao abrir arquivos", error)

def line_piker(archive_talk, argument):
    lines_piked = [linha for linha in archive_talk if argument in linha]
    return lines_piked

def save_csv(data_list, archive_name):
    df_pd = pandas.DataFrame(data_list).to_csv(
        'data_csv/'+archive_name+'.csv', 
        header=False, encoding='utf-8', index=False)

def filter(argument):
    date = re.findall(r"\d+/\d+/\d+", argument)
    hour = re.findall(r"\d+\:\d+", argument)
    valor = re.findall(r"\d+\s+reais", argument)

    format_line = [date, hour, valor]
    if not format_line[0]:
        format_line[0] = dataframe_list[-1][0]
    try:
        for i, j in enumerate(format_line):
            format_line[i] = j[0].replace(',','[').replace('!',']').replace('.','')
    except Exception as error: 
        print("Erro no filtro", error)
        return True

    if 'desconto no boleto' in argument:
        format_line[2] = "-R$"+format_line[2][:-6]+",00"
    else:
        format_line[2] = "R$"+format_line[2][:-6]+",00"

    dataframe_list.append(format_line)
    
def extract(directory, arg_one, arg_two):
    for archive in os.listdir(directory):
        try:
            dataframe_list = []
            _open = open_archive(directory, archive)
            talk, name = _open
            fill_line = line_piker(talk, arg_one)
            filled_line = line_piker(fill_line, arg_two)
            for line in filled_line:
                filter(line)
            save_csv(dataframe_list, name)
        except Exception as error:
            print("erro ao Extrair", error)