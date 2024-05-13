
import pandas as pd
import numpy as np

class ScritturaExcel:

    def __init__(self,filepath):
        self.filepath = filepath


    def Scrittura(self,df,
                Df_filtrato,
                statistiche_calcolate,
                statistiche_dafare):
            self.writer = pd.ExcelWriter(self.filepath, engine='xlsxwriter')
            self.ScritturaOriginali(df)
            if not Df_filtrato.empty:  
                self.ScritturaFiltrati(Df_filtrato)
            if statistiche_dafare:
                self.ScritturaStatistiche(statistiche_calcolate,
                                        statistiche_dafare)

            # Close the Pandas Excel writer and output the Excel file.
            self.writer.close()
        
    def ScritturaOriginali(self,df):
        df.to_excel(self.writer, sheet_name='Originali')

    def ScritturaFiltrati(self,Df_filtrato):
        Df_filtrato.to_excel(self.writer, sheet_name='Filtrati')

    def ScritturaStatistiche(self,
                            statistiche_calcolate,
                            statistiche_dafare):
        NomiStat_gen=['Media','Mediana','Moda','Deviazione','Varianza','Minimo','Massimo']
        NomiStat=[NomiStat_gen[i] 
                for i in range(len(statistiche_dafare))
                if statistiche_dafare[i]]
        if len(statistiche_calcolate)==1:
            df_stat = pd.DataFrame(statistiche_calcolate).T
            df_stat.columns = NomiStat
            df_stat.to_excel(self.writer, sheet_name='Statistiche')
        else:
            NomiFogli=['Statistiche dei grezzi',
                    'Statistiche dei filtrati']
            for i in range(len(statistiche_calcolate)):
                df_stat = pd.DataFrame(statistiche_calcolate[i]).T
                df_stat.columns = NomiStat
                df_stat.to_excel(self.writer, sheet_name=NomiFogli[i])
