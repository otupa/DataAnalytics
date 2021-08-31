from datetime import datetime, date

def date_generator(argument):
    date_ = datetime.strptime(argument, '%d/%m/%Y').date()
    print(date_)
    return str(date_)+" 00:00:00"

