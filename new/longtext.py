from PyPDF2 import PdfReader

reader = PdfReader("ModuleDS007.pdf")

with open("longtext.txt", "w") as f:
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        f.write(page.extract_text())
        f.write("\n-----------------------------------------\n")
