import tkinter as tk
from Funzioni import *


root = tk.Tk()
app = Interfaccia(root).FinestraPrincipale()
root.mainloop()

data=app.df
print(data.columns)