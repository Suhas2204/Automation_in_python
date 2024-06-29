import openpyxl as xl
from openpyxl.styles import Font


wb = xl.load_workbook("transaction_id.xlsx")
sheet = wb["Sheet1"]
# cell = sheet['a1']
cell = sheet.cell(1,1)
bold_font = Font(bold=True)
sheet.delete_cols(4)



for row in range (2, sheet.max_row + 1):
    cell = sheet.cell(row, 3)
    cell2 = cell.value
    corrected_price = (cell2 * 0.9)
    corrected_price_cell = sheet.cell(row, 4)
    corrected_price_cell.value = corrected_price
    corrected_price_cell.font = bold_font



wb.save('transaction2.xlsx')


