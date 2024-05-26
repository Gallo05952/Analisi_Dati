import pandas as pd
import numpy as np
import datetime

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
    
    def GraficoPearson(self, correlazioni):
        # grafica creando un grafico html
        # con plotly

        import plotly.graph_objects as go
        import plotly.tools as tls
    # Crea un grafico a barre con pandas
        fig = go.Figure(data=[go.Bar(
                    x=correlazioni.columns,
                    y=correlazioni.values[0]
                )])

                # Salva il grafico come file HTML
        fig.write_html('GraficoPearson.html')