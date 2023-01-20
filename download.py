import sqlite3
import xlsxwriter
from datetime import datetime  # Used to name the file with today's date


def downloadfile(dbname):
    workbook = xlsxwriter.Workbook(dbname + datetime.now().strftime("%Y %m %d") + '.xlsx')  # Create file
    conn = sqlite3.connect(dbname)  # Connect to your database
    cursor = conn.cursor()  # Create the cursor
    try:
        worksheet = workbook.add_worksheet(name='data')  # Sheet names in excel can have up to 31 chars
    except:
        pass
    worksheet.write(0, 0, 'titulo del producto')
    worksheet.write(0, 1, 'URL')
    worksheet.write(0, 2, 'nº reviews past 15 days')
    worksheet.write(0, 3, 'nº reviews past 30 days')
    for row_number, row in enumerate(cursor.execute('SELECT * FROM data order by last30 DESC')):
        for column_number, item in enumerate(row):
            try:
                worksheet.write(row_number + 1, column_number, item)  # Write the cell in the current sheet
            except:
                pass
    workbook.close()
