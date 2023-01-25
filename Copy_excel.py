from openpyxl import load_workbook


# Class to manage excel data with openpyxl.

class Copy_excel:
    def __init__(self, src, destination):
        self.wb = load_workbook(src)
        self.ws = self.wb.active
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
