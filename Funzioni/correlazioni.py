# Fix for the FutureWarning regarding DataFrame.applymap
# Replace df.applymap(self.check_numeric) with a proper alternative since applymap is deprecated.
# The alternative approach involves using DataFrame.apply with a lambda function that applies check_numeric to each element.

# Fix for the TypeError in check_numeric
# The issue is with the isinstance check for datetime. It should be datetime.datetime instead of just datetime.

import pandas as pd
import numpy as np
import datetime
import plotly.express as px
import os

class Correlazione:

    def __init__(self, df):
        # Updated line to use DataFrame.apply with a lambda function for element-wise operation
        self.df = df.apply(lambda x: x.apply(self.check_numeric))

    def check_numeric(self, x):
        # Fixed the isinstance check to use datetime.datetime
        if isinstance(x, datetime.datetime):
            return np.nan
        if x is None:
            return np.nan
        if isinstance(x, str) and x.strip() == "":
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
        corr_long = correlazioni.unstack().reset_index()
        corr_long.columns = ['Variable 1', 'Variable 2', 'Correlation']
        
        fig = px.bar(corr_long, x='Variable 1', y='Correlation', color='Variable 2', barmode='group')
        fig.write_html(fr"C:\Users\galloni\OneDrive - unibs.it\Corsi\Python\Analisi_Dati\Grafici\{savename}_GraficoPearson.html")

# import pandas as pd
# import numpy as np
# import datetime
# import plotly.express as px
# import os


# class Correlazione:

#     def __init__(self, df):
#         self.df = df.applymap(self.check_numeric)
# # #.time
# #     def check_numeric(self, x):
# #         if isinstance(x, datetime):
# #             return np.nan
# #         try:
# #             float(x)
# #             return x
# #         except ValueError:
# #             return np.nan
#     def check_numeric(self, x):
#         # Condizione per datetime già presente
#         if isinstance(x, datetime):
#             return np.nan
#         # Aggiunta condizione per None
#         if x is None:
#             return np.nan
#         # Aggiunta condizione per stringa vuota
#         if isinstance(x, str) and x.strip() == "":
#             return np.nan
#         # Qui puoi aggiungere altre condizioni specifiche se necessario
        
#         try:
#             float(x)
#             return x
#         except ValueError:
#             return np.nan

#     def Pearson(self):
#         return self.df.corr(method='pearson')
    
#     def Spearman(self):
#         return self.df.corr(method='spearman')
    
#     def Kendall(self):
#         return self.df.corr(method='kendall')
    

#     def GraficoPearson(self, correlazioni, savename):
#         # Trasformazione del DataFrame di correlazione in un formato lungo per il plotting
#         corr_long = correlazioni.unstack().reset_index()
#         corr_long.columns = ['Variable 1', 'Variable 2', 'Correlation']
        
#         # Creazione del barplot con Plotly
#         fig = px.bar(corr_long, x='Variable 1', y='Correlation', color='Variable 2', barmode='group')
#         # Salva il grafico come file HTML
#         # fig.write_html(f"{savename}_GraficoPearson.html")
#         fig.write_html(fr"C:\Users\galloni\OneDrive - unibs.it\Corsi\Python\Analisi_Dati\Grafici\{savename}_GraficoPearson.html")
