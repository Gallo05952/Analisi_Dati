import tkinter as tk
from Funzioni import *


root = tk.Tk()
app = Interfaccia(root)
app.FinestraPrincipale()
root.mainloop()

#data=app.df
#print(data.columns)
print(app.FiltroIntervallo)
print(app.Filtro2)
if app.Filtro2 == True:
    print(app.TempoDa)
if app.FiltroIntervallo == True:
    #print(app.TempoInizio)
    print(app.TempoFine)
