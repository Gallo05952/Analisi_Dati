import pandas as pd
import numpy as np

class ConversioneCSV:

    def __init__(self, file):
        self.file = file

    def converti_valore(self, valore):
        try:
            # Try to convert the value to datetime
            data = pd.to_datetime(valore, format='%d/%m/%Y %H:%M', errors='coerce')
            if pd.isnull(data):
                # If the conversion to datetime fails, try to convert the value to float
                return float(valore.replace(',', '.'))
            else:
                # If the conversion is successful, return the hour and minute
                return data.strftime('%H:%M')
        except ValueError:
            # If the conversion to float also fails, return the original value
            return valore

    def csv2data(self):
        # Read the CSV file into a DataFrame
        df = pd.read_csv(self.file, sep='\t', dtype=str)
        print(df)
        # Apply the converti_valore function to each value in the DataFrame
        df = df.applymap(self.converti_valore)

        return df

    def nomi_colonne(self):
        # Read the CSV file into a DataFrame
        df = pd.read_csv(self.file, sep='\t')

        # Return the column names as a list
        return df.columns.tolist()
# import pandas as pd
# import numpy as np
# class ConversioneCSV:

#     def __init__(self,file):
#         self.file = file

#     def csv2data(self):
#         # Read the Excel file
#         with open(self.file, 'r') as f:
#             lines = f.readlines()
#         data = [line.split('\n') for line in lines]
#         # Join the strings in the first row into a single string separated by semicolons
#         i=0
#         dati=[]
#         for i in range(len(data)):
#             DatiC=';'.join(data[i])
#             dati.append(DatiC.split(';'))

#         # Get the first row as column names
#         column_names = dati[0]

#         # Get the rest of the data excluding the first row
#         data_rows = dati[1:]

#         # Convert data_rows into a DataFrame using column_names as column headers
#         df = pd.DataFrame(data_rows, columns=column_names)
#         # Convert all string values to float, replacing commas with periods
#         #df.iloc[1:, 2:] = df.iloc[1:, 2:].applymap(lambda x: pd.to_numeric(x.replace(',', '.'), errors='coerce') if isinstance(x, str) else x)
#         # df.iloc[0:, 0:] = df.iloc[0:, 0:].apply(lambda series: series.map(lambda x: pd.to_numeric(x.replace(',', '.'), errors='coerce') if isinstance(x, str) else x))
#         df = df.fillna('')
#         for col in df.columns:
#             df[col] = df[col].astype(str).apply(lambda x: pd.to_numeric(x.replace(',', '.'), errors='coerce'))
#         df=df.replace('', np.nan)
#         #df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y %H:%M')
#         try:
#             df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y %H:%M:%S')
#         except ValueError:
#             df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y %H:%M')
#         df['Data'] = df['Data'].dt.strftime('%H:%M')
#         return df

#     def nomi_colonne(self):
#         with open(self.file, 'r') as f:
#             lines = f.readlines()
#         data = [line.split('\n') for line in lines]
#         # Join the strings in the first row into a single string separated by semicolons
#         i=0
#         dati=[]
#         for i in range(len(data)):
#             DatiC=';'.join(data[i])
#             dati.append(DatiC.split(';'))

#         # Get the first row as column names
#         column_names = dati[0]

#         # Get the rest of the data excluding the first row
#         data_rows = dati[1:]

#         # Convert data_rows into a DataFrame using column_names as column headers
#         df = pd.DataFrame(data_rows, columns=column_names)
#         column_names2 = df.columns.tolist()
#         return column_names2