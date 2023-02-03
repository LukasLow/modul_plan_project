import os
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("ModuleDS007.pdf")
outputs = {}

if not os.path.exists("single_modules"):
    os.makedirs("single_modules")

for i in range(len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()
    if "Modul" in text:
        unique = text.split("Modul")[1].strip()
        if "verzeichnis" in unique.lower() or len(unique) > 80:
            continue
        unique = "Modul" + unique.split(" - ")[0].strip()
        unique = unique.replace("Module", "Modul")
        unique = unique.replace(" ", "_")
        print(f"Unique value: {unique}")
        if unique not in outputs:
            outputs[unique] = PdfWriter()
        outputs[unique].add_page(page)

for unique, output in outputs.items():
    try:
        unique = unique.replace("_", " ")
        unique = "Modul " + unique.split("Modul")[1].strip()
        print(f"{unique} has {len(output.pages)} pages")
        with open(f"single_modules/{unique}.pdf", "wb") as f:
            output.write(f)
    except Exception as e:
        print(f"Error creating PDF for {unique}: {e}")
