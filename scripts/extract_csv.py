import datetime
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
    try:
        date = re.findall(r"\d+/\d+/\d+", argument)
        date = datetime.datetime.strptime(date[0], "%d/%m/%Y").strftime("%Y-%m-%d")
        if not date:
            date = '0000-00-00'
        hour = re.findall(r"\d+\:\d+", argument)
        hour = hour[0]+':00'
        date_time = "{} {}".format(date, hour)

        valor = re.findall(r"\d+\s+reais", argument)
        valor = valor[0][:-6]
        if 'desconto no boleto' in argument:
            operation = '-'
        else:
            operation = '+'

        format_line = [date_time, valor, operation]
        dataframe_list.append(format_line)
    except Exception as error:
        print(error, argument)
        return True
    
def extract(directory, arg_one, arg_two):
    for archive in os.listdir(directory):
        try:
            dataframe_list.clear()
            _open = open_archive(directory, archive)
            talk, name = _open
            # print(talk)
            # print(name)
            fill_line = line_piker(talk, arg_one)
            filled_line = line_piker(fill_line, arg_two)
            for line in filled_line:
                filter(line)
            # print(dataframe_list)
            save_csv(dataframe_list, name)
        except Exception as error:
            print("erro ao Extrair", error,dataframe_list[-1] )