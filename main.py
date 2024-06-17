import tkinter as tk
from Funzioni import *
import numpy as np
import pandas as pd
from tkinter import messagebox
from PIL import Image, ImageTk

def App(finesta_principale):
    finesta_principale.title("Analisi Dati")
    finesta_principale.geometry("400x350")
    
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
    label_file_in.grid(row=2, column=1)
    
    # BOTTONE CARICA FILE
    bottone_carica_file = tk.Button(finesta_principale,
                            text="Carica File", 
                            command=lambda: Caricamento(label_file_in,
                                        bottone_carica_file,bottone_filtro, bottone_statistiche,
                                        bottone_correlazione, bottone_grafici, bottone_grafici_stat, bottone_grafici_corr, bottone_salva),
                            bg="light grey",
                            font=("Arial", 12),
                            fg="bLACK")
    bottone_carica_file.grid(row=2, column=0)

    # EMPRY ROW
    empty_row = tk.Label(finesta_principale,
                        text="")
    empty_row.grid(row=3, column=0)

    # BOTTONE FILTRO
    bottone_filtro = tk.Button(finesta_principale,
                            text="Filtro",
                            command=lambda: Filtraggio(finesta_principale, tempo,bottone_filtro),
                            bg="light grey",
                            font=("Arial", 12),
                            fg="black")
    bottone_filtro.config(state=tk.DISABLED)
    bottone_filtro.grid(row=4, column=0)

    # EMPTY ROW
    empty_row = tk.Label(finesta_principale,
                        text="")
    empty_row.grid(row=5, column=0)

    # BOTTONE STATISTICHE
    bottone_statistiche = tk.Button(finesta_principale,
                                    text="Statistiche",
                                    command=lambda: Statistiche(finesta_principale,df, df_filtrato,bottone_statistiche),
                                    font=("Arial", 12),
                                    bg="light grey",
                                    fg="black")
    bottone_statistiche.config(state=tk.DISABLED)
    bottone_statistiche.grid(row=6, column=0)

    # EMPTY ROW
    empty_row = tk.Label(finesta_principale,
                        text="")
    empty_row.grid(row=7, column=0)

    # BOTTONE CORRELAZIONE
    bottone_correlazione = tk.Button(finesta_principale,
                                    text="Correlazione",
                                    command=lambda: Correlzioniamo(finesta_principale, df, df_filtrato, bottone_correlazione),
                                    bg="light grey",
                                    font=("Arial", 12),
                                    fg="black")
    bottone_correlazione.config(state=tk.DISABLED)
    bottone_correlazione.grid(row=8, column=0)

    # EMPTY ROW
    empty_row = tk.Label(finesta_principale,
                        text="")
    empty_row.grid(row=9, column=0)

    # BOTTONE GRAFICI VARIABILI
    bottone_grafici = tk.Button(finesta_principale,
                            text="Grafici",
                            command=lambda: Grafici_Variabili(),
                            bg="light grey",
                            font=("Arial", 12),
                            fg="black")
    bottone_grafici.config(state=tk.DISABLED)
    bottone_grafici.grid(row=4, column=2)

    # BOTTONE GRAFICI DENSITà DI PROBABILITà
    bottone_grafici_stat = tk.Button(finesta_principale,
                                text="Grafici Probabilità",
                                command=lambda: Grafici_Probabilità(),
                                bg="light grey",
                                font=("Arial", 12),
                                fg="black")
    bottone_grafici_stat.config(state=tk.DISABLED)
    bottone_grafici_stat.grid(row=6, column=2)

    # BOTTONE GRAFICI CORRELAZIONE
    bottone_grafici_corr = tk.Button(finesta_principale,
                                text="Grafici Correlazione",
                                command=lambda: Grafici_Correlazione(),
                                bg="light grey",
                                font=("Arial", 12),
                                fg="black")
    bottone_grafici_corr.config(state=tk.DISABLED)
    bottone_grafici_corr.grid(row=8, column=2)

    # BOTTONE SALVA
    bottone_salva = tk.Button(finesta_principale,
                            text="Excel Salva",
                            command=lambda: Salva(),
                            bg="light grey",
                            font=("Arial", 12),
                            fg="black")
    bottone_salva.config(state=tk.DISABLED)
    bottone_salva.grid(row=10, column=1)

    try:
            # Load the image file
        img = Image.open(r"C:\Users\galloni\OneDrive - unibs.it\Corsi\Python\Analisi_Dati\MG.png")

            # Resize the image
        img = img.resize((50, 50), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS

            # Convert the image to a Tkinter-compatible photo image
        tk_img = ImageTk.PhotoImage(img)

            # Create a label and add the image to it
        logo_label = tk.Label(finesta_principale, image=tk_img)
        logo_label.image = tk_img  # keep a reference to the image to prevent it from being garbage collected
        logo_label.grid(row=10, column=2)
    except Exception as e:
        print("Errore nel caricamento del logo: ", e)

def Caricamento(label_file_in, bottone_carica_file, bottone_filtro, bottone_statistiche,bottone_correlazione, bottone_grafici, bottone_grafici_stat, bottone_grafici_corr, bottone_salva):
    global df, tempo  # Riferimento alle variabili globali
    path, df, tempo = CaricaFile().file_input_sfoglia()
    label_file_in.config(text=path)
    if df is not None:
        bottone_filtro.config(bg="light blue")
        bottone_filtro.config(state=tk.NORMAL)
        bottone_statistiche.config(bg="light blue")
        bottone_statistiche.config(state=tk.NORMAL)
        bottone_correlazione.config(bg="light blue")
        bottone_correlazione.config(state=tk.NORMAL)
        bottone_grafici.config(bg="light blue")
        bottone_grafici.config(state=tk.NORMAL)
        bottone_grafici_stat.config(bg="light blue")
        bottone_grafici_stat.config(state=tk.NORMAL)
        bottone_grafici_corr.config(bg="light blue")
        bottone_grafici_corr.config(state=tk.NORMAL)
        bottone_salva.config(bg="light blue")
        bottone_salva.config(state=tk.NORMAL)

def Filtraggio(finestra_principale, tempo, bottone_filtro):
    global df_filtrato
    try:
        filtro = Filtro(finestra_principale, tempo, df)
        filtro.FinestraFiltro()
        finestra_principale.wait_window(filtro.finestra_filtro)
        df_filtrato = filtro.DataFrame_filtrato()
        if not df_filtrato.empty:
            bottone_filtro.config(bg="light green")
            
        else:
            df_filtrato = None
    except Exception as e:
        messagebox.showerror("Errore", "Nessun filtro applicato")

def Statistiche(finestra_principale,df,df_filtrato,bottone_statistiche):
    global df_statistiche
    stat= FinestraStatistiche(root, df, df_filtrato)
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
        
def Correlzioniamo(finestra_principale, df, df_filtrato, bottone_correlazione):
    global df_correlazione, preferenze_corr
    correlazione = FinestraCorrelazioni(root, df, df_filtrato)
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
    fines_salva=FinestraSalvataggio(root, df, df_filtrato, df_statistiche, df_correlazione, preferenze_corr)
    fines_salva.Finestra()

def Grafici_Variabili():
    FinestraGraficiBase(root, df, df_filtrato).Finestra()

def Grafici_Probabilità():
    FinestraGraficiProbabilita(root, df, df_filtrato).Finestra()

def Grafici_Correlazione():
    FinestraGraficiCorrelazioni(root, df, df_filtrato, df_correlazione, preferenze_corr).Finestra()

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

