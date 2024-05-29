import tkinter as tk
import numpy as np
from tkinter import messagebox
from Funzioni import *

class FinestraStatistiche:

    def __init__(self, root, df,df_filtrato):
        self.root = root
        self.df = df
        self.df_filtrato = df_filtrato
        
    def Finestra(self):
        self.finestra_stat = tk.Toplevel(self.root)
        self.finestra_stat.title("Finestra Statistiche")
        self.finestra_stat.geometry("1000x400")

        # CREAZIONE DELLE VARIABILI PER I CHECKBUTTON
        try:
            self.Media_var = tk.BooleanVar()
            self.Mediana_var = tk.BooleanVar()
            self.Moda_var = tk.BooleanVar()
            self.Deviazione_var = tk.BooleanVar()
            self.Varianza_var = tk.BooleanVar()
            self.minimo_var = tk.BooleanVar()
            self.massimo_var = tk.BooleanVar()
            self.Dati_grezzi_var = tk.BooleanVar()
            self.Dati_filtrati_var = tk.BooleanVar()
        except AttributeError:
            print("Errore nella creazione delle variabili per i checkbutton")

        # SEZIONE STATISTICHE
        self.testoStat = tk.Label(self.finestra_stat,
                            text="Seleziona la tipologia di statistica",
                            font=("Helvetica", 14),
                            fg="red")
        self.testoStat.grid(row=0, column=0)

        # CHECK BOX STATISTICHE
        try:
        # STATISTICA: MEDIA
            self.Media_cb = tk.Checkbutton(self.finestra_stat, 
                                        text="Media", 
                                        font=("Helvetica", 12),
                                        variable=self.Media_var)
            self.Media_cb.grid(row=1, column=0)
            # STATISTICA: MEDIANA
            self.Mediana_cb = tk.Checkbutton(self.finestra_stat,
                                        text="Mediana",
                                        font=("Helvetica", 12),
                                        variable=self.Mediana_var)
            self.Mediana_cb.grid(row=2, column=0)
            # STATISTICA: MODA
            self.Moda_cb = tk.Checkbutton(self.finestra_stat,
                                    text="Moda",
                                    font=("Helvetica", 12),
                                    variable=self.Moda_var)
            self.Moda_cb.grid(row=3, column=0)
            # STATISTICA: DEVIAZIONE STANDARD
            self.Deviazione_cb = tk.Checkbutton(self.finestra_stat,
                                            text="Deviazione Standard", 
                                            font=("Helvetica", 12),
                                            variable=self.Deviazione_var)
            self.Deviazione_cb.grid(row=4, column=0)
            # STATISTICA: VARIANZA
            self.Varianza_cb = tk.Checkbutton(self.finestra_stat, 
                                        text="Varianza", 
                                        font=("Helvetica", 12),
                                        variable=self.Varianza_var)
            self.Varianza_cb.grid(row=5, column=0)
            # STATISTICA: MINIMO
            self.Minimo_cb = tk.Checkbutton(self.finestra_stat,
                                        text="Minimo",
                                        font=("Helvetica", 12),
                                        variable=self.minimo_var)
            self.Minimo_cb.grid(row=6, column=0)
            # STATISTICA: MASSIMO
            self.Massimo_cb = tk.Checkbutton(self.finestra_stat,
                                        text="Massimo",
                                        font=("Helvetica", 12),
                                        variable=self.massimo_var)
            self.Massimo_cb.grid(row=7, column=0)
        except AttributeError:
            print("Errore nel checkbox delle statistiche")

        # CHECK BOX PER LA SELEZIONE DEI DATI
        try:
            # SELEZIONA DATI    
            self.SelezionaDati = tk.Label(self.finestra_stat, 
                        text="Seleziona i dati su cui fare le statistiche",
                        font=("Helvetica", 14, "bold"),
                        fg="red")          
            self.SelezionaDati.grid(row=0, column=3)

            self.Dati_grezzi = tk.Checkbutton(self.finestra_stat, 
                                        text="Dati grezzi", 
                                        font=("Helvetica", 12),
                                        variable=self.Dati_grezzi_var)
            self.Dati_grezzi.grid(row=1, column=3)

            self.Dati_filtrati = tk.Checkbutton(self.finestra_stat,
                                        text="Dati filtrati", 
                                        font=("Helvetica", 12),
                                        variable=self.Dati_filtrati_var)
            self.Dati_filtrati.grid(row=2, column=3)
        except AttributeError:
            print("Errore nel checkbox dei dati")

        # BOTTONE OK E CHIUSURA
        self.ok_button_stat = tk.Button(self.finestra_stat,
                                        text="OK", 
                                        font=("Helvetica", 12),
                                        command=self.SalvataggioStat)
        self.ok_button_stat.grid(row=8, column=2, padx=10, pady=10)

    def SalvataggioStat(self):
        try:
            self.MediaS=self.Media_var.get()
            self.MedianaS=self.Mediana_var.get()
            self.ModaS=self.Moda_var.get()
            self.DeviazioneS=self.Deviazione_var.get()
            self.VarianzaS=self.Varianza_var.get()
            self.minimoS=self.minimo_var.get()
            self.massimoS=self.massimo_var.get()
            self.Dati_grezziS=self.Dati_grezzi_var.get()
            self.Dati_filtratiS=self.Dati_filtrati_var.get()
        except AttributeError:
            print("Errore")
        finally:
            getattr(self.finestra_stat, 'destroy', lambda: None)()

    def get_Stat(self):
        # STATISTICHE SUI DATI GREZZI
        if self.Dati_grezzi_var.get():
            stat_grezze=self.StatisticheGrezzi()
        else:
            stat_grezze=None
        # STATISTICHE SUI DATI FILTRATI
        if self.Dati_filtrati_var.get():
            if self.df_filtrato is not None:
                stat_filtrati=self.StatisticheFiltrati()
            else:
                messagebox.showerror("Errore", "Non hai selezionato ancora nessun filtro")
        else:
            stat_filtrati=None
        self.finestra_stat.destroy()
        return stat_grezze, stat_filtrati

    def Media(self, col):
        try:
            media = self.df[col].mean()
        except:
            media = np.nan
        return media
    
    def Mediana(self, col):
        try:
            mediana = self.df[col].median()
        except:
            mediana = np.nan
        return mediana
    
    def Varianza(self, col):
        try:
            varianza = self.df[col].var()
        except:
            varianza = np.nan
        return varianza
    
    def DeviazioneStandard(self, col):
        try:
            deviazione_standard = self.df[col].std()
        except:
            deviazione_standard = np.nan
        return deviazione_standard

    def Moda(self, col):
        try:
            moda_df = self.df[col].mode(dropna=True)
            if not moda_df.empty:
                moda = moda_df.iloc[0]
            else:
                moda = np.nan
        except:
            moda = np.nan
        return moda

    def Minimo(self, col):
        try:
            minimo = self.df[col].min()
        except:
            minimo = np.nan
        return minimo

    def Massimo(self, col):
        try:
            massimo = self.df[col].max()
        except:
            massimo = np.nan
        return massimo
    
    def StatisticheGrezzi(self):
        statistiche_grezzi = {}
        for col in self.df.columns:
            statistiche_grezzi[col] = self.calcola_statistiche(col)
        return statistiche_grezzi
    
    def StatisticheFiltrati(self):
        statistiche_filtrati = {}
        for col in self.df_filtrato.columns:
            statistiche_filtrati[col] = self.calcola_statistiche(col)
        return statistiche_filtrati
    
    def calcola_statistiche(self, col):
        statistiche = {}
        if self.Media_var.get():
            statistiche["Media"] = self.Media(col)
        if self.Mediana_var.get():
            statistiche["Mediana"] = self.Mediana(col)
        if self.Varianza_var.get():
            statistiche["Varianza"] = self.Varianza(col)
        if self.Deviazione_var.get():
            statistiche["Deviazione Standard"] = self.DeviazioneStandard(col)
        if self.Moda_var.get():
            statistiche["Moda"] = self.Moda(col)
        if self.minimo_var.get():
            statistiche["Minimo"] = self.Minimo(col)
        if self.massimo_var.get():
            statistiche["Massimo"] = self.Massimo(col)
        return statistiche
