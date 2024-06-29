import openpyxl as xl
wb = xl.load_workbook("transaction_id.xlsx")
sheet = wb["Sheet1"]
# cell = sheet['a1']
cell1 = sheet.cell(1,1)
print(cell1)
