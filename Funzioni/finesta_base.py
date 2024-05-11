import tkinter as tk
from tkinter import filedialog


class Interfaccia:
        
    def __init__(self,root):
        self.root = root

    def FinestraPrincipale(self):
                
            self.root.title("Finestra Principale")
            self.root.geometry("300x200")

            self.label_titolo= tk.Label(self.root, text="Analisi Dati")
            self.label_titolo.grid(row=0, column=0)

            # Import del file
            self.label_file_in= tk.Label(self.root, text="File da importare")
            self.label_file_in.grid(row=1, column=0)


            self.sfoglia_input=tk.Button(self.root,
                                        text="Seleziona da file",
                                        command=self.file_input_sfoglia)
            

            self.sfoglia_input.grid(row=1, column=1)
            # self.provazz=tk.Button(self.root, text="Prova2", command=self.prova2)
            # self.provazz.grid(row=2, column=0)

            self.path_in = ""

    def file_input_sfoglia(self):
        from . import AperturaFile
        self.path_in = filedialog.askopenfilename()
        if self.path_in:  # Aggiorna il Label solo se è stato selezionato un file
            self.label_file_in.config(text=self.path_in)
            AperturaFile(self.path_in).Apertura()
