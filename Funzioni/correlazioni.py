import pandas as pd
import numpy as np

class Correlazione:

    def __init__(self, df):
        self.df = df.applymap(self.check_numeric)

    def check_numeric(self, x):
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