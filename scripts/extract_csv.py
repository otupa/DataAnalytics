from filter_talk import filter
import pandas
import os


def open_archive(directory, archive):
    archive_talk = open(os.path.join(
        directory, archive), 'r', encoding = 'utf-8').read().splitlines()
    name_file = archive[:-4][29:]
    return archive_talk, name_file

def line_piker(archive_talk, argument):
    lines_piked = [linha for linha in archive_talk if argument in linha]
    return lines_piked

def save_csv(data_list, archive_name):
    df_pd = pandas.DataFrame(data_list).to_csv(
        'data_csv/'+archive_name+'.csv', 
        header=False, encoding='utf-8', index=False)
    
def extract(directory, arg_one, arg_two):
    for archive in os.listdir(directory):
        _open = open_archive(directory, archive)
        talk, name = _open
        fill_line = line_piker(talk, arg_one)
        filled_line = line_piker(fill_line, arg_two)

        dataframe_list = [filter(line) for line in filled_line]
        export = save_csv(name, dataframe_list)