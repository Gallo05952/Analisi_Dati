import tkinter as tk
from Funzioni import *
import numpy as np


root = tk.Tk()
app = Interfaccia(root)
app.FinestraPrincipale()
root.mainloop()
statistiche_calcolate=[]
statistiche_dafare=[]

## FUNZIONI FILTRO
if app.FiltroIntervallo==True:
    Df_filtrato=FiltroTempo(app.df).FiltraPerTempo(app.TempoIniziale,
                                            app.TempoFinale)
elif app.Filtro2==True: 
    Df_filtrato=FiltroTempo(app.df).FineTransitorio(app.TempoDa)
else:
    print("Nessun filtro attivo")
    Df_filtrato=[]

## FUNZIONI STATISTICHE
statistiche_dafare=[app.MediaS,
                    app.MedianaS,
                    app.ModaS,
                    app.DeviazioneS,
                    app.VarianzaS,
                    app.minimoS,
                    app.massimoS]
if (app.Dati_grezziS == True and
    app.Dati_filtratiS == False):
    statistiche_calcolate = Statistica(app.df,
                                    statistiche_dafare).DatiStatistici()
elif (app.Dati_grezziS == False and
    app.Dati_filtratiS == True): 
    if (app.FiltroIntervallo==True or
        app.Filtro2==True):
        statistiche_calcolate = Statistica(Df_filtrato,
                                        statistiche_dafare).DatiStatistici()
    else: print("Devi selezionare il filtro da applicare")
elif (app.Dati_grezziS == True and
    app.Dati_filtratiS == True):
    if (app.FiltroIntervallo==True or
        app.Filtro2==True):
        calcola_statistiche_grezze = Statistica(app.df,
                                        statistiche_dafare).DatiStatistici()
        calcola_statistiche = Statistica(Df_filtrato,
                                        statistiche_dafare).DatiStatistici()
        statistiche_calcolate = [calcola_statistiche_grezze,
                                calcola_statistiche]
    print("Statistiche sui dati grezzi e filtrati")
else: print("Nessuna statistica selezionata")


## FUNZIONI CORRELAZIONE
correlazione=[]
if (app.Dati_grezziCorrS == True and
    app.Dati_filtratiCorrS == False):
    print("Correlazione sui dati grezzi")
    if app.PearsonS == True:
        print("Pearson")
        corr = Correlazione(app.df).Pearson()
        if app.correlazione_graficabiliS == "Pearson":
            Correlazione(app.df).GraficoPearson(corr,app.file_name)
        correlazione.append(corr)
    if app.SpearmanS == True:
        correlazione.append(Correlazione(app.df).Spearman())
        print("Spearman")
    if app.KendallS == True:
        print("Kendall")
        correlazione.append(Correlazione(app.df).Kendall())
elif (app.Dati_grezziCorrS == False and app.Dati_filtratiCorrS == True):
    if app.PearsonS == True:
        print("Pearson")
        correlazione.append(Correlazione(Df_filtrato).Pearson())
    if app.SpearmanS == True:
        print("Spearman")
        correlazione.append(Correlazione(Df_filtrato).Spearman())
    if app.KendallS == True:
        print("Kendall")
        correlazione.append(Correlazione(Df_filtrato).Kendall())
elif (app.Dati_grezziCorrS == True and app.Dati_filtratiCorrS == True):
    print("Correlazione sui dati grezzi e filtrati")
    if app.PearsonS == True:
        print("Pearson")
        correlazione_grezzi = Correlazione(app.df).Pearson()
        correlazione_filtrati = Correlazione(Df_filtrato).Pearson()
        correlazione.append([correlazione_grezzi,correlazione_filtrati])
    if app.SpearmanS == True:
        print("Spearman")
        correlazione_grezzi = Correlazione(app.df).Spearman()
        correlazione_filtrati = Correlazione(Df_filtrato).Spearman()
        correlazione.append([correlazione_grezzi,correlazione_filtrati])
    if app.KendallS == True:
        print("Kendall")
        correlazione_grezzi = Correlazione(app.df).Kendall()
        correlazione_filtrati = Correlazione(Df_filtrato).Kendall()
        correlazione.append([correlazione_grezzi,correlazione_filtrati])
else: print("Nessuna correlazione selezionata")


# SCRITTURA DEI DATI SU FILE EXCEL
correlazioni_da_fare=[app.PearsonS,app.SpearmanS,app.KendallS]
if (app.OpzSalvaS == True):
    ScritturaExcel(app.savename).Scrittura(app.df,
                                        Df_filtrato,statistiche_calcolate,
                                        statistiche_dafare,
                                        correlazione,
                                        correlazioni_da_fare)
# if app.Filtro2 == True or app.FiltroIntervallo == True: Filtro = True
# Preferenze = [Filtro, app.Dati_grezziS, app.Dati_filtratiS]
