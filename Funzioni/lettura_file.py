
import os
import pandas as pd
import numpy as np
from tkinter import messagebox
class AperturaFile:

    def __init__(self,path):
        self.path = path

    def Apertura(self):
        _, file_extension = os.path.splitext(self.path)
        if file_extension == '.csv':
            df=self.open_csv()
        elif file_extension == '.xlsx':
            messagebox.showerror("Errore", "L'import da .xlsx non è ancora supportato")
        else:
            print(f"Unsupported file extension: {file_extension}")
        return df

    def open_csv(self):
                # Read the Excel file
        with open(self.path, 'r') as f:
            lines = f.readlines()
        data = [line.split('\n') for line in lines]
        # Join the strings in the first row into a single string separated by semicolons
        i=0
        dati=[]
        for i in range(len(data)):
            DatiC=';'.join(data[i])
            dati.append(DatiC.split(';'))

        # Get the first row as column names
        column_names = dati[0]

        # Get the rest of the data excluding the first row
        data_rows = dati[1:]

        # Convert data_rows into a DataFrame using column_names as column headers
        df = pd.DataFrame(data_rows, columns=column_names)
        # Convert all string values to float, replacing commas with periods
        #df.iloc[1:, 2:] = df.iloc[1:, 2:].applymap(lambda x: pd.to_numeric(x.replace(',', '.'), errors='coerce') if isinstance(x, str) else x)
        df.iloc[0:, 1:] = df.iloc[0:, 1:].apply(lambda series: series.map(lambda x: pd.to_numeric(x.replace(',', '.'), errors='coerce') if isinstance(x, str) else x))
        df=df.replace('', np.nan)
        #df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y %H:%M')
        try:
            df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y %H:%M:%S')
        except ValueError:
            df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y %H:%M')
        df['Data'] = df['Data'].dt.strftime('%H:%M')
        return df

    def open_xlsx(self):
        print("Opening XLSX file")
