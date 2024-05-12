import tkinter as tk
from Funzioni import *


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


if (app.Dati_grezziS == True and
    app.Dati_filtratiS == False):
    print("Statistiche sui dati grezzi")
elif (app.Dati_grezziS == False and
    app.Dati_filtratiS == True):
    print("Statistiche sui dati filtrati")
elif (app.Dati_grezziS == True and
    app.Dati_filtratiS == True):
    print("Statistiche sui dati grezzi e filtrati")
else:
    print("Nessuna statistica selezionata")

# QUESTE SONO LE VARIABILI PER CHIAMARE LE STATISTICHE
print(app.MediaS)
print(app.MedianaS)
print(app.ModaS)
print(app.DeviazioneS)
print(app.VarianzaS)
print(app.Dati_grezziS)
print(app.Dati_filtratiS)
