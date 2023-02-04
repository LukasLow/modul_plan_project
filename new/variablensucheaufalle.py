import os
import time
from variablensuche import PDFdata

pdf_data = PDFdata("single_Module/Modul B.Inf.1204.pdf") 
print("SWS: " + str(pdf_data.get_sws()))
print("Präsenzzeit: " + str(pdf_data.get_presencetime()))
print("Selbststudium: " + str(pdf_data.get_selfstudytime()))


folder = "single_Module"

for pdfFile in os.listdir(folder):
    print(time)
    print("Reading file: " + pdfFile)
    pdf_data = PDFdata(folder + "/" + pdfFile)
    with open("output.txt", "a") as f:
        f.write("File: " + pdfFile + "\n")
        f.write("SWS: " + str(pdf_data.get_sws()) + "\n")
        f.write("Präsenzzeit: " + str(pdf_data.get_presencetime()) + "\n")
        f.write("Credits: " + str(pdf_data.get_credits()) + "\n")
        f.write("Version: " + str(pdf_data.get_version()) + "\n")
        f.write("Maximale Studierendenzahl: " + str(pdf_data.get_maxstudents()) + "\n")
        f.write("Sprache: " + pdf_data.get_language() + "\n")
        f.write("Selbststudium: " + str(pdf_data.get_selfstudytime()) + "\n\n")