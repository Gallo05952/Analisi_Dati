import tkinter as tk
from tkinter import messagebox,filedialog,ttk
import os
import numpy as np

class FinestraSalvataggio:

    def __init__(self, root, df, df_filtrato, df_statistiche,df_corr, preferenze,df_distribuzioni,pref_distribuzioni):
        self.root = root
        self.df = df
        self.df_filtrato = df_filtrato
        self.df_statistiche = df_statistiche
        self.df_corr = df_corr
        self.preferenze = preferenze
        self.df_distribuzioni = df_distribuzioni
        self.pref_distribuzioni = pref_distribuzioni
        self.percorso_path = None
        self.nomefile_entry = None
        self.lim_valvolaSfiato_var = None
        self.limite_ASKI_var = None
        self.T_Aski = None
        self.gestione_scaldiglia_var = None
        self.Valv_min = None
        self.Valv_max = None
        self.Valv_min_A = None
        self.Valv_max_A = None
        self.val_mass = None
        self.val_pot = None
        self.percorso = None
    
    def Finestra(self):
        self.finestra_salva = tk.Toplevel(self.root)
        self.finestra_salva.title("Finestra Salvataggio")
        self.finestra_salva.geometry("1500x600")
        
        # SEZIONE SALVATAGGIO
        testoSalva = tk.Label(self.finestra_salva,
                            text="Salva i dati",
                            font=("Helvetica", 18, "bold"),
                            fg="red")
        testoSalva.grid(row=0, column=0, columnspan=3)
        
        # riga per inserire il nome del file
        nomefile = tk.Label(self.finestra_salva,
                            text="Nome del file",
                            font=("Helvetica", 14),
                            fg="red")
        nomefile.grid(row=1, column=0)

        self.nomefile_entry = tk.Entry(self.finestra_salva)
        self.nomefile_entry.grid(row=1, column=1)

        # riga per selezionare il percorso
        percorso = tk.Label(self.finestra_salva,
                            text="Percorso",
                            font=("Helvetica", 14),
                            fg="red")
        percorso.grid(row=2, column=0)

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
        self.lim_valvolaSfiato_var = tk.BooleanVar()
        self.limite_ASKI_var = tk.BooleanVar()
        self.salva_disrtibuzioni = tk.BooleanVar()
        self.salva_disrtibuzioni_filt = tk.BooleanVar()

        self.salva_grezzi_cb = tk.Checkbutton(self.finestra_salva, 
                                            text="Dati grezzi", 
                                            font=("Helvetica", 12),
                                            variable=self.salva_grezzi)
        self.salva_grezzi_cb.grid(row=4, column=0)

        self.salva_filtrati_cb = tk.Checkbutton(self.finestra_salva,
                                        text="Dati filtrati", 
                                        variable=self.salva_filtrati,
                                        font=("Helvetica", 12))
        self.salva_filtrati_cb.grid(row=4, column=1)

        self.salva_statistiche_cb = tk.Checkbutton(self.finestra_salva,
                                        text="Statistiche Grezzi", variable=self.salva_statistiche,
                                        font=("Helvetica", 12))
        self.salva_statistiche_cb.grid(row=5, column=0)

        self.salva_statistiche_filt_cb = tk.Checkbutton(
                                self.finestra_salva,
                                text="Statistiche Filtrati", variable=self.salva_statistiche_filt,
                                font=("Helvetica", 12))
        self.salva_statistiche_filt_cb.grid(row=5, column=1)

        self.salva_correlazioni_cb = tk.Checkbutton(
                        self.finestra_salva, 
                        text="Correlazioni Grezzi", 
                        variable=self.salva_correlazioni,
                        font=("Helvetica", 12))
        self.salva_correlazioni_cb.grid(row=6, column=0)

        self.salva_correlazioni_filt_cb = tk.Checkbutton(
                                self.finestra_salva,
                                text="Correlazioni Filtrati", 
                                variable=self.salva_correlazioni_filt,
                                font=("Helvetica", 12))
        self.salva_correlazioni_filt_cb.grid(row=6, column=1)

        self.salva_distribuzioni_cb = tk.Checkbutton(
                                self.finestra_salva,
                                text="Distribuzioni", 
                                variable=self.salva_disrtibuzioni,
                                font=("Helvetica", 12))
        self.salva_distribuzioni_cb.grid(row=7, column=0)

        self.salva_distribuzioni_filt_cb = tk.Checkbutton(
                                self.finestra_salva,
                                text="Distribuzioni Filtrati", 
                                variable=self.salva_disrtibuzioni_filt,
                                font=("Helvetica", 12)) 
        self.salva_distribuzioni_filt_cb.grid(row=7, column=1)

        #empty row
        self.empty = tk.Label(self.finestra_salva, text="")
        self.empty.grid(row=8, column=0)

        # Label condizioni di prova
        condizioni = tk.Label(self.finestra_salva,
                            text="Condizioni di prova",
                            font=("Helvetica", 14),
                            fg="red")
        condizioni.grid(row=4, column=4)

        self.lim_valvolaSfiato = tk.Checkbutton(
            self.finestra_salva, 
            text="Valvola sfiato limitata", 
            font=("Helvetica", 12),
            variable=self.lim_valvolaSfiato_var,
            command=self.check_valvolaSfiato
        )
        self.lim_valvolaSfiato.grid(row=5, column=4)
        
        self.limite_ASKI = tk.Checkbutton(
            self.finestra_salva,
            text="Limite ASKI",
            font=("Helvetica", 12),
            variable=self.limite_ASKI_var,
            command=self.check_limite_ASKI)
        self.limite_ASKI.grid(row=5, column=6)

        label_T_Aski= tk.Label(self.finestra_salva, text="Temperatura ASKI[°C]", font=("Helvetica", 12))
        label_T_Aski.grid(row=8, column=6)
        self.T_Aski = tk.Entry(self.finestra_salva)
        self.T_Aski.grid(row=9, column=6)
        # Creazione della variabile StringVar per memorizzare il valore selezionato
        self.gestione_scaldiglia_var = tk.StringVar()

        # Creazione del Combobox con le opzioni desiderate
        self.gestione_scaldiglia = ttk.Combobox(self.finestra_salva, textvariable=self.gestione_scaldiglia_var, font=("Helvetica", 12))
        self.gestione_scaldiglia['values'] = ("Portata Fissa", "Potenza Fissa", "Equazione")

        # Collegamento dell'evento <<ComboboxSelected>> alla funzione gestioneS
        self.gestione_scaldiglia.bind("<<ComboboxSelected>>", self.gestioneS)
        note_label = tk.Label(self.finestra_salva, text="Inserisci eventuali note:", font=("Helvetica", 14), fg="red")
        note_label.grid(row=10, column=0, columnspan=2)
        self.note_textbox = tk.Text(self.finestra_salva, height=5, width=50)
        self.note_textbox.grid(row=11, column=0, columnspan=3)
        # Posizionamento del Combobox nella griglia
        self.gestione_scaldiglia.grid(row=5, column=8)
        #bottone per salvare
        self.salva = tk.Button(self.finestra_salva,
                                text="Salva", 
                                font=("Helvetica", 14),
                                bg="light grey",
                                command=self.salva)
        self.salva.grid(row=12, column=0)


    def scegli_percorso(self):
        self.percorso = filedialog.askdirectory()
        if self.percorso:
            self.percorso_path.config(text=os.path.basename(self.percorso))
        return self.percorso
        
    def salva(self):
        import pandas as pd
        if self.df_filtrato is not None:
            ora_inizio = self.df_filtrato.iloc[0,0]
            ora_fine = self.df_filtrato.iloc[-1,0]
        else:
            ora_inizio = self.df.iloc[0,0]
            ora_fine = self.df.iloc[-1,0]

        nomefile = self.nomefile_entry.get()
        percorso = self.percorso_path.cget("text")
        GestioneValvolasfiato = self.lim_valvolaSfiato_var.get()
        GestioneASKI = self.limite_ASKI_var.get()
        TAski=self.T_Aski.get()
        GestioneScaldiglia = self.gestione_scaldiglia_var.get()
        # Inizializzazione delle variabili opzionali
        val_min = val_max = val_min_A = val_max_A = None
        if GestioneValvolasfiato:
            val_min = self.Valv_min.get()
            val_max = self.Valv_max.get()
        if GestioneASKI:
            val_min_A = self.Valv_min_A.get()
            val_max_A = self.Valv_max_A.get()
        nomi_df_condizioni = ["Ora inizio","Ora fine","Valvola sfiato limitata", "Apertura minima","Apertura Massima","ASKI limitato","Carico minimo","Carico massimo","Temperatura ASKI","Gestione Scaldiglia"]
        # in base ai checkbox crea gli sheet e salva in xlsx file sulo stesso file
        # Dizionario con i dati selezionati
        data = {
            "Ora inizio": [ora_inizio],
            "Ora fine": [ora_fine],
            "Valvola sfiato limitata": [GestioneValvolasfiato],
            "Apertura minima": [val_min],
            "Apertura Massima": [val_max],
            "ASKI limitato": [GestioneASKI],
            "Carico minimo": [val_min_A],
            "Carico massimo": [val_max_A],
            "Temperatura ASKI": [TAski],
            "Gestione Scaldiglia": [GestioneScaldiglia]
        }
        if GestioneScaldiglia == "Portata Fissa":
            data["Portata massa [kg/h]"] = [self.val_mass.get()]
        elif GestioneScaldiglia == "Potenza Fissa":
            data["Potenza [kW]"] = [self.val_pot.get()]
        else:
            data["Scaldiglia libera"] = [""]
        # Creazione del DataFrame
        df_condizioni = pd.DataFrame(data)
        testo = """
INTERPRETAZIONE DEI RISULTATI:

- Skewness = 0: distribuzione simmetrica (potenzialmente normale)
- Skewness > 0: coda destra più lunga (distribuzione asimmetrica positiva)
- Skewness < 0: coda sinistra più lunga (distribuzione asimmetrica negativa)

- Kurtosis = 3: distribuzione simile a quella normale
- Kurtosis > 3: distribuzione più "appuntita" (più picchiata)
- Kurtosis < 3: distribuzione più "piatta" (meno picchiata)
""" 
        if self.percorso is not None:       
            with pd.ExcelWriter(self.percorso+"/"+nomefile+".xlsx",engine='xlsxwriter') as writer:
                df_condizioni.to_excel(writer, sheet_name="Condizioni di prova")
                workbook = writer.book
                worksheet = writer.sheets["Condizioni di prova"]
                
                # Calcolo della posizione per la casella di testo (sotto il DataFrame)
                if self.note_textbox:
                    start_row_note = len(df_condizioni) + 2  # Aggiungi 2 righe di spazio
                    worksheet.insert_textbox(start_row_note, 0, self.note_textbox.get("1.0", "end"))
                    start_row = len(df_condizioni) + 2  # Aggiungi 2 righe di spazio
                    start_col = 4
                else:
                    start_row = len(df_condizioni) + 2
                
                # Aggiunta della casella di testo nel worksheet
                worksheet.insert_textbox(start_row, start_col, testo, {'width': 400, 'height': 100})
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
                                sheet_name = "Correlazioni Grezzi " + self.preferenze[i]
                                # worksheet = writer.sheets[sheet_name]
                                self.df_corr[0][i].to_excel(writer, sheet_name=sheet_name)
                                worksheet = writer.sheets[sheet_name]
                                self.format_cells(worksheet,writer)
                                # self.df_corr[0][i].to_excel(writer, sheet_name="Correlazioni Grezzi "+ self.preferenze[i])
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
                                sheet_name = "Correlazioni Filtrati " + self.preferenze[j]
                                self.df_corr[1][j].to_excel(writer, sheet_name=sheet_name)
                                worksheet = writer.sheets[sheet_name]
                                self.format_cells(worksheet,writer)
                            # if not self.df_corr[1][j].empty:
                            #     print("Salvataggio correlazioni filtrati 2")
                            #     self.df_corr[1][j].to_excel(writer, sheet_name="Correlazioni Filtrati "+ self.preferenze[j])
                if self.salva_disrtibuzioni.get():
                    print("Salvataggio distribuzione grezzi iniziato")
                    if self.df_distribuzioni[0] is None:
                        messagebox.showinfo("Attenzione", "Non ci sono correlazioni da salvare dei dati grezzi")
                    else:
                        if len(self.df_distribuzioni[0]) == 0:
                            messagebox.showinfo("Attenzione", "Non ci sono correlazioni da salvare dei dati grezzi")
                        else:
                            # Creiamo un dizionario per raccogliere i dati per ogni test
                            test_data = {
                                "Shapiro-Wilk": [],
                                "Kolmogorov-Smirnov": [],
                                "Jarque-Bera": []
                            }
                            data_as_lists_SW = []
                            data_as_lists_KS = []
                            data_as_lists_JB = []
                            # Iteriamo attraverso i DataFrame e raccogliamo i dati per ogni test
                            for df in self.df_distribuzioni[0]:
                                if df is not None:
                                    if "Shapiro-Wilk" in df.columns:
                                        test_data["Shapiro-Wilk"].append(df["Shapiro-Wilk"])
                                        data_as_lists_SW = [serie.tolist() for serie in test_data["Shapiro-Wilk"]]
                                    if "Kolmogorov-Smirnov" in df.columns:
                                        test_data["Kolmogorov-Smirnov"].append(df["Kolmogorov-Smirnov"])
                                        data_as_lists_KS = [serie.tolist() for serie in test_data["Kolmogorov-Smirnov"]]
                                    if "Jarque-Bera" in df.columns:
                                        test_data["Jarque-Bera"].append(df["Jarque-Bera"])
                                        data_as_lists_JB = [serie.tolist() for serie in test_data["Jarque-Bera"]]

                            # Scriviamo i dati raccolti in fogli di lavoro separati
                            nomi_colonne = list(self.df.columns[1:])
                            print("nomi colonne", nomi_colonne)  # 
                            max_length = max(len(data_as_lists_SW), len(data_as_lists_KS), len(data_as_lists_JB),len(nomi_colonne))

