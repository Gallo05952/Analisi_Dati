from .correlazioni import Correlazione
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from .styles import Styles

class FinestraCorrelazioni:

    def __init__(self, root, df,df_filtrato):
        self.root = root
        self.df = df
        self.df_filtrato = df_filtrato

    def Finestra(self):
        self.finestra_corr = tk.Toplevel(self.root)
        self.finestra_corr.title("Finestra Correlazioni")
        self.finestra_corr.geometry("350x200")

        # CREAZIONE DELLE VARIABILI PER I CHECKBUTTON
        try:
            self.Pearson_var = tk.BooleanVar()
            self.Spearman_var = tk.BooleanVar()
            self.Kendall_var = tk.BooleanVar()
            self.Dati_grezzi_var = tk.BooleanVar()
            self.Dati_filtrati_var = tk.BooleanVar()
        except AttributeError:
            print("Errore nella creazione delle variabili per i checkbutton")

        # SEZIONE CORRELAZIONI
        self.testoCorr = tk.Label(self.finestra_corr,
                        text="Seleziona la tipologia di correlazione",
                        font=("Helvetica", 14, "bold"),
                        fg="red")
        self.testoCorr.grid(row=0, column=0, columnspan=3)

        # EMPTY LABEL
        empty_label = tk.Label(self.finestra_corr, text="")
        empty_label.grid(row=1, column=0)

        # CHECK BOX CORRELAZIONI
        try:
        # CORRELAZIONE: PEARSON
            self.Pearson_cb = tk.Checkbutton(self.finestra_corr, 
                                        text="Pearson", 
                                        variable=self.Pearson_var,
                                        font=("Helvetica", 12))
            self.Pearson_cb.grid(row=2, column=0)
            # CORRELAZIONE: SPEARMAN
            # self.Spearman_cb = tk.Checkbutton(self.finestra_corr,
            #                             text="Spearman", 
            #                             variable=self.Spearman_var)
            # self.Spearman_cb.grid(row=2, column=0)
            # CORRELAZIONE: KENDALL
            # self.Kendall_cb = tk.Checkbutton(self.finestra_corr,
            #                         text="Kendall",
            #                         variable=self.Kendall_var)
            # self.Kendall_cb.grid(row=3, column=0)

            # DATI GREZZI
            self.Dati_grezzi_cb = tk.Checkbutton(
                                self.finestra_corr,
                                text="Dati grezzi",
                                variable=self.Dati_grezzi_var,
                                font=("Helvetica", 12))
            self.Dati_grezzi_cb.grid(row=2, column=1)

            # DATI FILTRATI
            self.Dati_filtrati_cb = tk.Checkbutton(
                                self.finestra_corr,
                                text="Dati Filtrati",
                                variable=self.Dati_filtrati_var,
                                font=("Helvetica", 12))
            self.Dati_filtrati_cb.grid(row=3, column=1)
            
            #empty label
            empty_label = tk.Label(self.finestra_corr, text="")
            empty_label.grid(row=4, column=0)
            
                        # BOTTONE CONFERMA
            self.bottone_conferma = tk.Button(
                        self.finestra_corr,
                        text="Conferma",
                        command=lambda: self.Conferma(),
                        bg="light grey",
                        font=("Helvetica", 12),
                        fg="black")
            self.bottone_conferma.grid(row=6, column=0)
        except AttributeError:
            print("Errore nella creazione dei checkbutton")

    def Conferma(self):
        #import delle preferenze
        try:
            self.Pearson_var.get()
            self.Spearman_var.get()
            self.Kendall_var.get()
            self.Dati_grezzi_var.get()
            self.Dati_filtrati_var.get()
        except AttributeError:
            print("Errore nel get delle variabili")
        finally:
            getattr(self.finestra_corr, 'destroy', lambda: None)()

    def get_correlzioni(self):
        correlazioni_filtrate=[]
        correlazioni_grezze=[]
        preferenze=[]
        if self.Dati_grezzi_var.get()==True:
            if self.Pearson_var.get()==True:
                Pearson = Correlazione(self.df).Pearson()
            else:
                Pearson = None
            if self.Spearman_var.get()==True:
                Spearman = Correlazione(self.df).Spearman()
            else:
                Spearman = None
            if self.Kendall_var.get()==True:
                Kendall = Correlazione(self.df).Kendall()
            else:
                Kendall = None
            correlazioni_grezze = Pearson, Spearman, Kendall
            correlazioni_grezze = [i for i in correlazioni_grezze if i is not None]
        else: correlazioni_grezze = None
        if self.Dati_filtrati_var.get()==True:
            if self.df_filtrato is not None:
                if self.Pearson_var.get()==True:
                    Pearson = Correlazione(self.df_filtrato).Pearson()
                else:  
                    Pearson = None
                if self.Spearman_var.get()==True:
                    Spearman = Correlazione(self.df_filtrato).Spearman()
                else:
                    Spearman = None
                if self.Kendall_var.get()==True:
                    Kendall = Correlazione(self.df_filtrato).Kendall()
                else:
                    Kendall = None
                correlazioni_filtrate = Pearson, Spearman, Kendall
                correlazioni_filtrate = [i for i in correlazioni_filtrate if i is not None]
            else:
                messagebox.showerror("Errore", "Nessun filtro selezionato")
        else: correlazioni_filtrate = None
        if self.Pearson_var.get()==True:
            preferenze.append("Pearson")
        if self.Spearman_var.get()==True:
            preferenze.append("Spearman")
        if self.Kendall_var==True:
            preferenze.append("Kendall")
        return correlazioni_grezze, correlazioni_filtrate, preferenze
                
            

