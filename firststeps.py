import tabula
import pandas as pd

pdf_file = 'ModuleDS7.pdf'
table = tabula.read_pdf(pdf_file, pages= "15")
print("------------------------------------------------------------------------------------------------------------------------------------")
print(table)
print("------------------------------------------------------------------------------------------------------------------------------------")

import csv

# open the file in the write mode
with open('table.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(table)