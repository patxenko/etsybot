import openpyxl
import urllib3
import io
from openpyxl.drawing.image import Image



# It is not required for one to create a workbook on
# filesystem, therefore creating a virtual workbook
wrkb = openpyxl.Workbook()

# Number of sheets in the workbook (1 sheet in our case)
ws = wrkb.worksheets[0]

# Adding a row of data to the worksheet (used to
# distinguish previous excel data from the image)
ws.append([10, 2010, "Geeks", 4, "life"])

# A wrapper over PIL.Image, used to provide image
# inclusion properties to openpyxl library
http = urllib3.PoolManager()
r = http.request('GET', 'https://i.etsystatic.com/30535373/r/il/bd3c4e/3497447810/il_340x270.3497447810_o6y2.jpg')
image_file = io.BytesIO(r.data)
img = openpyxl.drawing.image.Image(image_file)
img.anchor = 'E2'
img.height = 80
img.width = 80

# Adding the image to the worksheet
# (with attributes like position)
ws.add_image(img)


# Saving the workbook created under the name of out.xlsx
wrkb.save('out.xlsx')