
import pandas as pd
import numpy as np

class ScritturaExcel:

    def __init__(self,filepath):
        self.filepath = filepath


    def Scrittura(self,df,
                Df_filtrato,
                statistiche_calcolate,
                statistiche_dafare,
                correlazioni,
                correlazioni_da_fare):
            self.writer = pd.ExcelWriter(self.filepath, engine='xlsxwriter')
            self.ScritturaOriginali(df)
            if not Df_filtrato.empty:  
                self.ScritturaFiltrati(Df_filtrato)
            if statistiche_dafare:
                self.ScritturaStatistiche(statistiche_calcolate,
                                        statistiche_dafare)
            if correlazioni_da_fare:
                self.ScritturaCorrelazioni(correlazioni,
                                        correlazioni_da_fare)
            

            # Close the Pandas Excel writer and output the Excel file.
            self.writer.close()
        
    def ScritturaOriginali(self,df):
        df.to_excel(self.writer, sheet_name='Originali')

    def ScritturaFiltrati(self,Df_filtrato):
        Df_filtrato.to_excel(self.writer, sheet_name='Filtrati')

    def ScritturaStatistiche(self,
                            statistiche_calcolate,
                            statistiche_dafare
                            ):
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

    def ScritturaCorrelazioni(self,
                            correlazioni,
                            correlazioni_da_fare):
        NomiCorr_gen=['Pearson','Spearman','Kendall']
        NomiCorr=[NomiCorr_gen[i] 
                for i in range(len(correlazioni_da_fare))
                if correlazioni_da_fare[i]]
        if all(isinstance(item, list) for item in correlazioni):
            NomiFogli=['Correlazioni dei grezzi',
                    'Correlazioni dei filtrati']
            for i in range(len(correlazioni)):
                if NomiCorr[i] == "Pearson":
                    correlazioni[i][0].to_excel(self.writer, sheet_name='Pearson_grezzi')
                    correlazioni[i][1].to_excel(self.writer, sheet_name='Pearson_filtrati')
                elif NomiCorr[i] == "Spearman":
                    correlazioni[i][0].to_excel(self.writer, sheet_name='Spearman_grezzi')
                    correlazioni[i][1].to_excel(self.writer, sheet_name='Spearman_filtrati')
                elif NomiCorr[i] == "Kendall":
                    correlazioni[i][0].to_excel(self.writer, sheet_name='Kendall_grezzi')
                    correlazioni[i][1].to_excel(self.writer, sheet_name='Kendall_filtrati')
        else:
            for i in range(len(correlazioni)):
                if NomiCorr[i] == "Pearson":
                    correlazioni[i].to_excel(self.writer, sheet_name='Pearson')
                elif NomiCorr[i] == "Spearman":
                    correlazioni[i].to_excel(self.writer, sheet_name='Spearman')
                elif NomiCorr[i] == "Kendall":
                    correlazioni[i].to_excel(self.writer, sheet_name='Kendall')
        # if len(correlazioni[0])==1:
        #     for i in range(len(correlazioni)):
        #         if NomiCorr[i] == "Pearson":
        #             correlazioni[i].to_excel(self.writer, sheet_name='Pearson')
        #         elif NomiCorr[i] == "Spearman":
        #             correlazioni[i].to_excel(self.writer, sheet_name='Spearman')
        #         elif NomiCorr[i] == "Kendall":
        #             correlazioni[i].to_excel(self.writer, sheet_name='Kendall')
        # else:
        #     NomiFogli=['Correlazioni dei grezzi',
        #             'Correlazioni dei filtrati']
        #     for i in range(len(correlazioni)):
        #         if NomiCorr[i] == "Pearson":
        #             correlazioni[i][0].to_excel(self.writer, sheet_name='Pearson_grezzi')
        #             correlazioni[i][1].to_excel(self.writer, sheet_name='Pearson_filtrati')
        #         elif NomiCorr[i] == "Spearman":
        #             correlazioni[i][0].to_excel(self.writer, sheet_name='Spearman_grezzi')
        #             correlazioni[i][1].to_excel(self.writer, sheet_name='Spearman_filtrati')
        #         elif NomiCorr[i] == "Kendall":
        #             correlazioni[i][0].to_excel(self.writer, sheet_name='Kendall_grezzi')
        #             correlazioni[i][1].to_excel(self.writer, sheet_name='Kendall_filtrati')