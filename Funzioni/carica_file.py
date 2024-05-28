from . import AperturaFile
from tkinter import filedialog

class CaricaFile:

    def __init__(self ):
        pass

    def file_input_sfoglia(self):
        path_in = filedialog.askopenfilename()
        if path_in:  # Aggiorna il Label solo se è stato selezionato un file
            df=AperturaFile(path_in).Apertura() 
            tempo = list(df.iloc[:, 0].unique())

            #ottieni il nome del file da path_in
            path_in = path_in.split("/")[-1]
        return path_in,df, tempo
    