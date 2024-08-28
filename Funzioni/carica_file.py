
'''
MODULO CHE PERMETTE DI CARICARE UN FILE .CSV O .XLSX
'''

from . import AperturaFile
from tkinter import filedialog
from tkinter import messagebox
import os
import pandas as pd

class CaricaFile:

    def __init__(self):
        pass

    def file_input_sfoglia(self):
        path_in = filedialog.askopenfilename()
        # se l'estensione di path_in è .csv, esegui il codice corrente

        if path_in:  # Aggiorna il Label solo se è stato selezionato un file
            if path_in.endswith('.csv'):
                df = AperturaFile(path_in).Apertura()
                # Aggiungi un suffisso numerico alle colonne duplicate
                df.columns = self._deduplicate_columns(df.columns)
                tempo = list(df.iloc[:, 0])
            elif path_in.endswith('.xlsx'):
                print("file xlsx")
                df = AperturaFile(path_in).Apertura()
                tempo = list(df.iloc[:, 0])
            else:
                messagebox.showerror("Errore", "Il file selezionato non è valido")
                return None, None, None

            # ottieni il nome del file da path_in
            path_in = os.path.basename(path_in)
        return path_in, df

    def _deduplicate_columns(self, columns):
        new_columns = []
        seen = {}
        for col in columns:
            if col in seen:
                seen[col] += 1
                new_columns.append(f"{col}_{seen[col]}")
            else:
                seen[col] = 0
                new_columns.append(col)
        return new_columns
# '''
# MODULO CHE PERMETTE DI CARICARE UN FILE .CSV O .XLSX
# '''

# from . import AperturaFile
# from tkinter import filedialog
# from tkinter import messagebox
# import os
# import pandas as pd
# class CaricaFile:

#     def __init__(self ):
#         pass

#     # def file_input_sfoglia(self):
#     #     path_in = filedialog.askopenfilename()
#     #     #se l'estensione di path_in è .csv, esegui il codice corrente

#     #     if path_in:  # Aggiorna il Label solo se è stato selezionato un file
#     #         if path_in.endswith('.csv'):
#     #             df=AperturaFile(path_in).Apertura()
#     #             tempo = list(df.iloc[:, 0])
#     #         elif path_in.endswith('.xlsx'):
#     #             print("file xlsx")
#     #             df=AperturaFile(path_in).Apertura()
#     #             tempo = list(df.iloc[:, 0])
#     #         else:
#     #             messagebox.showerror("Errore", "Il file selezionato non è valido")
#     #             return None, None, None

#     #         #ottieni il nome del file da path_in
#     #         path_in = path_in.split("/")[-1]
#     #     return path_in,df


#     def file_input_sfoglia(self):
#         path_in = filedialog.askopenfilename()
#         #se l'estensione di path_in è .csv, esegui il codice corrente

#         if path_in:  # Aggiorna il Label solo se è stato selezionato un file
#             if path_in.endswith('.csv'):
#                 df = AperturaFile(path_in).Apertura()
#                 # Aggiungi un suffisso numerico alle colonne duplicate
#                 df.columns = pd.io.parsers.ParserBase({'names': df.columns})._maybe_dedup_names(df.columns)
#                 tempo = list(df.iloc[:, 0])
#             elif path_in.endswith('.xlsx'):
#                 print("file xlsx")
#                 df = AperturaFile(path_in).Apertura()
#                 tempo = list(df.iloc[:, 0])
#             else:
#                 messagebox.showerror("Errore", "Il file selezionato non è valido")
#                 return None, None, None

#             #ottieni il nome del file da path_in
#             path_in = path_in.split("/")[-1]
#         return path_in, df
    