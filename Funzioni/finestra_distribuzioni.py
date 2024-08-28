import tkinter as tk

class FinestraDistribuzioni:

    def __init__(self, root, df,df_filtrato):
        self.root = root
        self.df = df
        self.df_filtrato = df_filtrato

    def Finestra(self):
        self.finestra_corr = tk.Toplevel(self.root)
        self.finestra_corr.title("Finestra Distribuzioni")
        self.finestra_corr.geometry("350x200")
