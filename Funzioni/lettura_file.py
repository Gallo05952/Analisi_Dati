import os

class AperturaFile:

    def __init__(self,path):
        self.path = path

    def Apertura(self):
        _, file_extension = os.path.splitext(self.path)
        if file_extension == '.csv':
            self.open_csv()
        elif file_extension == '.xlsx':
            self.open_xlsx()
        else:
            print(f"Unsupported file extension: {file_extension}")

    def open_csv(self):
        print("Opening CSV file")

    def open_xlsx(self):
        print("Opening XLSX file")
