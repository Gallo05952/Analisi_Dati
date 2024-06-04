import plotly.express as px
import tkinter as tk
import tkinter.ttk as ttk 
from tkinter import messagebox
from tkinter import filedialog   

class FinestraGraficiProbabilita:

    def __init__(self, root, df, df_filter):
        self.df = df
        self.df_filter = df_filter
        self.root = root

    def Finestra(self):
        self.grafici_probabilita = tk.Toplevel(self.root)
        self.grafici_probabilita.title("Finestra Grafici Probabilità")
        self.grafici_probabilita.geometry("1000x400")

        self.dati_grezzi=tk.BooleanVar()
        self.dati_grezzi.trace('w', self.update_checkboxes)
        self.dati_filtrati=tk.BooleanVar()
        self.dati_filtrati.trace('w', self.update_checkboxes)
        self.variabile_x = tk.StringVar()

        # label
        self.testoGrafici = tk.Label(self.grafici_probabilita,
                                    text="Seleziona la variabili per il grafico",
                                    font=("Helvetica", 14),
                                    fg="red")
        self.testoGrafici.grid(row=0, column=0)

        #empty label
        self.empty_label = tk.Label(self.grafici_probabilita, text="")
        self.empty_label.grid(row=1, column=0)

        # selezione dei dati
        self.dati_grezzi_cb = tk.Checkbutton(self.grafici_probabilita, text="Dati grezzi", variable=self.dati_grezzi)
        self.dati_grezzi_cb.grid(row=2, column=0)

        self.dati_filtrati_cb = tk.Checkbutton(self.grafici_probabilita, text="Dati filtrati", variable=self.dati_filtrati)
        self.dati_filtrati_cb.grid(row=2, column=1)

        # empty label
        self.empty_label = tk.Label(self.grafici_probabilita, text="")
        self.empty_label.grid(row=3, column=0)

        self.variabili = list(self.df.columns)
        self.variabile_x=ttk.Combobox(self.grafici_probabilita, 
                                    textvariable=self.variabile_x,
                                    values=self.variabili)
        self.variabile_x.grid(row=4, column=0)
        
        # empty label
        self.empty_label = tk.Label(self.grafici_probabilita, text="")
        self.empty_label.grid(row=5, column=0)

        self.bottone_grafico = tk.Button(self.grafici_probabilita,
                                        text="Crea Grafico",
                                        command=self.CreaGrafico,
                                        bg="light grey",
                                        font=("Arial", 12),
                                        fg="black")
        self.bottone_grafico.grid(row=6, column=0)

    def CreaGrafico(self):
        import pandas as pd
        global fig
        try:
            x = self.variabile_x.get()
        except:
            messagebox.showerror("Errore", "Seleziona la variabile x")
            return
        if self.dati_grezzi.get():
            print("Dati grezzi")
            print(x)
            print(self.df.columns)
            print(self.df[x])
            try:
                self.df[x] = pd.to_numeric(self.df[x], errors='coerce')  # Converti la colonna in numerico
                fig = px.histogram(self.df, x=x, nbins=int(180/5), marginal="box", title='Distribuzione di probabilità'+x)
                fig.show()
                messagebox.showinfo("Grafico", "Grafico grezzi creato correttamente")
            except Exception as e:
                messagebox.showerror("Errore", e)
        if self.dati_filtrati.get():
            if self.df_filter is None:
                messagebox.showerror("Errore", "Dati filtrati non presenti")
                return
            else:
                print("Dati filtrati")
                print(x)
                try:
                    self.df_filter[x] = pd.to_numeric(self.df_filter[x], errors='coerce')  # Converti la colonna in numerico
                    fig = px.histogram(self.df_filter, x=x, nbins=int(180/5), marginal="box",  title='Distribuzione di probabilità'+x)
                    fig.show()
                    messagebox.showinfo("Grafico", "Grafico filtrato creato correttamente")
                except:
                    messagebox.showerror("Errore", "Errore nella creazione del grafico filtrato")


    def update_checkboxes(self, *args):
        if self.dati_grezzi.get():
            self.dati_filtrati_cb.config(state='disabled')
        elif self.dati_filtrati.get():
            self.dati_grezzi_cb.config(state='disabled')
        else:
            self.dati_grezzi_cb.config(state='normal')
            self.dati_filtrati_cb.config(state='normal')