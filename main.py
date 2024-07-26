import tkinter as tk
from Funzioni import *
import numpy as np
import pandas as pd
from tkinter import messagebox
from PIL import Image, ImageTk

def App(finesta_principale):
    finesta_principale.title("Analisi Dati")
    finesta_principale.geometry("800x450")
    global df_DaUnire, df_MRU, df_MRU_Unito, df_Unito, df_mTp
    df_DaUnire = []
    df_MRU = []
    df_MRU_Unito = pd.DataFrame()
    df_Unito=pd.DataFrame()
    df_mTp=pd.DataFrame()

    # LABEL
    label= tk.Label(finesta_principale,
                    text="Analisi Dati",
                    font=("Arial", 24, "bold"), 
                    fg="green")
    label.grid(row=0, column=0, columnspan=3)

    #EMPTY ROW
    empty_row = tk.Label(finesta_principale, 
                        text="")
    empty_row.grid(row=1, column=0)

    # LABEL FILE IN
    label_file_in = tk.Label(finesta_principale,
                            text="File in: ",
                            font=("Arial", 12))
    label_file_in.grid(row=3, column=0)
    
    #* BOTTONE CARICA FILE
    bottone_carica_file = tk.Button(finesta_principale,
                            text="CSV 1", 
                            command=lambda: Caricamento(label_file_in,
                                        bottone_carica_file,bottone_filtro, bottone_statistiche,
                                        bottone_correlazione, bottone_salva),
                            bg="light grey",
                            font=("Arial", 12),
                            fg="bLACK")
    bottone_carica_file.grid(row=2, column=0)

    #* BOTTONE CARICA FILE
    bottone_carica_file2 = tk.Button(finesta_principale,
                            text="MRU1",
                            command=lambda: CaricamentoMRU(label_file2_in,
                                        bottone_carica_file2),
                            bg="light grey",
                            font=("Arial", 12),
                            fg="black")
    bottone_carica_file2.grid(row=2, column=2)

    # LABEL FILE IN
    label_file2_in = tk.Label(finesta_principale,
                            text="File in: ",
                            font=("Arial", 12))
    label_file2_in.grid(row=3, column=2)

    #* BOTTONE CARICA FILE
    bottone_carica_file3 = tk.Button(finesta_principale,
                            text="MRU2",
                            command=lambda: CaricamentoMRU(label_file3_in,
                                        bottone_carica_file3),
                            bg="light grey",
                            font=("Arial", 12),
                            fg="black")
    bottone_carica_file3.grid(row=2, column=3)

    # LABEL FILE IN
    label_file3_in = tk.Label(finesta_principale,
                            text="File in: ",
                            font=("Arial", 12))
    label_file3_in.grid(row=3, column=3)

    #* BOTTONE CARICA FILE
    bottone_carica_file4 = tk.Button(finesta_principale,
                            text="MRU3",
                            command=lambda: CaricamentoMRU(label_file4_in,
                                        bottone_carica_file4),
                            bg="light grey",
                            font=("Arial", 12),
                            fg="black")
    bottone_carica_file4.grid(row=2, column=4)

    # LABEL FILE IN
    label_file4_in = tk.Label(finesta_principale,
                            text="File in: ",
                            font=("Arial", 12))
    label_file4_in.grid(row=3, column=4)

    #* BOTTONE CARICA FILE
    bottone_carica_file5 = tk.Button(finesta_principale,
                            text="MRU4",
                            command=lambda: CaricamentoMRU(label_file5_in,
                                        bottone_carica_file5),
                            bg="light grey",
                            font=("Arial", 12),
                            fg="black")
    bottone_carica_file5.grid(row=2, column=5)

    # LABEL FILE IN
    label_file5_in = tk.Label(finesta_principale,
                            text="File in: ",
                            font=("Arial", 12))
    label_file5_in.grid(row=3, column=5)

    #* BOTTONE CARICA FILE
    bottone_carica_file6 = tk.Button(finesta_principale,
                            text="MRU5",
                            command=lambda: CaricamentoMRU(label_file6_in,
                                        bottone_carica_file6),
                            bg="light grey",
                            font=("Arial", 12),
                            fg="black")
    bottone_carica_file6.grid(row=2, column=6)

    label_file6_in = tk.Label(finesta_principale,
                            text="File in: ",
                            font=("Arial", 12))
    label_file6_in.grid(row=3, column=6)

    #* BOTTONE CARICA FILE
    bottone_carica_file7 = tk.Button(finesta_principale,
                            text="CSV 2",
                            command=lambda: Caricamento2(label_file7_in,
                                        bottone_carica_file7),
                            bg="light grey",
                            font=("Arial", 12),
                            fg="black")
    bottone_carica_file7.grid(row=2, column=1)

    label_file7_in = tk.Label(finesta_principale,   
                            text="File in: ",
                            font=("Arial", 12))
    label_file7_in.grid(row=3, column=1)

    #* BOTTONE unisci file
    bottone_unisci = tk.Button(finesta_principale,
                            text="Unisci",
                            command=lambda: UnisciFile(),
                            bg="light grey",
                            font=("Arial", 12),
                            fg="black")
    bottone_unisci.grid(row=4, column=1)

    # EMPRY ROW
    empty_row = tk.Label(finesta_principale,
                        text="")
    empty_row.grid(row=5, column=0)

    #* BOTTONE COP
    bottone_cop = tk.Button(finesta_principale,
                        text="COP",
                        command=lambda: CalcoloCOP(bottone_cop),
                        bg="light grey",
                        font=("Arial", 12),
                        fg="black")
    bottone_cop.grid(row=4, column=3)


    #* BOTTONE FILTRO
    bottone_filtro = tk.Button(finesta_principale,
                            text="Filtro",
                            command=lambda: Filtraggio(finesta_principale,bottone_filtro),
                            bg="light grey",
                            font=("Arial", 12),
                            fg="black")
    # bottone_filtro.config(state=tk.DISABLED)
    bottone_filtro.grid(row=6, column=0)

    # EMPTY ROW
    empty_row = tk.Label(finesta_principale,
                        text="")
    empty_row.grid(row=7, column=0)

    #* BOTTONE STATISTICHE
    bottone_statistiche = tk.Button(finesta_principale,
                                    text="Statistiche",
                                    command=lambda: Statistiche(finesta_principale,df_Unito, df_filtrato,bottone_statistiche),
                                    font=("Arial", 12),
                                    bg="light grey",
                                    fg="black")
    # bottone_statistiche.config(state=tk.DISABLED)
    bottone_statistiche.grid(row=8, column=0)

    # EMPTY ROW
    empty_row = tk.Label(finesta_principale,
                        text="")
    empty_row.grid(row=9, column=0)

    #* BOTTONE CORRELAZIONE
    bottone_correlazione = tk.Button(finesta_principale,
                                    text="Correlazione",
                                    command=lambda: Correlzioniamo(finesta_principale, df, df_filtrato, bottone_correlazione),
                                    bg="light grey",
                                    font=("Arial", 12),
                                    fg="black")
    # bottone_correlazione.config(state=tk.DISABLED)
    bottone_correlazione.grid(row=10, column=0)

    # EMPTY ROW
    empty_row = tk.Label(finesta_principale,
                        text="")
    empty_row.grid(row=11, column=0)

    # # BOTTONE GRAFICI VARIABILI
    # bottone_grafici = tk.Button(finesta_principale,
    #                         text="Grafici",
    #                         command=lambda: Grafici_Variabili(),
    #                         bg="light grey",
    #                         font=("Arial", 12),
    #                         fg="black")
    # bottone_grafici.config(state=tk.DISABLED)
    # bottone_grafici.grid(row=6, column=2)

    # # BOTTONE GRAFICI DENSITà DI PROBABILITà
    # bottone_grafici_stat = tk.Button(finesta_principale,
    #                             text="Grafici Probabilità",
    #                             command=lambda: Grafici_Probabilità(),
    #                             bg="light grey",
    #                             font=("Arial", 12),
    #                             fg="black")
    # bottone_grafici_stat.config(state=tk.DISABLED)
    # bottone_grafici_stat.grid(row=8, column=2)

    # # BOTTONE GRAFICI CORRELAZIONE
    # bottone_grafici_corr = tk.Button(finesta_principale,
    #                             text="Grafici Correlazione",
    #                             command=lambda: Grafici_Correlazione(),
    #                             bg="light grey",
    #                             font=("Arial", 12),
    #                             fg="black")
    # bottone_grafici_corr.config(state=tk.DISABLED)
    # bottone_grafici_corr.grid(row=10, column=2)

    # BOTTONE SALVA
    bottone_salva = tk.Button(finesta_principale,
                            text="Excel Salva",
                            command=lambda: Salva(),
                            bg="light grey",
                            font=("Arial", 12),
                            fg="black")
    # bottone_salva.config(state=tk.DISABLED)
    bottone_salva.grid(row=12, column=1)

    try:
            # Load the image file
        img = Image.open(r"C:\Users\galloni\OneDrive - unibs.it\Corsi\Python\Analisi_Dati\Foto\MG.png")

            # Resize the image
        img = img.resize((50, 50), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS

            # Convert the image to a Tkinter-compatible photo image
        tk_img = ImageTk.PhotoImage(img)

            # Create a label and add the image to it
        logo_label = tk.Label(finesta_principale, image=tk_img)
        logo_label.image = tk_img  # keep a reference to the image to prevent it from being garbage collected
        logo_label.grid(row=12, column=3)
    except Exception as e:
        print("Errore nel caricamento del logo: ", e)

def Caricamento(label_file_in, bottone_carica_file, bottone_filtro, bottone_statistiche,bottone_correlazione, bottone_salva):
    # Riferimento alle variabili globali
    path, df_mTp = CaricaFile().file_input_sfoglia()
    label_file_in.config(text=path)
    if df_mTp is not None:
        df_DaUnire.append(df_mTp)
        print("Caricamento completato mTp")
        # bottone_filtro.config(bg="light blue")
        # bottone_filtro.config(state=tk.NORMAL)
        bottone_carica_file.config(bg="light blue")
        # bottone_statistiche.config(bg="light blue")
        # bottone_statistiche.config(state=tk.NORMAL)
        # bottone_correlazione.config(bg="light blue")
        # bottone_correlazione.config(state=tk.NORMAL)
        # # bottone_grafici.config(bg="light blue")
        # # bottone_grafici.config(state=tk.NORMAL)
        # # bottone_grafici_stat.config(bg="light blue")
        # # bottone_grafici_stat.config(state=tk.NORMAL)
        # # bottone_grafici_corr.config(bg="light blue")
        # # bottone_grafici_corr.config(state=tk.NORMAL)
        # bottone_salva.config(bg="light blue")
        # bottone_salva.config(state=tk.NORMAL)

def Caricamento2(label_file_in, bottone_carica_file):
    # Utilizza la lista globale dfs_mRu per aggiungere nuovi DataFrame
    path, df= CaricaFile().file_input_sfoglia()  # Carica il file
    
    if df is not None:
        df_DaUnire.append(df)  # Aggiunge la coppia (DataFrame, tempo) alla lista
        
        label_file_in.config(text=path)  # Aggiorna l'etichetta con il percorso del file
        bottone_carica_file.config(bg="light blue")  # Cambia il colore del bottone
        bottone_carica_file.config(state=tk.NORMAL) 
    print(len(df_DaUnire))

def CaricamentoMRU(label_file_in, bottone_carica_file):
    path,df=CaricaFile().file_input_sfoglia()
    # funzione pulisci dataframe MRU
    df=PulisciMRU(df)
    df=VerificaCH4(df)
    df=RiordinaMRU(df)
    if df is not None:
        df_MRU.append(df)
        label_file_in.config(text=path)
        bottone_carica_file.config(bg="light blue")
        bottone_carica_file.config(state=tk.NORMAL)

def VerificaCH4(df):
    # Verifica se la colonna CH4 è presente nel dataframe
    if 'CH4' and not 'CH4PPM' in df.columns:
        #prendi i valori in CH4 e crea una nuova colonna CH4PPM dividendo i valori per 10^5
        df['CH4PPM'] = df['CH4'] * 100000
    elif 'CH4PPM' and not 'CH4' in df.columns:
        df['CH4'] = df['CH4PPM'] / 100000
    return df

def RiordinaMRU(df):
    colonne = ['Data','CO2', 'CH4', 'CH4PPM', 'O2', 'N2', 'H2S']
    colonne_presenti = [col for col in colonne if col in df.columns]
    #ordina le colonne presenti in funzione a colonne
    df = df[colonne_presenti]
    return df

def PulisciMRU(df):
    df.ffill(inplace=True)
    # controlla che ci siano queste colonne, se non ci sono inseriscile con valori = 0
    colonne = ['Data','CO2', 'CH4','CH4PPM', 'O2', 'N2', 'H2S']
    colonne_presenti = [col for col in colonne if col in df.columns]
    colonne_da_inserire = [col for col in colonne if col not in df.columns]
    for col in colonne_da_inserire:
        df[col] = 0

    return df

def UnisciFile():
    global df_Unito
    df_MRU_Unito = UnisciMRU()
    if df_DaUnire:  # Check if df_DaUnire is empty
        df_Unito = df_DaUnire[0].copy()  # Start with a copy of the first DataFrame to avoid modifying the original

        for i in range(1, len(df_DaUnire)):
            # Merge without renaming columns
            df_Unito = pd.merge(df_Unito, df_DaUnire[i], on='Data', how='outer', suffixes=('', f'_DaUnire{i}'))
            
            # No need for manual renaming after using suffixes in merge

        # Merge with df_MRU_Unito if it's not None and contains data
        if df_MRU_Unito is not None and not df_MRU_Unito.empty:
            # Trova le date comuni tra df_Unito e df_MRU_Unito

            # Using a suffix to differentiate columns from df_MRU_Unito
            df_Unito = pd.merge(df_Unito, df_MRU_Unito, on='Data', how='outer', suffixes=('', '_MRU'))

        # Drop rows where all elements are NaN
        df_Unito.dropna(how='all', inplace=True)

        print("Unione completata")
        colonne = list(df_Unito.columns)
        print(colonne)
    else:
        df_Unito = df_MRU_Unito.copy()

def UnisciMRU():
    global df_MRU_Unito
    if not df_MRU:  # Check if df_MRU is empty
        return pd.DataFrame()  # Return an empty DataFrame if there are no DataFrames to merge
    df_MRU[0] = df_MRU[0].dropna(axis=1, how='all')
    # Initialize df_MRU_Unito with the first DataFrame in the list to ensure it has a structure
    df_MRU_Unito = df_MRU[0].copy()
    # Modify column names except for the first one
    df_MRU_Unito.columns = [col if i == 0 else str(col) + '_MRU1' for i, col in enumerate(df_MRU_Unito.columns)]

    
    # Start the loop from the second DataFrame (if exists)
    for i in range(1, len(df_MRU)):
        # Merge without renaming columns

    # Adjust column names without overwriting the first column
        # df_MRU[i].columns = [col if idx == 0 elif f'{col}' =='' else f'{col}_MRU{i+1}' for idx, col in enumerate(df_MRU[i].columns)]
        # df_MRU_Unito = pd.merge(df_MRU_Unito, df_MRU[i], on='Data', how='outer')
        #rimuovi le colonne con soli valori NaN
        df_MRU[i] = df_MRU[i].dropna(axis=1, how='all')
        df_MRU[i].columns = [col if idx == 0 else (f'{col}_MRU{i+1}' if col != '' else '') for idx, col in enumerate(df_MRU[i].columns)]
        print("DF_MRU"+str(i+1)+":")
        print(df_MRU[i].iloc[:, 0:10])
        df_MRU_Unito = pd.merge(df_MRU_Unito, df_MRU[i], on='Data', how='outer')
    
    # Filter the DataFrame to remove rows where all values are NaN
    # df_MRU_Unito = df_MRU_Unito.dropna(how='all')
    # Seleziona tutte le colonne tranne 'Data'
    # Assicurati che 'Data' sia una colonna e non l'indice del DataFrame, se non lo è già
    # Calcola una maschera booleana per le righe con tutti valori NaN nelle colonne esclusa 'Data'
    mask = df_MRU_Unito.drop(columns=['Data']).isna().all(axis=1)

    # Usa la maschera per mantenere solo le righe dove almeno una colonna (esclusa 'Data') ha un valore non-NaN
    df_MRU_Unito = df_MRU_Unito[~mask]
    # rimuovi tutte le colonne named Data tranne la prima
    # Rimuovi i duplicati basandoti solo sulla colonna 'Data', mantenendo la prima occorrenza
    df_MRU_Unito = df_MRU_Unito.drop_duplicates(subset=['Data'], keep='first')
    print(list(df_MRU_Unito.columns))
    print(df_MRU_Unito.iloc[:, 0:10])
    return df_MRU_Unito

def Filtraggio(finestra_principale, bottone_filtro):
    global df_filtrato, df_Unito  # Aggiungi df_Unito alla dichiarazione globale
    if df_Unito.columns.empty:
        df_Unito = df_DaUnire[0] # Questa linea ora funzionerà come previsto
        print("Filtro su un solo Dataframe")
    try:
        #estrapola una lista dal dalla colonna del dataframe Data che parta dalla prima riga in cui almeno uno dei valori con pedice _MRU non è NaN
        colonne=df_MRU_Unito.columns
        if not colonne.empty:
            date_comuni = set(df_Unito['Data']).intersection(set(df_MRU_Unito['Data']))
        # Crea una lista tempo che contiene solo le date presenti in entrambi i dataframe
            tempo = list(df_Unito.loc[df_Unito['Data'].isin(date_comuni), 'Data'])
        else:
            if isinstance(df_Unito, pd.DataFrame):
                tempo = list(df_Unito['Data'])
            else:
                print("df_Unito is not a DataFrame")
            # tempo = list(df_Unito['Data'])
        filtro = Filtro(finestra_principale, tempo, df_Unito)
        filtro.FinestraFiltro()
        finestra_principale.wait_window(filtro.finestra_filtro)
        df_filtrato = filtro.DataFrame_filtrato()
        if not df_filtrato.empty:
            bottone_filtro.config(bg="light green")
            
        else:
            df_filtrato = None
    except Exception as e:
        messagebox.showerror("Errore", "Nessun filtro applicato")
        print("Errore: ", e)

def Statistiche(finestra_principale,df_Unito,df_filtrato,bottone_statistiche):
    global df_statistiche
    stat= FinestraStatistiche(root, df_Unito, df_filtrato)
    stat.Finestra()
    finestra_principale.wait_window(stat.finestra_stat)
    df_statistiche = stat.get_Stat()
    stat_grezze=df_statistiche[0]
    stat_filtrate=df_statistiche[1]
    if df_statistiche[0] is not None or df_statistiche[1] is not None:
        bottone_statistiche.config(bg="light green")
    if df_statistiche[0] is not None:
        df_stati_grezzi=pd.DataFrame(stat_grezze)
    else:
        df_stati_grezzi=None
    if df_statistiche[1] is not None:
        df_stati_filtrati=pd.DataFrame(stat_filtrate)
    else: 
        df_stati_filtrati=None
    df_statistiche=[df_stati_grezzi,df_stati_filtrati]
        
def Correlzioniamo(finestra_principale, df_unione, df_filtrato, bottone_correlazione):
    global df_correlazione, preferenze_corr
    correlazione = FinestraCorrelazioni(root, df_Unito, df_filtrato)
    correlazione.Finestra()
    finestra_principale.wait_window(correlazione.finestra_corr)
    corr_grezze,corr_filtrate,preferenze_corr = correlazione.get_correlzioni()
    if corr_grezze is not None or corr_filtrate is not None:
        bottone_correlazione.config(bg="light green")
    if corr_grezze is not None:
        df_corr_grezze=[]
        for i in range(len(corr_grezze)):
            df_corr_grezze.append(pd.DataFrame(corr_grezze[i]))
    else:
        df_corr_grezze = None
    if corr_filtrate is not None:
        df_corr_filtrate=[]
        for i in range(len(corr_filtrate)):
            df_corr_filtrate.append(pd.DataFrame(corr_filtrate[i]))
        print("Correlazioni filtrate")
        print(df_corr_filtrate)
    else:
        df_corr_filtrate = ""

    df_correlazione = [df_corr_grezze, df_corr_filtrate]

    if df_correlazione[0] is not None or df_correlazione[1] is not None:
        bottone_correlazione.config(bg="light green")
    # if corr_grezze is not None:
    #     df_corr_grezze=pd.DataFrame(corr_grezze)
    # else:
    #     df_corr_grezze=None
    # if corr_filtrate is not None:
    #     df_corr_filtrate=pd.DataFrame(corr_filtrate)
    # else:
    #     df_corr_filtrate=None
    # df_correlazione=[df_corr_grezze,df_corr_filtrate]
    # if df_correlazione[0] or df_correlazione[1] or df_correlazione[2]:
    #     bottone_correlazione.config(bg="light green")

def Salva():
    fines_salva=FinestraSalvataggio(root, df_Unito, df_filtrato, df_statistiche, df_correlazione, preferenze_corr)
    fines_salva.Finestra()

def Grafici_Variabili():
    FinestraGraficiBase(root, df, df_filtrato).Finestra()

def Grafici_Probabilità():
    FinestraGraficiProbabilita(root, df, df_filtrato).Finestra()

def Grafici_Correlazione():
    FinestraGraficiCorrelazioni(root, df, df_filtrato, df_correlazione, preferenze_corr).Finestra()

def CalcoloCOP(bottone_cop):
    global df_Unito, df_MRU_Unito
    if df_MRU_Unito is None:
        messagebox.showerror("Errore", "Nessun file MRU caricato")
        return
    if df_Unito is None:
        messagebox.showerror("Errore", "Nessun file CSV caricato")
        return 
    if df_MRU_Unito.empty:
        messagebox.showerror("Errore", "File MRU vuoto")
        return
    if df_Unito.empty:
        messagebox.showerror("Errore", "File CSV vuoto")
        return
    if len(df_MRU_Unito.columns) < 31:
        messagebox.showerror("Attnezione", "Non hai inserito tutti gli MRU, questo causa un errore nel calcolo del COP")
    # if len(df_MRU_Unito.columns) > 26:
    #     messagebox.showerror("Attenzione", "A qunto pare alcuni MRU hanno misurato N2")
        
    print(len(df_MRU_Unito.columns))
    # Calcola il COP
    df_Unito=ScambioTermico(df_Unito).Calcolo()


#MAIN RUN
try:
    df = None
    tempo = None
    df_filtrato = None
    df_statistiche = None
    df_correlazione = None
    preferenze_corr = None
    root = tk.Tk()
    app=App(root)
    root.mainloop()
except Exception as e:
    print("Errore generico")

