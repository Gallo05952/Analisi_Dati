import plotly.express as px
import tkinter as tk
import tkinter.ttk as ttk 
from tkinter import messagebox
from tkinter import filedialog   

class FinestraGraficiBase:
    def __init__(self, root, df, df_filter):
        self.df = df
        self.df_filter = df_filter
        self.root = root

    def Finestra(self):
        self.grafici_base = tk.Toplevel(self.root)
        self.grafici_base.title("Finestra Grafici Variabili")
        self.grafici_base.geometry("900x250")

        self.dati_grezzi=tk.BooleanVar()
        self.dati_grezzi.trace('w', self.update_checkboxes)
        self.dati_filtrati=tk.BooleanVar()
        self.dati_filtrati.trace('w', self.update_checkboxes)

        # label
        self.testoGrafici = tk.Label(self.grafici_base,
                                    text="Seleziona le variabili per il grafico",
                                    font=("Helvetica", 14),
                                    fg="red")
        self.testoGrafici.grid(row=0, column=0, columnspan=6)

        #empty label
        self.empty_label = tk.Label(self.grafici_base, text="")
        self.empty_label.grid(row=1, column=0)

        # selezione dei dati
        self.testoDati = tk.Label(self.grafici_base,
                                text="Seleziona il tipo di dati",
                                font=("Helvetica", 14))
        self.testoDati.grid(row=2, column=0, columnspan=2)

        self.check_dati_grezzi = tk.Checkbutton(self.grafici_base,
                                        text="Dati grezzi",
                                        variable=self.dati_grezzi,
                                        font=("Helvetica", 12)
                                        )
        self.check_dati_grezzi.grid(row=2, column=2)

        self.check_dati_filtrati = tk.Checkbutton(self.grafici_base, 
                                            text="Dati filtrati",
                                            variable=self.dati_filtrati,
                                            font=("Helvetica", 12))
        if self.df_filter is None:
            self.check_dati_filtrati.config(state="disabled")
        self.check_dati_filtrati.grid(row=2, column=3)

        # empty label
        self.empty_label = tk.Label(self.grafici_base, text="")
        self.empty_label.grid(row=3, column=0)

        label_variabili=tk.Label(self.grafici_base,
                                text="Variabile x:",
                                font=("Helvetica", 12, "bold"),
                                fg="green")
        label_variabili.grid(row=4, column=0)

        label_variabili=tk.Label(self.grafici_base,
                                text="Variabili y:",
                                font=("Helvetica", 12, "bold"),
                                fg="blue")
        label_variabili.grid(row=4, column=1)

        try:
            # print(self.df_filter.columns)
            self.variabili = list(self.df.columns)
            self.variabile_x = tk.StringVar()
            self.variabile_y1 = tk.StringVar()
            self.variabile_y2 = tk.StringVar()
            self.variabile_y3 = tk.StringVar()
            self.variabile_y4 = tk.StringVar()
            self.variabile_y5 = tk.StringVar()
        except AttributeError:
            print("Errore nella creazione delle variabili")
        #
        self.x=ttk.Combobox(self.grafici_base,
                            textvariable=self.variabile_x,
                            values=self.variabili)
        self.x.grid(row=5, column=0)

        self.y1 = ttk.Combobox(self.grafici_base,
                                textvariable=self.variabile_y1,
                                values=self.variabili) 
        self.y1.grid(row=5, column=1)

        self.y2 = ttk.Combobox(self.grafici_base,
                                textvariable=self.variabile_y2,
                                values=self.variabili)
        self.y2.grid(row=5, column=2)

        self.y3 = ttk.Combobox(self.grafici_base,
                                textvariable=self.variabile_y3,
                                values=self.variabili)
        self.y3.grid(row=5, column=3)

        self.y4 = ttk.Combobox(self.grafici_base,
                                textvariable=self.variabile_y4,
                                values=self.variabili)
        self.y4.grid(row=5, column=4)

        self.y5 = ttk.Combobox(self.grafici_base,
                                textvariable=self.variabile_y5,
                                values=self.variabili)
        self.y5.grid(row=5, column=5)

        # empty label
        self.empty_label = tk.Label(self.grafici_base, text="")
        self.empty_label.grid(row=6, column=0)

        # button
        self.button = tk.Button(self.grafici_base,
                                text="Crea Grafico",
                                command=self.CreaGrafico,
                                font=("Helvetica", 12))
        self.button.grid(row=7, column=2)

        # bottone salva grafico
        self.button = tk.Button(self.grafici_base,
                                text="Salva Grafico",
                                command=self.SalvaGrafico,
                                font=("Helvetica", 12))
        self.button.grid(row=7, column=3)

    def CreaGrafico(self):
        global fig
        if self.dati_filtrati.get():
            try:
                if self.variabile_x.get() == "" and self.variabile_y1.get() == "" and self.variabile_y2.get() == "" and self.variabile_y3.get() == "" and self.variabile_y4.get() == "" and self.variabile_y5.get() == "":
                    tk.messagebox.showerror("Errore", "Seleziona la variabile x e almeno una variabile y")
                else:
                    if self.variabile_y5.get() == "":
                        fig = px.line(self.df_filter, x=self.variabile_x.get(), y=[self.variabile_y1.get(), self.variabile_y2.get(), self.variabile_y3.get(), self.variabile_y4.get()])
                    elif self.variabile_y4.get() == "":
                        fig = px.line(self.df_filter, x=self.variabile_x.get(), y=[self.variabile_y1.get(), self.variabile_y2.get(), self.variabile_y3.get()])
                    elif self.variabile_y3.get() == "":
                        fig = px.line(self.df_filter, x=self.variabile_x.get(), y=[self.variabile_y1.get(), self.variabile_y2.get()])
                    elif self.variabile_y2.get() == "":
                        fig = px.line(self.df_filter, x=self.variabile_x.get(), y=[self.variabile_y1.get()])
                        
                    fig.show()
            except AttributeError:
                messagebox.showerror("Errore", "Nel creare i grafici delle variabili filtrate")
        elif self.dati_grezzi.get():
            try:
                if self.variabile_x.get() == "" and self.variabile_y1.get() == "" and self.variabile_y2.get() == "" and self.variabile_y3.get() == "" and self.variabile_y4.get() == "" and self.variabile_y5.get() == "":
                    tk.messagebox.showerror("Errore", "Seleziona la variabile x e almeno una variabile y")
                else:
                    if self.variabile_y5.get() == "":
                        fig = px.line(self.df, x=self.variabile_x.get(), y=[self.variabile_y1.get(), self.variabile_y2.get(), self.variabile_y3.get(), self.variabile_y4.get()])
                    elif self.variabile_y4.get() == "":
                        fig = px.line(self.df, x=self.variabile_x.get(), y=[self.variabile_y1.get(), self.variabile_y2.get(), self.variabile_y3.get()])
                    elif self.variabile_y3.get() == "":
                        fig = px.line(self.df, x=self.variabile_x.get(), y=[self.variabile_y1.get(), self.variabile_y2.get()])
                    elif self.variabile_y2.get() == "":
                        fig = px.line(self.df, x=self.variabile_x.get(), y=[self.variabile_y1.get()])
                        
                    fig.show()
            except AttributeError:
                messagebox.showerror("Errore", "Nel creare i grafici delle variabili grezze")

    def SalvaGrafico(self):
        # fig è una variabile globale
        # apri una nuova finestra dove indicare percorso e nome del file
        save_level=tk.Toplevel()
        save_level.title("Salva Grafico")
        save_level.geometry("400x200")

        # label
        label = tk.Label(save_level,
                        text="Inserisci il nome del file",
                        font=("Helvetica", 12))
        label.grid(row=0, column=0)

        # entry
        entry = tk.Entry(save_level)
        entry.grid(row=0, column=1)

        #emèty label
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

    def Salva(self, entry, save_level):
        nome_file = entry.get()
        fig.write_html(self.path_out + "\\" + nome_file + ".html")
        messagebox.showinfo("Salvataggio", "Grafico salvato correttamente")
        entry.delete(0, tk.END)
        save_level.destroy()

    def update_checkboxes(self, *args):
        if self.dati_grezzi.get():
            self.check_dati_filtrati.config(state='disabled')

        elif self.dati_filtrati.get():
            self.check_dati_grezzi.config(state='disabled')

        else:
            self.check_dati_grezzi.config(state='normal')
            self.check_dati_filtrati.config(state='normal')