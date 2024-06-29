import openpyxl as xl
wb = xl.load_workbook("transaction_id.xlsx")
sheet = wb["Sheet1"]
cell = sheet['a1']
cell = sheet.cell(1,1)


for row in range (2, sheet.max_row + 1):
    cell = sheet.cell(row, 3)
    cell2 = cell.value
    corrected_price = (cell2 * 0.9)
    corrected_price_cell = sheet.cell(row, 5)
    corrected_price_cell.value = corrected_price


wb.save('transaction2.xlsx')


