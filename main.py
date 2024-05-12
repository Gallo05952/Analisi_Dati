import tkinter as tk
from Funzioni import *
import numpy as np


root = tk.Tk()
app = Interfaccia(root)
app.FinestraPrincipale()
root.mainloop()

#data=app.df
#print(data.columns)

## FUNZIONI FILTRO
if app.FiltroIntervallo==True:
    # print("Filtro attivo")
    # print("Tempo iniziale: ",app.TempoIniziale)
    # print("Tempo finale: ",app.TempoFinale)
    # print(len(app.df))
    Df_filtrato=FiltroTempo(app.df).FiltraPerTempo(app.TempoIniziale,
                                            app.TempoFinale)
    #print(len(abba))
elif app.Filtro2==True: 
    # print("Filtro scarto attivo")
    # print(len(app.df))
    # print("Tempo di scarto: ",app.TempoDa)
    Df_filtrato=FiltroTempo(app.df).FineTransitorio(app.TempoDa)
    # print(len(abba))
else:
    print("Nessun filtro attivo")
    Df_filtrato=np.NaN

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
    print("Statistiche sui dati grezzi")
    statistiche_calcolate = Statistica(app.df,
                                    statistiche_dafare).DatiStatistici()
    print(statistiche_calcolate)
elif (app.Dati_grezziS == False and
    app.Dati_filtratiS == True): 
    if (app.FiltroIntervallo==True or
        app.Filtro2==True):
        print("Statistiche sui dati filtrati")
        statistiche_calcolate = Statistica(Df_filtrato,
                                        statistiche_dafare).DatiStatistici()
        print(statistiche_calcolate)
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
else:
    print("Nessuna statistica selezionata")

# SCRITTURA DEI DATI SU FILE EXCEL
print(app.OpzSalvaS)