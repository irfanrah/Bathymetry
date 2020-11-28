import xlsxwriter
import time
from time import strftime 


waktu = strftime("%H:%M:%S")

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook(waktu+'.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
worksheet.write(1, 2, 'Sumbu X')
worksheet.write(1, 3, 'Sumbu Y')
worksheet.write(1, 4, 'Time')


# Start from the first cell. Rows and columns are zero indexed.
row = 2
col = 2

try:
	for sby in range(1,10):
		for sbx in range(1,10):
			worksheet.write(row,col,sby)
			worksheet.write(row, col + 1, sbx)
			waktuUpdate = strftime("%H:%M:%S")
			worksheet.write(row, col + 2, waktuUpdate)
			row += 1
			time.sleep(0.5)
except KeyboardInterrupt:
    workbook.close()



