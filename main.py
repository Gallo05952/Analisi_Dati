import tkinter as tk
from Funzioni import *
import numpy as np
import pandas as pd

def App(finesta_principale):
    finesta_principale.title("Analisi Dati")
    finesta_principale.geometry("1000x500")
    finesta_principale.configure(bg="white")
    finesta_principale.resizable(False,False)

    # Imposta il weight della colonna a 0 per evitare che si espanda -> NON FUNZIONA
    #finesta_principale.grid_columnconfigure(1, weight=0)
    
    # LABEL
    label= tk.Label(finesta_principale,
                    text="Analisi Dati",
                    font=("Arial", 20), 
                    fg="red",
                    bg="white")
    label.grid(row=0, column=0, columnspan=2)

    #EMPTY ROW
    empty_row = tk.Label(finesta_principale, 
                        text="")
    empty_row.grid(row=1, column=0)

    # LABEL FILE IN
    label_file_in = tk.Label(finesta_principale,
                            text="File in: ",
                            font=("Arial", 12),
                            bg="white")
    label_file_in.grid(row=2, column=1)
    
    # BOTTONE CARICA FILE
    bottone_carica_file = tk.Button(finesta_principale,
                            text="Carica File", 
                            command=lambda: Caricamento(label_file_in,
                                                    bottone_carica_file,bottone_filtro, bottone_statistiche,
                                                    bottone_correlazione),
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
    bottone_filtro.grid(row=4, column=0)

    #€ EMPTY ROW
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
    bottone_grafici.grid(row=4, column=2)

    # BOTTONE GRAFICI STATISTICA
    bottone_grafici_stat = tk.Button(finesta_principale,
                                text="Grafici Statistica",
                                command=lambda: Grafici_Statistica(),
                                bg="light grey",
                                font=("Arial", 12),
                                fg="black")
    bottone_grafici_stat.grid(row=6, column=2)

    # BOTTONE GRAFICI CORRELAZIONE
    bottone_grafici_corr = tk.Button(finesta_principale,
                                text="Grafici Correlazione",
                                command=lambda: Grafici_Correlazione(),
                                bg="light grey",
                                font=("Arial", 12),
                                fg="black")
    bottone_grafici_corr.grid(row=8, column=2)

    # BOTTONE SALVA
    bottone_salva = tk.Button(finesta_principale,
                            text="Excel Salva",
                            command=lambda: Salva(),
                            bg="light grey",
                            font=("Arial", 12),
                            fg="black")
    bottone_salva.grid(row=10, column=1)


def Caricamento(label_file_in, bottone_carica_file, bottone_filtro, bottone_statistiche,bottone_correlazione):
    global df, tempo  # Riferimento alle variabili globali
    path, df, tempo = CaricaFile().file_input_sfoglia()
    label_file_in.config(text=path)
    if df is not None:
        bottone_filtro.config(bg="light blue")
        bottone_statistiche.config(bg="light blue")
        bottone_correlazione.config(bg="light blue")

def Filtraggio(finestra_principale, tempo, bottone_filtro):
    global df_filtrato
    filtro = Filtro(finestra_principale, tempo, df)
    filtro.FinestraFiltro()
    finestra_principale.wait_window(filtro.finestra_filtro)
    df_filtrato = filtro.DataFrame_filtrato()
    if not df_filtrato.empty:
        bottone_filtro.config(bg="light green")

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
        print(type(df_corr_grezze))
        print(df_corr_grezze)
    else:
        df_corr_grezze = None
    if corr_filtrate is not None:
        df_corr_filtrate=[]
        for i in range(len(corr_filtrate)):
            df_corr_filtrate.append(pd.DataFrame(corr_filtrate[i]))
        print(type(df_corr_filtrate[0]))
        print(df_corr_filtrate)
    else:
        df_corr_filtrate = None

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

def Grafici_Statistica():
    pass

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


# ## FUNZIONI STATISTICHE
# statistiche_dafare=[app.MediaS,
#                     app.MedianaS,
#                     app.ModaS,
#                     app.DeviazioneS,
#                     app.VarianzaS,
#                     app.minimoS,
#                     app.massimoS]
# if (app.Dati_grezziS == True and
#     app.Dati_filtratiS == False):
#     statistiche_calcolate = Statistica(app.df,
#                                     statistiche_dafare).DatiStatistici()
# elif (app.Dati_grezziS == False and
#     app.Dati_filtratiS == True): 
#     if (app.FiltroIntervallo==True or
#         app.Filtro2==True):
#         statistiche_calcolate = Statistica(Df_filtrato,
#                                         statistiche_dafare).DatiStatistici()
#     else: print("Devi selezionare il filtro da applicare")
# elif (app.Dati_grezziS == True and
#     app.Dati_filtratiS == True):
#     if (app.FiltroIntervallo==True or
#         app.Filtro2==True):
#         calcola_statistiche_grezze = Statistica(app.df,
#                                         statistiche_dafare).DatiStatistici()
#         calcola_statistiche = Statistica(Df_filtrato,
#                                         statistiche_dafare).DatiStatistici()
#         statistiche_calcolate = [calcola_statistiche_grezze,
#                                 calcola_statistiche]
#     print("Statistiche sui dati grezzi e filtrati")
# else: print("Nessuna statistica selezionata")


# ## FUNZIONI CORRELAZIONE
# correlazione=[]
# if (app.Dati_grezziCorrS == True and
#     app.Dati_filtratiCorrS == False):
#     print("Correlazione sui dati grezzi")
#     if app.PearsonS == True:
#         print("Pearson")
#         corr = Correlazione(app.df).Pearson()
#         if app.correlazione_graficabiliS == "Pearson":
#             Correlazione(app.df).GraficoPearson(corr,app.file_name)
#         correlazione.append(corr)
#     if app.SpearmanS == True:
#         correlazione.append(Correlazione(app.df).Spearman())
#         print("Spearman")
#     if app.KendallS == True:
#         print("Kendall")
#         correlazione.append(Correlazione(app.df).Kendall())
# elif (app.Dati_grezziCorrS == False and app.Dati_filtratiCorrS == True):
#     if app.PearsonS == True:
#         print("Pearson")
#         corr=Correlazione(Df_filtrato).Pearson()
#         if app.correlazione_graficabiliS == "Pearson":
#             Correlazione(Df_filtrato).GraficoPearson(corr,app.file_name)
#         correlazione.append(corr)
#     if app.SpearmanS == True:
#         print("Spearman")
#         correlazione.append(Correlazione(Df_filtrato).Spearman())
#     if app.KendallS == True:
#         print("Kendall")
#         correlazione.append(Correlazione(Df_filtrato).Kendall())
# elif (app.Dati_grezziCorrS == True and app.Dati_filtratiCorrS == True):
#     print("Correlazione sui dati grezzi e filtrati")
#     if app.PearsonS == True:
#         print("Pearson")
#         correlazione_grezzi = Correlazione(app.df).Pearson()
#         correlazione_filtrati = Correlazione(Df_filtrato).Pearson()
#         if app.correlazione_graficabiliS == "Pearson":
#             file_name_grezzi = app.file_name + "_Grezzi"
#             Correlazione(app.df).GraficoPearson(correlazione_grezzi,file_name_grezzi)
#             file_name_filtrati = app.file_name + "_Filtrati"
#             Correlazione(Df_filtrato).GraficoPearson(correlazione_filtrati,file_name_filtrati)
#         correlazione.append([correlazione_grezzi,correlazione_filtrati])
#     if app.SpearmanS == True:
#         print("Spearman")
#         correlazione_grezzi = Correlazione(app.df).Spearman()
#         correlazione_filtrati = Correlazione(Df_filtrato).Spearman()
#         correlazione.append([correlazione_grezzi,correlazione_filtrati])
#     if app.KendallS == True:
#         print("Kendall")
#         correlazione_grezzi = Correlazione(app.df).Kendall()
#         correlazione_filtrati = Correlazione(Df_filtrato).Kendall()
#         correlazione.append([correlazione_grezzi,correlazione_filtrati])
# else: print("Nessuna correlazione selezionata")


# # SCRITTURA DEI DATI SU FILE EXCEL
# correlazioni_da_fare=[app.PearsonS,app.SpearmanS,app.KendallS]
# if (app.OpzSalvaS == True):
#     ScritturaExcel(app.savename).Scrittura(app.df,
#                                         Df_filtrato,statistiche_calcolate,
#                                         statistiche_dafare,
#                                         correlazione,
#                                         correlazioni_da_fare)
# # if app.Filtro2 == True or app.FiltroIntervallo == True: Filtro = True
# # Preferenze = [Filtro, app.Dati_grezziS, app.Dati_filtratiS]