# Aggiungi NaN alle liste più corte fino a raggiungere la lunghezza massima
                            data_as_lists_SW.extend([np.nan] * (max_length - len(data_as_lists_SW)))
                            data_as_lists_KS.extend([np.nan] * (max_length - len(data_as_lists_KS)))
                            data_as_lists_JB.extend([np.nan] * (max_length - len(data_as_lists_JB)))
                            nomi_colonne.extend([np.nan] * (max_length - len(nomi_colonne)))
                            # Crea un dizionario con i dati
                            data_dict = {
                                'Variabili': nomi_colonne,
                                'Shapiro-Wilk': data_as_lists_SW,
                                'Kolmogorov-Smirnov': data_as_lists_KS,
                                'Jarque-Bera': data_as_lists_JB
                            }

                            # Crea il DataFrame utilizzando il dizionario
                            df_prova = pd.DataFrame(data_dict)
                            print("df_prova", df_prova)
                            # Converti i valori delle colonne in numerici
                            df_prova['Shapiro-Wilk'] = df_prova['Shapiro-Wilk'].apply(lambda x: x[0] if isinstance(x, list) and len(x) > 0 else float('nan'))
                            df_prova['Kolmogorov-Smirnov'] = df_prova['Kolmogorov-Smirnov'].apply(lambda x: x[0] if isinstance(x, list) and len(x) > 0 else float('nan'))
                            df_prova['Jarque-Bera'] = df_prova['Jarque-Bera'].apply(lambda x: x[0] if isinstance(x, list) and len(x) > 0 else float('nan'))

                            # Assicurati che i valori siano di tipo numerico
                            df_prova['Shapiro-Wilk'] = pd.to_numeric(df_prova['Shapiro-Wilk'], errors='coerce')
                            df_prova['Kolmogorov-Smirnov'] = pd.to_numeric(df_prova['Kolmogorov-Smirnov'], errors='coerce')
                            df_prova['Jarque-Bera'] = pd.to_numeric(df_prova['Jarque-Bera'], errors='coerce')

                            print("df_prova", df_prova)
                            df_prova.to_excel(writer, sheet_name="Distribuzione grezzi")



                if self.salva_disrtibuzioni_filt.get():
                    print("Salvataggio correlazioni filtrati")
                    if self.df_distribuzioni[1] is None:
                        messagebox.showinfo("Attenzione", "Non ci sono correlazioni da salvare dei dati filtrati")
                    else:
                        if len(self.df_distribuzioni[1]) == 0:
                            messagebox.showinfo("Attenzione", "Non ci sono correlazioni da salvare dei dati filtrati")
                        else:
                            # Creiamo un dizionario per raccogliere i dati per ogni test
                            test_data = {
                                "Shapiro-Wilk": [],
                                "Kolmogorov-Smirnov": [],
                                "Jarque-Bera": []
                            }
                            data_as_lists_SW = []
                            data_as_lists_KS = []
                            data_as_lists_JB = []
                            # Iteriamo attraverso i DataFrame e raccogliamo i dati per ogni test
                            for df in self.df_distribuzioni[1]:
                                if df is not None:
                                    if "Shapiro-Wilk" in df.columns:
                                        test_data["Shapiro-Wilk"].append(df["Shapiro-Wilk"])
                                        data_as_lists_SW = [serie.tolist() for serie in test_data["Shapiro-Wilk"]]
                                    if "Kolmogorov-Smirnov" in df.columns:
                                        test_data["Kolmogorov-Smirnov"].append(df["Kolmogorov-Smirnov"])
                                        data_as_lists_KS = [serie.tolist() for serie in test_data["Kolmogorov-Smirnov"]]
                                    if "Jarque-Bera" in df.columns:
                                        test_data["Jarque-Bera"].append(df["Jarque-Bera"])
                                        data_as_lists_JB = [serie.tolist() for serie in test_data["Jarque-Bera"]]

                            # Scriviamo i dati raccolti in fogli di lavoro separati
                            nomi_colonne = list(self.df.columns[1:])
                            print("nomi colonne", nomi_colonne)
                            max_length = max(len(data_as_lists_SW), len(data_as_lists_KS), len(data_as_lists_JB), len(nomi_colonne))

                            # Aggiungi NaN alle liste più corte fino a raggiungere la lunghezza massima
                            data_as_lists_SW.extend([np.nan] * (max_length - len(data_as_lists_SW)))
                            data_as_lists_KS.extend([np.nan] * (max_length - len(data_as_lists_KS)))
                            data_as_lists_JB.extend([np.nan] * (max_length - len(data_as_lists_JB)))
                            nomi_colonne.extend([np.nan] * (max_length - len(nomi_colonne)))

                            # Crea un dizionario con i dati
                            data_dict = {
                                'Variabili': nomi_colonne,
                                'Shapiro-Wilk': data_as_lists_SW,
                                'Kolmogorov-Smirnov': data_as_lists_KS,
                                'Jarque-Bera': data_as_lists_JB
                            }

                            # Crea il DataFrame utilizzando il dizionario
                            df_prova = pd.DataFrame(data_dict)
                            print("df_prova", df_prova)
                            # Converti i valori delle colonne in numerici
                            df_prova['Shapiro-Wilk'] = df_prova['Shapiro-Wilk'].apply(lambda x: x[0] if isinstance(x, list) and len(x) > 0 else float('nan'))
                            df_prova['Kolmogorov-Smirnov'] = df_prova['Kolmogorov-Smirnov'].apply(lambda x: x[0] if isinstance(x, list) and len(x) > 0 else float('nan'))
                            df_prova['Jarque-Bera'] = df_prova['Jarque-Bera'].apply(lambda x: x[0] if isinstance(x, list) and len(x) > 0 else float('nan'))

                            # Assicurati che i valori siano di tipo numerico
                            df_prova['Shapiro-Wilk'] = pd.to_numeric(df_prova['Shapiro-Wilk'], errors='coerce')
                            df_prova['Kolmogorov-Smirnov'] = pd.to_numeric(df_prova['Kolmogorov-Smirnov'], errors='coerce')
                            df_prova['Jarque-Bera'] = pd.to_numeric(df_prova['Jarque-Bera'], errors='coerce')

                            print("df_prova", df_prova)
                            df_prova.to_excel(writer, sheet_name="Distribuzione filtrati")
            messagebox.showinfo("Salvataggio", "Salvataggio completato")
        else:
            messagebox.showinfo("Attenzione", "Selezionare un percorso")

    def format_cells(self,worksheet,writer):
        red_format = writer.book.add_format({'bg_color': '#FFC7CE'})
        green_format = writer.book.add_format({'bg_color': '#C6EFCE'})
        worksheet.conditional_format('A1:Z1000', {'type': 'cell',
                                                    'criteria': '<',
                                                    'value': -0.5,
                                                    'format': red_format})
        worksheet.conditional_format('A1:Z1000', {'type': 'cell',
                                                    'criteria': 'between',
                                                    'minimum': 0.5,
                                                    'maximum': 0.99,
                                                    'format': green_format})
        
    def check_valvolaSfiato(self):
        if self.lim_valvolaSfiato_var.get():
            self.label_min = tk.Label(self.finestra_salva, text="Valore min", font=("Helvetica", 12))
            self.label_min.grid(row=6, column=3)
            self.label_max = tk.Label(self.finestra_salva, text="Valore max", font=("Helvetica", 12))
            self.label_max.grid(row=7, column=3)
            self.Valv_min = tk.Entry(self.finestra_salva)
            self.Valv_max = tk.Entry(self.finestra_salva)
            self.Valv_min.grid(row=6, column=4)
            self.Valv_max.grid(row=7, column=4)
            self
        else:
            if hasattr(self, 'label_min'):
                self.label_min.grid_forget()
            if hasattr(self, 'label_max'):
                self.label_max.grid_forget()
            if hasattr(self, 'Valv_min'):
                self.Valv_min.grid_forget()
            if hasattr(self, 'Valv_max'):
                self.Valv_max.grid_forget()

    def check_limite_ASKI(self):
        if self.limite_ASKI_var.get():
            self.label_min_A = tk.Label(self.finestra_salva, text="Valore min", font=("Helvetica", 12))
            self.label_min_A.grid(row=6, column=5)
            self.label_max_A = tk.Label(self.finestra_salva, text="Valore max", font=("Helvetica", 12))
            self.label_max_A.grid(row=7, column=5)
            self.Valv_min_A = tk.Entry(self.finestra_salva)
            self.Valv_max_A = tk.Entry(self.finestra_salva)
            self.Valv_min_A.grid(row=6, column=6)
            self.Valv_max_A.grid(row=7, column=6)
        else:
            if hasattr(self, 'label_min_A'):
                self.label_min_A.grid_forget()
            if hasattr(self, 'label_max_A'):
                self.label_max_A.grid_forget()
            if hasattr(self, 'Valv_min_A'):
                self.Valv_min_A.grid_forget()
            if hasattr(self, 'Valv_max_A'):
                self.Valv_max_A.grid_forget()

    def gestioneS(self,event=None):
        if self.gestione_scaldiglia_var.get() == "Portata Fissa":
            self.label_val_mass= tk.Label(self.finestra_salva, text="Portata massa [kg/h]", font=("Helvetica", 12))
            self.label_val_mass.grid(row=6, column=7)
            self.val_mass = tk.Entry(self.finestra_salva)
            self.val_mass.grid(row=6, column=8)
        elif self.gestione_scaldiglia_var.get() == "Potenza Fissa":
            self.label_val_pot= tk.Label(self.finestra_salva, text="Potenza [kW]", font=("Helvetica", 12))
            self.label_val_pot.grid(row=6, column=7)
            self.val_pot = tk.Entry(self.finestra_salva)
            self.val_pot.grid(row=6, column=8)
        else:
            #elimina eventuali label presenti inseriti nei due if precedenti
            if hasattr(self, 'label_val_mass'):
                self.label_val_mass.grid_forget()
            if hasattr(self, 'val_mass'):
                self.val_mass.grid_forget()
            if hasattr(self, 'label_val_pot'):
                self.label_val_pot.grid_forget()
            if hasattr(self, 'val_pot'):
                self.val_pot.grid_forget()   