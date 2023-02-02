import xlsxwriter
import os, requests

url = 'https://i.etsystatic.com/30535373/r/il/bd3c4e/3497447810/il_340x270.3497447810_o6y2.jpg'
with open(os.path.join(f'test.jpg'), 'wb') as f:
    f.write(requests.get(url, verify=False).content)
# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('nuevo.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 30)

# Insert an image.
worksheet.write('A2', 'Insert an image in a cell:')
worksheet.insert_image('B2', 'test.jpg')

# Insert an image offset in the cell.
worksheet.write('A12', 'Insert an image with an offset:')
worksheet.insert_image('B12', 'test.jpg', {'x_offset': 15, 'y_offset': 10})

# Insert an image with scaling.
worksheet.write('A23', 'Insert a scaled image:')
worksheet.insert_image('B23', 'python.png', {'x_scale': 0.5, 'y_scale': 0.5})

os.remove('test.jpg')

workbook.close()
