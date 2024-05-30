import tkinter as tk
from tkinter import messagebox,filedialog


class FinestraSalvataggio:

    def __init__(self, root, df, df_filtrato, df_statistiche,df_corr, preferenze):
        self.root = root
        self.df = df
        self.df_filtrato = df_filtrato
        self.df_statistiche = df_statistiche
        self.df_corr = df_corr
        self.preferenze = preferenze
    
    def Finestra(self):
        self.finestra_salva = tk.Toplevel(self.root)
        self.finestra_salva.title("Finestra Salvataggio")
        self.finestra_salva.geometry("1000x400")
        
        # SEZIONE SALVATAGGIO
        self.testoSalva = tk.Label(self.finestra_salva,
                            text="Salva i dati",
                            font=("Helvetica", 18, "bold"),
                            fg="red")
        self.testoSalva.grid(row=0, column=0, columnspan=3)
        
        # riga per inserire il nome del file
        self.nomefile = tk.Label(self.finestra_salva,
                            text="Nome del file",
                            font=("Helvetica", 14),
                            fg="red")
        self.nomefile.grid(row=1, column=0)

        self.nomefile_entry = tk.Entry(self.finestra_salva)
        self.nomefile_entry.grid(row=1, column=1)

        # riga per selezionare il percorso
        self.percorso = tk.Label(self.finestra_salva,
                            text="Percorso",
                            font=("Helvetica", 14),
                            fg="red")
        self.percorso.grid(row=2, column=0)

        #sfoglial percorso
        self.sfoglia = tk.Button(self.finestra_salva, text="Sfoglia", 
                                font=("Helvetica", 14),
                                bg="light grey",
                                command=self.scegli_percorso)
        self.sfoglia.grid(row=2, column=1)

        #visualizza il percorso
        self.percorso_path = tk.Label(self.finestra_salva,
                                    font=("Helvetica", 14))
        self.percorso_path.grid(row=2, column=2)

        #empty row
        self.empty = tk.Label(self.finestra_salva, text="")
        self.empty.grid(row=3, column=0)

        #checbox per cosa salvare
        self.salva_grezzi = tk.BooleanVar()
        self.salva_filtrati = tk.BooleanVar()
        self.salva_statistiche = tk.BooleanVar()
        self.salva_correlazioni = tk.BooleanVar()
        self.salva_statistiche_filt = tk.BooleanVar()
        self.salva_correlazioni_filt = tk.BooleanVar()

        self.salva_grezzi_cb = tk.Checkbutton(self.finestra_salva, 
                                            text="Dati grezzi", variable=self.salva_grezzi)
        self.salva_grezzi_cb.grid(row=4, column=0)

        self.salva_filtrati_cb = tk.Checkbutton(self.finestra_salva,
                                        text="Dati filtrati", variable=self.salva_filtrati)
        self.salva_filtrati_cb.grid(row=4, column=1)

        self.salva_statistiche_cb = tk.Checkbutton(self.finestra_salva,
                                        text="Statistiche Grezzi", variable=self.salva_statistiche)
        self.salva_statistiche_cb.grid(row=5, column=0)

        self.salva_statistiche_filt_cb = tk.Checkbutton(
                                self.finestra_salva,
                                text="Statistiche Filtrati", variable=self.salva_statistiche_filt)
        self.salva_statistiche_filt_cb.grid(row=5, column=1)

        self.salva_correlazioni_cb = tk.Checkbutton(
                        self.finestra_salva, 
                        text="Correlazioni Grezzi", 
                        variable=self.salva_correlazioni)
        self.salva_correlazioni_cb.grid(row=6, column=0)

        self.salva_correlazioni_filt_cb = tk.Checkbutton(
                                self.finestra_salva,
                                text="Correlazioni Filtrati", 
                                variable=self.salva_correlazioni_filt)
        self.salva_correlazioni_filt_cb.grid(row=6, column=1)

        #empty row
        self.empty = tk.Label(self.finestra_salva, text="")
        self.empty.grid(row=8, column=0)

        #bottone per salvare
        self.salva = tk.Button(self.finestra_salva,
                                text="Salva", 
                                font=("Helvetica", 14),
                                bg="light grey",
                                command=self.salva)
        self.salva.grid(row=9, column=0)


    def scegli_percorso(self):
        percorso = filedialog.askdirectory()
        if percorso:
            self.percorso_path.config(text=percorso)
        return self.percorso
        

    def salva(self):
        import pandas as pd
        nomefile = self.nomefile_entry.get()
        percorso = self.percorso_path.cget("text")
        # in base ai checkbox crea gli sheet e salva in xlsx file sulo stesso file
        with pd.ExcelWriter(percorso+"/"+nomefile+".xlsx") as writer:
            if self.salva_grezzi.get():
                if self.df is None:
                    messagebox.showinfo("Attenzione", "Non ci sono dati grezzi da salvare")
                else:
                    self.df.to_excel(writer, sheet_name="Dati grezzi")
            if self.salva_filtrati.get():
                if self.df_filtrato is None:
                    messagebox.showinfo("Attenzione", "Non ci sono dati filtrati da salvare")
                else:
                    self.df_filtrato.to_excel(writer, sheet_name="Dati filtrati")
            if self.salva_statistiche.get():
                if self.df_statistiche is None:
                    messagebox.showinfo("Attenzione", "Non ci sono statistiche da salvare")
                else:
                    self.df_statistiche[0].to_excel(writer, sheet_name="Statistiche Grezzi")
            if self.salva_statistiche_filt.get():
                if self.df_statistiche is None:
                    messagebox.showinfo("Attenzione", "Non ci sono statistiche da salvare")
                else:
                    self.df_statistiche[1].to_excel(writer, sheet_name="Statistiche Filtrati")
            if self.salva_correlazioni.get():
                if self.df_corr[0] is None:
                    messagebox.showinfo("Attenzione", "Non ci sono correlazioni da salvare dei dati grezzi")
                else:
                    # df_corr è una lista con dentro due liste con dentro potenzialmente 3 dataframe il numero di dataframe lo posso vedere dalla lunghezza di preferenze
                    i=0
                    if len(self.df_corr[0]) == 0:
                        messagebox.showinfo("Attenzione", "Non ci sono correlazioni da salvare dei dati grezzi")
                    for i in range(len(self.df_corr[0])):
                        if self.df_corr[0][i] is not None:
                            self.df_corr[0][i].to_excel(writer, sheet_name="Correlazioni Grezzi "+ self.preferenze[i])
            if self.salva_correlazioni_filt.get():
                print("Salvataggio correlazioni filtrati")
                if self.df_corr[1] is None:
                    messagebox.showinfo("Attenzione", "Non ci sono correlazioni da salvare dei dati filtrati")
                else:
                    j=0
                    if len(self.df_corr[1]) == 0:
                        messagebox.showinfo("Attenzione", "Non ci sono correlazioni da salvare dei dati filtrati")
                    print(len(self.df_corr[1]))
                    for j in range(len(self.df_corr[1])):
                        if not self.df_corr[1][j].empty:
                            print("Salvataggio correlazioni filtrati 2")
                            self.df_corr[1][j].to_excel(writer, sheet_name="Correlazioni Filtrati "+ self.preferenze[j])
        messagebox.showinfo("Salvataggio", "Salvataggio completato")