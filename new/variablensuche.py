from PyPDF2 import PdfReader

pdf_file_path = "single_Module/Modul B.Agr.0375.pdf"
pdf_reader = PdfReader(pdf_file_path)

# Alle Texte aus allen Seiten extrahieren
text = "".join(page.extract_text() for page in pdf_reader.pages)

# Nach "SWS" suchen
if "SWS" in text:
    # Text vor oder nach "SWS" finden und in Module_SWS speichern
    module_sws = text.split("SWS")[0].strip()[-1:]# + text.split("SWS")[1].strip()[:1]
    print(f"Module SWS: {module_sws}")
else:
    print("SWS not found in the PDF text.")


from PyPDF2 import PdfReader

pdf_file_path = "single_Module/Modul B.Agr.0375.pdf"
reader = PdfReader(pdf_file_path)

for i in range(len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()
    if "Präsenzzeit:" in text:
        # Split the text at "Präsenzzeit:" and keep only the second part
        text = text.split("Präsenzzeit:")[1]
        # Split the text again at the first space character
        number_text = text.split(" ")[0]
        # Try to convert the string to an integer
        try:
            presence_time = int(number_text)
            print(f"Präsenzzeit: {presence_time}")
        except ValueError:
            print("Could not parse Präsenzzeit.")
            break
print("------------------------")
print(f"Module SWS: {module_sws}")
print(f"Präsenzzeit: {presence_time}")






# # Nach "Präsenzzeit" suchen
# if "Präsenzzeit" in text:
#     # Text vor oder nach "Präsenzzeit" finden und in Module_SWS speichern
#     module_Preasenzzeit = text.split("Präsenzzeit")[1].strip()[:1]
    
# print(f"Module SWS: {module_sws}")
# print(f"Präsenzzeit: {module_Preasenzzeit}")