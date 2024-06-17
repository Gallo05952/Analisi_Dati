'''
MODULO CHE PERMETTE DI CARICARE UN FILE .CSV O .XLSX
'''

from . import AperturaFile
from tkinter import filedialog
from tkinter import messagebox
import os
class CaricaFile:

    def __init__(self ):
        pass

    def file_input_sfoglia(self):
        path_in = filedialog.askopenfilename()
        #se l'estensione di path_in è .csv, esegui il codice corrente

        if path_in:  # Aggiorna il Label solo se è stato selezionato un file
            if path_in.endswith('.csv'):
                df=AperturaFile(path_in).Apertura()
                tempo = list(df.iloc[:, 0])
            elif path_in.endswith('.xlsx'):
                print("file xlsx")
                df=AperturaFile(path_in).Apertura()
                tempo = list(df.iloc[:, 0])
            else:
                messagebox.showerror("Errore", "Il file selezionato non è valido")
                return None, None, None

            #ottieni il nome del file da path_in
            path_in = path_in.split("/")[-1]
            print(tempo)
        return path_in,df, tempo
    