import tkinter as tk
from Funzioni import *


root = tk.Tk()
app = Interfaccia(root)
app.FinestraPrincipale()
root.mainloop()

#data=app.df
#print(data.columns)

if app.FiltroIntervallo==True:
    print("Filtro attivo")
    print("Tempo iniziale: ",app.TempoIniziale)
    print("Tempo finale: ",app.TempoFinale)
    print(len(app.df))
    abba=FiltroTempo(app.df).FiltraPerTempo(app.TempoIniziale,app.TempoFinale)
    print(len(abba))
elif app.Filtro2==True: 
    print("Filtro scarto attivo")
    print(len(app.df))
    print("Tempo di scarto: ",app.TempoDa)
    abba=FiltroTempo(app.df).FineTransitorio(app.TempoDa)
    print(len(abba))
else:
    print("Nessun filtro attivo")

# QUESTE SONO LE VARIABILI PER CHIAMARE LE STATISTICHE
print(app.MediaS)
print(app.MedianaS)
print(app.ModaS)
print(app.DeviazioneS)
print(app.VarianzaS)
