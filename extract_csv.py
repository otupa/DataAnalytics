import pandas as pd
from datetime import datetime, date, timedelta
import csv
import os
import re


class ExtractCsv():
    def __init__(self):
        self._global_list = []

    def open_archive(self, talk_dir, archive):
        _archive_talk = open(os.path.join(
            talk_dir, archive), 'r', encoding = 'utf-8').read().splitlines()
        _name_file = archive[:-4][29:]
        return _archive_talk, _name_file

    def line_piker(self, archive_talk, argument):
        lines_piked = [linha for linha in archive_talk if argument in linha]
        return lines_piked

    def save_csv(self, archive_name):
        df_pd = pd.DataFrame(_global_list).to_csv(
            'data_csv/'+archive_name+'.csv', 
            header=False, encoding='utf-8', index=False)

    def filter_talk(self, argument):
        date = re.findall(r"\d+/\d+/\d+", argument)
        hour = re.findall(r"\d+\:\d+", argument)
        valor = re.findall(r"\d+\s+reais", argument)
        format_line = [date, hour, valor]
        if not format_line[0]:
            format_line[0] = _global_list[-1][0]
        try:
            for i, j in enumerate(format_line):
                format_line[i] = j[0].replace(',','[').replace('!',']').replace('.','')
        except Exception as error: return True

        if 'desconto no boleto' in argument:
            format_line[2] = "DR$"+format_line[2][:-6]+",00"
        else:
            format_line[2] = "R$"+format_line[2][:-6]+",00"

            
        _global_list.append(format_line)

        print(format_line)
    
    def main_loop(argument, variant, variant_2):
        for archive in os.listdir(argument):
            _open = open_archive(directory, archive)
            talk, name = _open
            fill_line = line_piker(talk, variant)
            filled_line = line_piker(fill_line, variant_2)

            for line in filled_line:
                filter_talk(line)

            export = save_csv(name)