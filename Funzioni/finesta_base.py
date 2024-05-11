import tkinter as tk
from tkinter import filedialog


class Interfaccia:
        
    def __init__(self,root):
        self.root = root

    def FinestraPrincipale(self):
                
            self.root.title("Finestra Principale")
            self.root.geometry("500x300")

            self.label_titolo= tk.Label(self.root, text="Analisi Dati")
            self.label_titolo.grid(row=0, column=0)

            # Import del file
            self.label_file_in= tk.Label(self.root, text="File da importare")
            self.label_file_in.grid(row=1, column=0)


            self.sfoglia_input=tk.Button(self.root,
                                        text="Seleziona da file",
                                        command=self.file_input_sfoglia)
            self.sfoglia_input.grid(row=1, column=1)

            self.diversi_progetti = [
                "CD - DisCO2very",
                "CD - COP Aski",
                "Nitrati"]
            self.progetto_selezionata = tk.StringVar(self.root)
            self.menu_a_discesa = tk.OptionMenu(self.root, self.progetto_selezionata, *self.diversi_progetti)
            self.menu_a_discesa.grid(row=1, column=2)

            self.path_in = ""

            # self.chiudi_pulsante = tk.Button(self.root, text="Chiudi", command=self.root.destroy)
            # self.chiudi_pulsante.grid(row=2, column=0)

    def file_input_sfoglia(self):
        from . import AperturaFile
        self.path_in = filedialog.askopenfilename()
        if self.path_in:  # Aggiorna il Label solo se è stato selezionato un file
            self.label_file_in.config(text=self.path_in)
            self.df=AperturaFile(self.path_in).Apertura()