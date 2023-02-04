from PyPDF2 import PdfReader


class PDFdata:
    def __init__(self, pdf_file_path):
        self.pdf_file_path = pdf_file_path
        self.reader = PdfReader(pdf_file_path)
        
    def get_presencetime(self):
        for i in range(len(self.reader.pages)):
            self.page = self.reader.pages[i]
            text = self.page.extract_text()
            if "Präsenzzeit:" in text:
                # Split the text at "Präsenzzeit:" and keep only the second part
                text = text.split("Präsenzzeit:")[1]
                # Split the text again at the first space character
                number_text = text.split(" ")[0]
                # Try to convert the string to an integer
                try:
                    presence_time = int(number_text)
                    return presence_time
                except ValueError:
                    print("Could not parse Präsenzzeit.")
                    return None
            elif "Attendance time:" in text:
                # Split the text at "Attendance time:" and keep only the second part
                text = text.split("Attendance time:")[1]
                # Split the text again at the first space character
                number_text = text.split(" ")[0]
                # Try to convert the string to an integer
                try:
                    presence_time = int(number_text)
                    return presence_time
                except ValueError:
                    print("Could not parse Attendance time.")
                    return None
        else:
            print("Neither Präsenzzeit nor Attendance time found in the PDF")
                
    def get_selfstudytime(self):
        for i in range(len(self.reader.pages)):
            self.page = self.reader.pages[i]
            text = self.page.extract_text()
            if "Selbststudium:" in text:
                # Split the text at "Selbststudium:" and keep only the second part
                text = text.split("Selbststudium:")[1]
                # Split the text again at the first space character
                number_text = text.split(" ")[0]
                # Try to convert the string to an integer
                try:
                    selfstudytime = int(number_text)
                    return selfstudytime
                except ValueError:
                    print("Could not parse Selbststudium.")
                    break       
            elif "Self-study time:" in text:
                # Split the text at "Self-study time:" and keep only the second part
                text = text.split("Self-study time:")[1]
                # Split the text again at the first space character
                number_text = text.split(" ")[0]
                # Try to convert the string to an integer
                try:
                    presence_time = int(number_text)
                    return presence_time
                except ValueError:
                    print("Could not parse Self-study time.")
                    return None
        else:
            print("Neither Präsenzzeit nor Self-study time found in the PDF")
         
                
    def get_sws(self):
        for i in range(len(self.reader.pages)):
            self.page = self.reader.pages[i]
            text = self.page.extract_text()
            # Nach "SWS" suchen
            if "SWS" in text:
                # Text vor oder nach "SWS" finden und in Module_SWS speichern
                module_sws = text.split("SWS")[0].strip()[-1:]# + text.split("SWS")[1].strip()[:1]
                module_sws = int(module_sws)
                return module_sws
            elif "WLH" in text:
                # Text vor oder nach "WLH" finden und in module_sws speichern
                module_sws = text.split("WLH")[0].strip()[-1:]
                module_sws = int(module_sws)
                return module_sws
        else:
            return None
    get


                
       
        
print("------------------------")
pdf_data = PDFdata("single_Module/Modul B.Inf.1206.pdf") 
print("SWS: " + str(pdf_data.get_sws()))
print("Präsenzzeit: " + str(pdf_data.get_presencetime()))
print("Selbststudium: " + str(pdf_data.get_selfstudytime()))






print("------------------------")
