import time
import openpyxl
import Copy_excel as ce


# primero creamos
filepath = "poc.xlsx"
wb = openpyxl.Workbook()
wb.save(filepath)

excel = ce.Copy_excel('poc.xlsx','poc.xlsx')
while (1==1):
    arr = ['cs','csadca','asd','asdfasf']
    excel.ws.append(arr)
    excel.save_excel()
    time.sleep(4)


