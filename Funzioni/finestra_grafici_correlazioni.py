import plotly.express as px
import numpy as np
import tkinter as tk
import tkinter.ttk as ttk 
from tkinter import messagebox
from tkinter import filedialog   

class FinestraGraficiCorrelazioni:

    def __init__(self, root, df, df_filter, df_corr, preferenze):
        self.df = df
        self.df_filter = df_filter
        self.root = root
        self.df_corr = df_corr
        self.preferenze = preferenze

    def Finestra(self):
        self.grafici_correlazioni = tk.Toplevel(self.root)
        self.grafici_correlazioni.title("Finestra Grafici Correlazioni")
        self.grafici_correlazioni.geometry("1000x400")

        self.dati_grezzi=tk.BooleanVar()
        self.dati_filtrati=tk.BooleanVar()

        # label
        self.testoGrafici = tk.Label(self.grafici_correlazioni,
                                    text="Seleziona i dati per il grafico delle correlazioni",
                                    font=("Helvetica", 14),
                                    fg="red")
        self.testoGrafici.grid(row=0, column=0,columnspan=3)

        #empty label
        self.empty_label = tk.Label(self.grafici_correlazioni, text="")
        self.empty_label.grid(row=1, column=0)

        # selezione dei dati
        self.dati_grezzi_cb=tk.Checkbutton(self.grafici_correlazioni, text="Dati grezzi", variable=self.dati_grezzi)
        self.dati_grezzi_cb.grid(row=2, column=0)

        self.dati_filtrati_cb=tk.Checkbutton(self.grafici_correlazioni, text="Dati filtrati", variable=self.dati_filtrati)
        self.dati_filtrati_cb.grid(row=2, column=1)

        # empty label
        self.empty_label = tk.Label(self.grafici_correlazioni, text="")
        self.empty_label.grid(row=3, column=0)

        try:
            self.variabili = list(self.df.columns)
            self.variabile_x1 = tk.StringVar()
            self.variabile_x2 = tk.StringVar()
            self.variabile_x3 = tk.StringVar()
            self.variabile_x4 = tk.StringVar()
            self.variabile_x5 = tk.StringVar()
            self.variabile_y1 = tk.StringVar()
            self.variabile_y2 = tk.StringVar()
            self.variabile_y3 = tk.StringVar()
            self.variabile_y4 = tk.StringVar()
            self.variabile_y5 = tk.StringVar()
            self.corr_graficata = tk.StringVar()
        except AttributeError:
            print("Errore nella creazione delle variabili")

        # seleziona la correlazione da visualizzare
        self.testoCorrelazioni = tk.Label(self.grafici_correlazioni, text="Seleziona la correlazione da visualizzare")
        self.testoCorrelazioni.grid(row=4, column=0, columnspan=2)

        self.x=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.corr_graficata,
                            values=self.preferenze)
        self.x.grid(row=4, column=2)

        # empty label
        self.empty_label = tk.Label(self.grafici_correlazioni, text="")
        self.empty_label.grid(row=5, column=0)

        self.label_x = tk.Label(self.grafici_correlazioni, text="Variabili x")
        self.label_x.grid(row=6, column=0)

        # variabile di cui si vuole visualizzare la correlazione
        self.x1=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_x1,
                            values=self.variabili)
        self.x1.grid(row=6, column=1)

        self.x2=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_x2,
                            values=self.variabili)
        self.x2.grid(row=6, column=2)

        self.x3=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_x3,
                            values=self.variabili)
        self.x3.grid(row=6, column=3)

        self.x4=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_x4,
                            values=self.variabili)
        self.x4.grid(row=6, column=4)

        self.x5=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_x5,
                            values=self.variabili)
        self.x5.grid(row=6, column=5)

        # empty label
        self.empty_label = tk.Label(self.grafici_correlazioni, text="")
        self.empty_label.grid(row=7, column=0)

        self.label_y = tk.Label(self.grafici_correlazioni, text="Variabili y")
        self.label_y.grid(row=8, column=0)

        # variabile y con cui si vuole visualizzare la correlazione
        self.y1=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_y1,
                            values=self.variabili)
        self.y1.grid(row=8, column=1)

        self.y2=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_y2,
                            values=self.variabili)
        self.y2.grid(row=8, column=2)

        self.y3=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_y3,
                            values=self.variabili)
        self.y3.grid(row=8, column=3)

        self.y4=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_y4,
                            values=self.variabili)
        self.y4.grid(row=8, column=4)

        self.y5=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_y5,
                            values=self.variabili)
        self.y5.grid(row=8, column=5)

        # empty label
        self.empty_label = tk.Label(self.grafici_correlazioni, text="")
        self.empty_label.grid(row=9, column=0)

        # bottone per visualizzare il grafico
        self.button = tk.Button(self.grafici_correlazioni, text="Crea Grafico", command=self.CreaGrafico)
        self.button.grid(row=10, column=2)

        # bottone per salvare il grafico
        self.button = tk.Button(self.grafici_correlazioni, text="Salva Grafico", command=self.SalvaGrafico)
        self.button.grid(row=10, column=3)

    def CreaGrafico(self):
        import pandas as pd
        # prendi i dati inseriti nelle combobox
        try:
            x1 = self.variabile_x1.get()
            x2 = self.variabile_x2.get()
            x3 = self.variabile_x3.get()
            x4 = self.variabile_x4.get()
            x5 = self.variabile_x5.get()
            y1 = self.variabile_y1.get()
            y2 = self.variabile_y2.get()
            y3 = self.variabile_y3.get()
            y4 = self.variabile_y4.get()
            y5 = self.variabile_y5.get()
            corr_graficata = self.corr_graficata.get()
        except AttributeError:
            print("Errore nella creazione delle variabili")

        # controlla se i dati grezzi sono stati selezionati
        if self.dati_grezzi.get() == True:
            print("Dati grezzi selezionati")
            # fai un instogramma con le x e le y selezionate
            try:  
                print(type(self.df_corr[0]))
                print(len(self.df_corr[0]))
                print(self.df_corr[0])
                import numpy as np
                x_graf=[x1, x2, x3, x4, x5]
                x_graf = [x for x in x_graf if x != ""]
                y_graf=[y1, y2, y3, y4, y5]
                y_graf = [y for y in y_graf if y != ""]
                # trova l'indice corrispondente delle x in df_corr
                indices_x = [self.variabili.index(x) for x in x_graf if x in self.variabili]
                indices_y = [self.variabili.index(y) for y in y_graf if y in self.variabili]
                df_graf = pd.DataFrame(np.squeeze(self.df_corr[0]))
                # prendi le righe indicate dagli indici_x dal dataframe df_graf


                righe_selezionate = df_graf.iloc[indices_x]

                colonne_selezionate = righe_selezionate.iloc[:,indices_y]
                print(righe_selezionate)
                print(colonne_selezionate)
                # crea il grafico
                fig = px.bar(df_graf)
                messagebox.showinfo("Grafico creato", "Il grafico è stato creato")                
            except AttributeError:
                #visualizza il tipo di errore attraverso il print
                print("Errore nella creazione del grafico:" + str(AttributeError))



    def SalvaGrafico(self):
        pass
                             
