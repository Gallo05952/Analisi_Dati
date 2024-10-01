import tkinter as tk
from scipy.stats import shapiro, normaltest, jarque_bera, kstest
import pandas as pd
class FinestraDistribuzioni:

    def __init__(self, root, df,df_filtrato):
        self.root = root
        self.df = df
        self.df_filtrato = df_filtrato

    def Finestra(self):
        self.finestra_dist = tk.Toplevel(self.root)
        self.finestra_dist.title("Finestra Distribuzioni")
        self.finestra_dist.geometry("350x200")

        # CREAZIONE DELLE VARIABILI PER I CHECKBUTTON
        try:
            self.Shapiro_Wilk_var = tk.BooleanVar()
            self.Kolmogorov_Smirnov_var = tk.BooleanVar()
            self.Jarque_Bera_var = tk.BooleanVar()
            self.Dati_grezzi_var = tk.BooleanVar()
            self.Dati_filtrati_var = tk.BooleanVar()
        except AttributeError:
            print("Errore nella creazione delle variabili per i checkbutton")

        # SEZIONE TEST DI NORMALITA'
        self.testoDist = tk.Label(self.finestra_dist,
                        text="Seleziona il test di normalità",
                        font=("Helvetica", 14, "bold"),
                        fg="red")
        self.testoDist.grid(row=0, column=0, columnspan=3)

        # EMPTY LABEL
        empty_label = tk.Label(self.finestra_dist, text="")
        empty_label.grid(row=1, column=0)

        # CHECK BOX TEST DI NORMALITA'
       
    # TEST DI NORMALITA': SHAPIRO-WILK
        self.Shapiro_Wilk_cb = tk.Checkbutton(self.finestra_dist, 
                                    text="Shapiro-Wilk", 
                                    variable=self.Shapiro_Wilk_var,
                                    font=("Helvetica", 12))
        self.Shapiro_Wilk_cb.grid(row=2, column=0)
        # TEST DI NORMALITA': KOLMOGOROV-SMIRNOV
        self.Kolmogorov_Smirnov_cb = tk.Checkbutton(self.finestra_dist,
                                    text="Kolmogorov-Smirnov", 
                                    variable=self.Kolmogorov_Smirnov_var,
                                    font=("Helvetica", 12))
        self.Kolmogorov_Smirnov_cb.grid(row=3, column=0)
        # TEST DI NORMALITA': JARQUE-BERA
        self.Jarque_Bera_cb = tk.Checkbutton(self.finestra_dist,
                                text="Jarque-Bera",
                                variable=self.Jarque_Bera_var,
                                font=("Helvetica", 12))
        self.Jarque_Bera_cb.grid(row=4, column=0)

        # DATI GREZZI
        self.Dati_grezzi_cb = tk.Checkbutton(
                            self.finestra_dist,
                            text="Dati grezzi",
                            variable=self.Dati_grezzi_var,
                            font=("Helvetica", 12))
        self.Dati_grezzi_cb.grid(row=2, column=1)

        # DATI FILTRATI
        self.Dati_filtrati_cb = tk.Checkbutton(
                            self.finestra_dist,
                            text="Dati filtrati",
                            variable=self.Dati_filtrati_var,
                            font=("Helvetica", 12))
        self.Dati_filtrati_cb.grid(row=3, column=1)

        #empty label
        empty_label = tk.Label(self.finestra_dist, text="")
        empty_label.grid(row=5, column=0)

        # BOTTONE CONFERMA
        self.bottone_conferma = tk.Button(self.finestra_dist,
                                text="Conferma",
                                command=self.Salvataggio,
                                font=("Helvetica", 12))
        self.bottone_conferma.grid(row=5, column=0)

    def Salvataggio(self):
        try:
            self.Shapiro_Wilk_S = self.Shapiro_Wilk_var.get()
            self.Kolmogorov_Smirnov_S = self.Kolmogorov_Smirnov_var.get()
            self.Jarque_Bera_S = self.Jarque_Bera_var.get()
            self.Dati_grezzi_S = self.Dati_grezzi_var.get()
            self.Dati_filtrati_S = self.Dati_filtrati_var.get()
        finally:
            getattr(self.finestra_dist, 'destroy', lambda: None)()

    def get_distr(self):
        # # IMPORT DELLE PREFERENZE
        if self.Dati_grezzi_var.get() == True:
            print("Dati grezzi")
            dist_grezzi=self.DistribuzioneGrezzi()
        else: dist_grezzi=None
        if self.Dati_filtrati_var.get() == True:
            print("Dati filtrati")
            dist_filtrati=self.DistribuzioneFiltrati()
        else: dist_filtrati=None
        preferenze=[]
        if self.Shapiro_Wilk_var.get() == True:
            preferenze.append("Shapiro-Wilk")
        if self.Kolmogorov_Smirnov_var.get() == True:
            preferenze.append("Kolmogorov-Smirnov")
        if self.Jarque_Bera_var.get() == True:
            preferenze.append("Jarque-Bera")
        self.finestra_dist.destroy()
        print(dist_grezzi, dist_filtrati, preferenze)
        return dist_grezzi, dist_filtrati, preferenze

    def DistribuzioneGrezzi(self):
        distribuzione_grezzi = {}
        for col in self.df.columns:
            print(col)
            print(self.df[col])
            # print(self.df[col].name)
            distribuzione_grezzi[col] = self.calcola_distribuzione(self.df[col])
        return distribuzione_grezzi

    def DistribuzioneFiltrati(self):
        distribuzione_filtrati = {}
        for col in self.df_filtrato.columns:
            print(col)
            # print(self.df_filtrato[col].name)
            distribuzione_filtrati[col] = self.calcola_distribuzione(self.df_filtrato[col])
        return distribuzione_filtrati

    # def calcola_distribuzione(self, colonna):
    #     distribuzioni={}
    #     if pd.api.types.is_datetime64_any_dtype(colonna):
    #         print(f"La colonna {colonna.name} è di tipo datetime, salto il calcolo delle distribuzioni.")
    #         return distribuzioni
    #     if self.Shapiro_Wilk_var.get() == True:
    #         print("Shapiro-Wilk")
    #         shapiro_test = shapiro(colonna)
    #         print(shapiro_test)
    #         distribuzioni["Shapiro-Wilk"] = shapiro_test
    #     if self.Kolmogorov_Smirnov_var.get() == True:
    #         print("Kolmogorov-Smirnov")
    #         ks_test = kstest(colonna, 'norm')
    #         print(ks_test)
    #         distribuzioni["Kolmogorov-Smirnov"] = ks_test.pvalue
    #     if self.Jarque_Bera_var.get() == True:
    #         print("Jarque-Bera")
    #         jb_test = jarque_bera(colonna)
    #         print(jb_test)
    #         distribuzioni["Jarque-Bera"] = jb_test
    #     return distribuzioni
    def calcola_distribuzione(self, colonna):
        distribuzioni = {}
        if pd.api.types.is_datetime64_any_dtype(colonna):
            print(f"La colonna {colonna.name} è di tipo datetime, salto il calcolo delle distribuzioni.")
            return distribuzioni
        else:
            #converti la colonna in valori numerici
            colonna = pd.to_numeric(colonna, errors='coerce')
        if not pd.api.types.is_numeric_dtype(colonna):
            print(f"La colonna {colonna.name} non è di tipo numerico, salto il calcolo delle distribuzioni.")
            return distribuzioni
        if self.Shapiro_Wilk_var.get() == True:
            print("Shapiro-Wilk")
            shapiro_test = shapiro(colonna)
            print(shapiro_test)
            distribuzioni["Shapiro-Wilk"] = shapiro_test.pvalue
        if self.Kolmogorov_Smirnov_var.get() == True:
            print("Kolmogorov-Smirnov")
            ks_test = kstest(colonna, 'norm')
            print(ks_test)
            distribuzioni["Kolmogorov-Smirnov"] = ks_test.pvalue
        if self.Jarque_Bera_var.get() == True:
            print("Jarque-Bera")
            jb_test = jarque_bera(colonna)
            print(jb_test)
            distribuzioni["Jarque-Bera"] = jb_test.pvalue
        return distribuzioni

