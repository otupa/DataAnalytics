from datetime import datetime, date, timedelta

def date_generator(_initial, _final):
    dates_range = []
    initial_date = datetime.strptime(_initial, '%d/%m/%Y').date()
    final_date = datetime.strptime(_final, '%d/%m/%Y').date()
    increment = timedelta(days=1)

    while initial_date <= final_date:
        dates_range.append(initial_date.strftime('%d/%m/%Y'))
        initial_date += increment
    return dates_range