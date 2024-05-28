import tkinter as tk
from Funzioni import *
import numpy as np




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
                            command=lambda: Caricamento(label_file_in),
                            bg="light grey",
                            fg="bLACK")
    bottone_carica_file.grid(row=2, column=0)

    # EMPRY ROW
    empty_row = tk.Label(finesta_principale,
                        text="")
    empty_row.grid(row=3, column=0)

    bottone_filtro = tk.Button(finesta_principale,
                            text="Filtro",
                            command=Filtro(finesta_principale).FinestraFiltro,
                            bg="light grey",
                            fg="black")
    bottone_filtro.grid(row=4, column=0)


def Caricamento(label_file_in):
    global df, tempo  # Riferimento alle variabili globali
    path, df, tempo = CaricaFile().file_input_sfoglia()
    label_file_in.config(text=path)


df = None
tempo = None
root = tk.Tk()
app=App(root)
root.mainloop()



    # # BOTTONE CARICA FILE
    # bottone_carica_file = tk.Button(finesta_principale, text="Carica File", command=CaricaFile, bg="blue", fg="white")
    # bottone_carica_file.pack()

    # # BOTTONE FILTRO
    # bottone_filtro = tk.Button(finesta_principale, text="Filtro", command=Filtro, bg="blue", fg="white")
    # bottone_filtro.pack()

    # # BOTTONE STATISTICHE
    # bottone_statistiche = tk.Button(finesta_principale, text="Statistiche", command=Statistiche, bg="blue", fg="white")
    # bottone_statistiche.pack()

    # # BOTTONE CORRELAZIONE
    # bottone_correlazione = tk.Button(finesta_principale, text="Correlazione", command=Correlazione, bg="blue", fg="white")
    # bottone_correlazione.pack()

    # # BOTTONE SALVA
    # bottone_salva = tk.Button(finesta_principale, text="Salva", command=Salva, bg="blue", fg="white")
    # bottone_salva.pack()

    # # BOTTONE ESCI
    # bottone_esci = tk.Button(finesta_principale, text="Esci", command=finesta_principale.quit, bg="red", fg="white")
    # bottone_esci.pack()

    # finesta_principale.mainloop()







# statistiche_calcolate=[]
# statistiche_dafare=[]

# ## FUNZIONI FILTRO
# if app.FiltroIntervallo==True:
#     Df_filtrato=FiltroTempo(app.df).FiltraPerTempo(app.TempoIniziale,
#                                             app.TempoFinale)
# elif app.Filtro2==True: 
#     Df_filtrato=FiltroTempo(app.df).FineTransitorio(app.TempoDa)
# else:
#     print("Nessun filtro attivo")
#     Df_filtrato=[]

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
