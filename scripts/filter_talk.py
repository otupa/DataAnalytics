import re

def filter(argument):

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
        format_line[2] = "-R$"+format_line[2][:-6]+",00"
    else:
        format_line[2] = "R$"+format_line[2][:-6]+",00"

    return format_line