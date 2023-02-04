# Import the PdfReader module from PyPDF2
from PyPDF2 import PdfReader

# Set the file path of the PDF
pdf_file_path = "single_Module/Modul B.Inf.1302.pdf"

# Read the PDF using the PdfReader
reader = PdfReader(pdf_file_path)

# Open a new text file to write the contents of the PDF
with open("longtext.txt", "w") as f:
    # Loop through all pages in the PDF
    for i in range(len(reader.pages)):
        # Get the current page
        page = reader.pages[i]
        # Write the text of the current page to the text file
        f.write(page.extract_text())
        # Print the text of the current page
        print(page.extract_text())
        
        # Check if the word "SWS" appears in the text of the page
        if "SWS" in page.extract_text():
            # Get the text before and after "SWS"
            text_before_sws = page.extract_text().split("SWS")[0]
            text_after_sws = page.extract_text().split("SWS")[1]
            
            # Get the number before or after "SWS"
            before_sws = text_before_sws.split()[-1]
            after_sws = text_after_sws.split()[0]
            
            # Try to convert the number to an integer
            try:
                before_sws = int(before_sws)
                module_sws = before_sws
            except ValueError:
                try:
                    after_sws = int(after_sws)
                    module_sws = after_sws
                except ValueError:
                    # If the number can't be converted to an integer, set module_sws to None
                    module_sws = None
            
            # Print the value of module_sws
            print("Module SWS:", module_sws)
