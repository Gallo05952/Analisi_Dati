import pandas as pd
import numpy as np

class Statistica:
    def __init__(self,df,daFare):
        self.df = df.copy()
        self.daFare = daFare        
    
    def Media(self, col):
        try:
            media = self.df[col].mean()
        except:
            media = np.nan
        return media
    
    def Mediana(self, col):
        try:
            mediana = self.df[col].median()
        except:
            mediana = np.nan
        return mediana
    
    def Varianza(self, col):
        try:
            varianza = self.df[col].var()
        except:
            varianza = np.nan
        return varianza
    
    def DeviazioneStandard(self, col):
        try:
            deviazione_standard = self.df[col].std()
        except:
            deviazione_standard = np.nan
        return deviazione_standard

    def Moda(self, col):
        try:
            moda_df = self.df[col].mode(dropna=True)
            if not moda_df.empty:
                moda = moda_df.iloc[0]
            else:
                moda = np.nan
        except:
            moda = np.nan
        return moda

    def Minimo(self, col):
        try:
            minimo = self.df[col].min()
        except:
            minimo = np.nan
        return minimo

    def Massimo(self, col):
        try:
            massimo = self.df[col].max()
        except:
            massimo = np.nan
        return massimo
    
    def DatiStatistici(self):
        statistiche = {}
        for col in self.df.columns:
            statistiche[col] = self.calcola_statistiche(col)
        return statistiche
    
    def calcola_statistiche(self, col):
        stat=[]
        if self.daFare[0]==True:
            stat.append(self.Media(col))
        if self.daFare[1]==True:
            stat.append(self.Mediana(col))
        if self.daFare[2]==True:
            stat.append(self.Moda(col))
        if self.daFare[3]==True:
            stat.append(self.DeviazioneStandard(col))
        if self.daFare[4]==True:
            stat.append(self.Varianza(col))
        if self.daFare[5]==True:
            stat.append(self.Minimo(col))
        if self.daFare[6]==True:
            stat.append(self.Massimo(col))
        return stat