import pandas as pd
import numpy as np
import datetime
import plotly.express as px
import os


class Correlazione:

    def __init__(self, df):
        self.df = df.applymap(self.check_numeric)

    def check_numeric(self, x):
        if isinstance(x, datetime.time):
            return np.nan
        try:
            float(x)
            return x
        except ValueError:
            return np.nan

    def Pearson(self):
        return self.df.corr(method='pearson')
    
    def Spearman(self):
        return self.df.corr(method='spearman')
    
    def Kendall(self):
        return self.df.corr(method='kendall')
    

    def GraficoPearson(self, correlazioni, savename):
        # Trasformazione del DataFrame di correlazione in un formato lungo per il plotting
        corr_long = correlazioni.unstack().reset_index()
        corr_long.columns = ['Variable 1', 'Variable 2', 'Correlation']

        # Creazione del barplot con Plotly
        fig = px.bar(corr_long, x='Variable 1', y='Correlation', color='Variable 2', barmode='group')
        # Salva il grafico come file HTML
        # fig.write_html(f"{savename}_GraficoPearson.html")
        fig.write_html(fr"C:\Users\galloni\OneDrive - unibs.it\Corsi\Python\Analisi_Dati\Grafici\{savename}_GraficoPearson.html")
