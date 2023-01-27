from openpyxl import load_workbook
from pathlib import Path
from datetime import datetime
import openpyxl


# Class to manage excel data with openpyxl.

class Copy_excel:
    def __init__(self, src, destination):
        #src y destination son lo mismo
        self.old_data = []
        # 1. comprobamos si existe el file
        path = Path(src)
        sheet_name = datetime.now().strftime("%Y_%m_%d %H_%M")
        if path.is_file():
            print("El fichero " + src + "fichero ya existe")
            self.wb = load_workbook(src)
            for s_name in self.wb.sheetnames:
                current_s = self.wb[s_name]
                m_row = current_s.max_row
                # Loop will print all values
                # of first column
                for i in range(1, m_row + 1):
                    cell_obj = current_s.cell(row=i, column=2)
                    self.old_data.append(cell_obj.value)
            # print(str(self.old_data))
            self.ws = self.wb.create_sheet(sheet_name)
        else:
            self.wb = openpyxl.Workbook()
            sheet_namess = self.wb.sheetnames
            ss_sheet1 = self.wb[sheet_namess[0]]
            ss_sheet1.title = sheet_name
            self.wb.save(src)
            self.ws = self.wb[sheet_name]
        mylist = ['titulo del producto', 'URL', 'nº reviews past 15 days', 'nº reviews past 30 days']
        self.ws.append(mylist)
        self.wb.save(src)
        self.dest = destination
        self.row_dest = 1

    # Write the value in the cell defined by row_dest+column_dest
    def write_workbook(self, column_dest, value):
        c = self.ws.cell(row=self.row_dest, column=column_dest)
        c.value = value
        self.row_dest = self.row_dest + 1

    # Save excel file
    def save_excel(self):
        self.wb.save(self.dest)

    def load_info(self):
        for worksheet in self.wb:
            print(worksheet.name)
