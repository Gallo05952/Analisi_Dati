import tkinter as tk
from tkinter import filedialog


class Interfaccia:
        
    def __init__(self,root):
        self.root = root

    def FinestraPrincipale(self):
                
            self.root.title("Finestra Principale")
            self.root.geometry("500x300")

            self.tempo = []

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

            self.pulsante_filtro = tk.Button(
                                self.root,
                                text="Filtra",
                                command=self.FinestraFiltro)
            self.pulsante_filtro.grid(row=2, column=0)
            self.path_in = ""

            # self.chiudi_pulsante = tk.Button(self.root, text="Chiudi", command=self.root.destroy)
            # self.chiudi_pulsante.grid(row=2, column=0)

    def file_input_sfoglia(self):
        from . import AperturaFile
        self.path_in = filedialog.askopenfilename()
        if self.path_in:  # Aggiorna il Label solo se è stato selezionato un file
            self.label_file_in.config(text=self.path_in)
            self.df=AperturaFile(self.path_in).Apertura()
            self.tempo=self.df['Data'].unique()
            print(self.df['Data'])

    def FinestraFiltro(self):
        self.finestra_filtro = tk.Toplevel(self.root)
        self.finestra_filtro.title("Finestra Filtro")
        self.finestra_filtro.geometry("300x200")

        # Creazione delle variabili per i Checkbutton
        self.IntervalloT = tk.BooleanVar()
        self.DaTempo = tk.BooleanVar()

        # Creazione dei Checkbutton
        self.check1 = tk.Checkbutton(self.finestra_filtro, text="Opzione 1", variable=self.IntervalloT)
        self.check1.grid(row=0, column=0)
        self.tempo = list(self.df['Data'].unique())
        self.tempoIN = tk.StringVar(self.finestra_filtro)
        self.Tin = tk.OptionMenu(self.finestra_filtro, self.tempoIN, *self.tempo)
        self.Tin.grid(row=1, column=0)
        self.check2 = tk.Checkbutton(self.finestra_filtro, text="Opzione 2", variable=self.DaTempo)
        self.check2.grid(row=2, column=0)
