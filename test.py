import datetime

month_name = 'Jan'

month_num = datetime.datetime.strptime(month_name, '%b').month

print(month_num, type(month_num))

#fechaRecogida = datetime.datetime(int(2023), 'Jan', int(12))

