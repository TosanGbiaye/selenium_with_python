# 6:55 - 7:07
# 1. enter the command: pip instal xlrd on your command prompt
# 2. Create an excel file input some data and save it
# 3 import xlrd on your pycharm 4. give the location of your excel file and add the file name.xlsx
# 5. change the slash to forward slash
import pandas
import xlrd
import pandas as pd
loc = pd.read_excel("C:/Users/hp/Documents/TAS/DataDriven.xlsx", engine='openpyxl')

#loc ="C:/Users/hp/Documents/TAS/DataDriven.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

p1 = sheet.cell(1, 0).value
print(p1)

print(sheet.nrows)
print(sheet.ncols)
