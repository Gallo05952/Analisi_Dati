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
elif app.Filtro2==True:
    print("Filtro scarto attivo")
    print("Tempo di scarto: ",app.TempoDa)
else:
    print("Nessun filtro attivo")