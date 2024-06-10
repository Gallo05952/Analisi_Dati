import plotly.express as px
import numpy as np
import tkinter as tk
import tkinter.ttk as ttk 
from tkinter import messagebox
from tkinter import filedialog   
from .styles import Styles

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
        self.grafici_correlazioni.geometry("1000x300")

        self.dati_grezzi=tk.BooleanVar()
        self.dati_grezzi.trace('w', self.update_checkboxes)
        self.dati_filtrati=tk.BooleanVar()
        self.dati_filtrati.trace('w', self.update_checkboxes)

        # label
        self.testoGrafici = tk.Label(self.grafici_correlazioni,
            text="Seleziona i dati per il grafico delle correlazioni",
            font=("Helvetica", 14),
            fg="red")
        self.testoGrafici.grid(row=0, column=0,columnspan=5)

        #empty label
        self.empty_label = tk.Label(self.grafici_correlazioni, text="")
        self.empty_label.grid(row=1, column=0)

        # selezione dei dati
        self.dati_grezzi_cb=ttk.Checkbutton(self.grafici_correlazioni, 
                                        text="Dati grezzi", variable=self.dati_grezzi,
                                        style="Style1.TButton")
        self.dati_grezzi_cb.grid(row=2, column=0)

        self.dati_filtrati_cb=ttk.Checkbutton(self.grafici_correlazioni,
                                            text="Dati filtrati", variable=self.dati_filtrati,
                                            style="Style1.TButton")
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
        self.testoCorrelazioni = ttk.Label(
            self.grafici_correlazioni,
            text="Seleziona la correlazione da visualizzare",
            font=("Helvetica", 14))
        self.testoCorrelazioni.grid(row=4, column=0, columnspan=3)

        self.x=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.corr_graficata,
                            values=self.preferenze,
                            state="readonly")
        self.x.grid(row=4, column=3)

        # empty label
        self.empty_label = tk.Label(self.grafici_correlazioni, text="")
        self.empty_label.grid(row=5, column=0)

        self.label_x = ttk.Label(
            self.grafici_correlazioni,          
            text="Variabili x",
            font=("Helvetica", 14))
        self.label_x.grid(row=6, column=0)

        # variabile di cui si vuole visualizzare la correlazione
        self.x1=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_x1,
                            values=self.variabili,
                            state="readonly")
        self.x1.grid(row=6, column=1)

        self.x2=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_x2,
                            values=self.variabili,
                            state="readonly")
        self.x2.grid(row=6, column=2)

        self.x3=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_x3,
                            values=self.variabili,
                            state="readonly")
        self.x3.grid(row=6, column=3)

        self.x4=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_x4,
                            values=self.variabili,
                            state="readonly")
        self.x4.grid(row=6, column=4)

        self.x5=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_x5,
                            values=self.variabili,
                            state="readonly")
        self.x5.grid(row=6, column=5)

        # empty label
        self.empty_label = tk.Label(self.grafici_correlazioni, text="")
        self.empty_label.grid(row=7, column=0)

        self.label_y = tk.Label(
            self.grafici_correlazioni, 
            text="Variabili y",
            font=("Helvetica", 14))
        self.label_y.grid(row=8, column=0)

        # variabile y con cui si vuole visualizzare la correlazione
        self.y1=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_y1,
                            values=self.variabili,
                            state="readonly")
        self.y1.grid(row=8, column=1)

        self.y2=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_y2,
                            values=self.variabili,
                            state="readonly")
        self.y2.grid(row=8, column=2)

        self.y3=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_y3,
                            values=self.variabili,
                            state="readonly")
        self.y3.grid(row=8, column=3)

        self.y4=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_y4,
                            values=self.variabili,
                            state="readonly")
        self.y4.grid(row=8, column=4)

        self.y5=ttk.Combobox(self.grafici_correlazioni,
                            textvariable=self.variabile_y5,
                            values=self.variabili,
                            state="readonly")
        self.y5.grid(row=8, column=5)

        # empty label
        self.empty_label = tk.Label(self.grafici_correlazioni, text="")
        self.empty_label.grid(row=9, column=0)

        # bottone per visualizzare il grafico
        self.button = tk.Button(
            self.grafici_correlazioni,
            text="Crea Grafico",
            command=self.CreaGrafico,
            font=("Helvetica", 12))
        self.button.grid(row=10, column=2)

        # bottone per salvare il grafico
        self.button_save = tk.Button(
            self.grafici_correlazioni,
            text="Salva Grafico",
            command=self.SalvaGrafico,
            font=("Helvetica", 12))
        self.button_save.grid(row=10, column=3)

    def CreaGrafico(self):
        import pandas as pd
        # prendi i dati inseriti nelle combobox
        global fig
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
                import numpy as np
                x_graf=[x1, x2, x3, x4, x5]
                x_graf = [x for x in x_graf if x != ""]
                filtred_df_grezzo=self.df[x_graf]

                corr_long = self.df.unstack().reset_index()
                corr_long.columns = ['Variable 1', 'Variable 2', 'Correlation']

                # Creazione del barplot con Plotly
                fig = px.bar(corr_long, x='Variable 1', y='Correlation', color='Variable 2', barmode='group')
                # crea il grafico
                fig.show()
                messagebox.showinfo("Grafico creato", "Il grafico è stato creato")
            except AttributeError:
                #visualizza il tipo di errore attraverso il print
                print("Errore nella creazione del grafico:" + str(AttributeError))
        if self.dati_filtrati.get() == True:
            if self.df_corr[1] == None:
                messagebox.showinfo("Errore", "Non ci sono dati filtrati")
            else:
                try:  
                    import numpy as np
                    x_graf=[x1, x2, x3, x4, x5]
                    x_graf = [x for x in x_graf if x != ""]
                    y_graf=[y1, y2, y3, y4, y5]
                    y_graf = [y for y in y_graf if y != ""]
                    # trova l'indice corrispondente delle x in df_corr
                    indices_x = [self.variabili.index(x) for x in x_graf if x in self.variabili]
                    indices_y = [self.variabili.index(y) for y in y_graf if y in self.variabili]
                    df_graf = pd.DataFrame(np.squeeze(self.df_corr[1]))

                    righe_selezionate = df_graf.iloc[indices_x]
                    # Riassegna i nomi delle righe

                    colonne_selezionate = righe_selezionate.iloc[:,indices_y]
                    colonne_selezionate.index = x_graf

                    # Riassegna i nomi delle colonne
                    colonne_selezionate.columns = y_graf

                    corr_long = colonne_selezionate.unstack().reset_index()
                    corr_long.columns = ['Variable 1', 'Variable 2', 'Correlation']
            # Creazione del barplot con Plotly
                    fig = px.bar(corr_long, x='Variable 1', y='Correlation', color='Variable 2', barmode='group')
                    # crea il grafico
                    fig.show()
                    messagebox.showinfo("Grafico creato", "Il grafico è stato creato")                
                except AttributeError:
                    #visualizza il tipo di errore attraverso il print
                    print("Errore nella creazione del grafico:" + str(AttributeError))
                    
    # def SalvaGrafico(self):
    #     # fig è una variabile globale
    #     # apri una nuova finestra dove indicare percorso e nome del file
    #     save_level=tk.Toplevel()
    #     save_level.title("Salva Grafico")
    #     save_level.geometry("400x200")

    #     # label
    #     label = tk.Label(save_level, text="Inserisci il nome del file")
    #     label.grid(row=0, column=0)

    #     # entry
    #     entry = tk.Entry(save_level)
    #     entry.grid(row=0, column=1)

    #     # button sfoglia per indicare il percorso
    #     button = tk.Button(save_level, text="Sfoglia", command=lambda: self.Sfoglia())
    #     button.grid(row=1, column=0)

    #     # button salva
    #     button = tk.Button(save_level, text="Salva", command=lambda: self.Salva(entry, save_level))
    #     button.grid(row=1, column=1)
    def SalvaGrafico(self):
        # fig è una variabile globale
        # apri una nuova finestra dove indicare percorso e nome del file
        save_level=tk.Toplevel()
        save_level.title("Salva Grafico")
        save_level.geometry("600x200")

        # label
        label = tk.Label(save_level, 
                        text="Inserisci il nome del file",
                        font=("Helvetica", 14))
        label.grid(row=0, column=0)

        # entry
        entry = tk.Entry(save_level)
        entry.grid(row=0, column=1)

        #empty label
        empty_label = tk.Label(save_level, text="")
        empty_label.grid(row=1, column=0)


        # button sfoglia per indicare il percorso
        button = tk.Button(save_level,
                        text="Sfoglia",
                        command=lambda: self.Sfoglia(entry),
                        font=("Arial", 12))
        button.grid(row=2, column=0)

        #label percorso
        self.label_out = tk.Label(save_level,
                                text="Percorso:",
                                font=("Arial", 12))
        self.label_out.grid(row=2, column=1)

        # button salva
        button = tk.Button(save_level,
                        text="Salva",
                        command=lambda: self.Salva(entry, save_level),
                        font=("Arial", 12))
        button.grid(row=3, column=1)

    def Sfoglia(self, entry):
        self.path_out = filedialog.askdirectory()
        path = self.path_out.split("/")[-1]  # No need to call copy() on a string
        self.label_out.config(text=path)
        
    # def Salva(self, entry, save_level):
    #     nome=entry.get()
    #     fig.write_html(path + nome + ".html")
    #     messagebox.showinfo("Salvataggio", "Grafico salvato correttamente")
    #     entry.delete(0, tk.END)
    #     save_level.destroy()
    def Salva(self, entry, save_level):
        nome_file = entry.get()
        fig.write_html(self.path_out + "\\" + nome_file + ".html")
        messagebox.showinfo("Salvataggio", "Grafico salvato correttamente")
        entry.delete(0, tk.END)
        save_level.destroy()

    def update_checkboxes(self, *args):
        if self.dati_grezzi.get():
            self.dati_filtrati_cb.config(state='disabled')
        elif self.dati_filtrati.get():
            self.dati_grezzi_cb.config(state='disabled')
        else:
            self.dati_grezzi_cb.config(state='normal')
            self.dati_filtrati_cb.config(state='normal')