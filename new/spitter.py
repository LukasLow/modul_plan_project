# Import the required library
import os, sys
from PyPDF2 import PdfReader, PdfWriter
sys.stdout = open("output_print_splitter.txt", "w")
# Define the path for the input PDF file
pdf_file = "ModuleDS007.pdf"

# Load the PDF file
pdf_reader = PdfReader(pdf_file)
outputs = {}

# Create a directory for the output files
output_folder = "single_Module"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all pages in the PDF
for i in range(len(pdf_reader.pages)):
    # Get the current page
    page = pdf_reader.pages[i]
    # Extract the text from the current page
    text = page.extract_text()
    # Check if the word "Modul" is in the text
    if "Modul" in text:
        # Get the unique value after the word "Modul"
        unique = text.split("Modul")[1].strip()
        print (unique + "\n\n")
        # Get the first part of the unique value until the ":" or "-"
        if " - " in unique:
            unique = "Modul" + unique.split(" - ")[0].strip()
        elif " : " in unique:
            unique = "Modul" + unique.split(" : ")[0].strip()
        # Skip if the unique value contains the word "verzeichnis" or its length is greater than 80 characters
        if "verzeichnis" in unique.lower() or len(unique) > 120:
            continue
        # Replace "Module" with "Modul"
        unique = unique.replace("Module", "Modul")
        # Replace spaces with underscores
        unique = unique.replace(" ", "_")
        # Print the unique value
        print(f"Unique value: {unique}\n\n\n\n")
        # Create a new PdfWriter for this unique value if it doesn't already exist
        if unique not in outputs:
            outputs[unique] = PdfWriter()
        # Add the current page to the PdfWriter for this unique value
        outputs[unique].add_page(page)

# Loop through all unique values
for unique, output in outputs.items():
    try:
        # Replace underscores with spaces
        unique = unique.replace("_", " ")
        # Add "Modul " before the unique value
        unique = "Modul " + unique.split("Modul")[1].strip()
        # Print the number of pages for this unique value
        print(f"{unique} has {len(output.pages)} pages")
        # Write the PdfWriter for this unique value to a new file in the "output_folder" 
        with open(f"{output_folder}/{unique}.pdf", "wb") as f:
            output.write(f)
    except Exception as e:
        # Print any errors that occur while writing the PDF file
        print(f"Error creating PDF for {unique}: {e}")
        
        
sys.stdout.close()
sys.stdout = sys.__stdout__