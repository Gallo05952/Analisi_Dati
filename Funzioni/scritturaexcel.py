
import pandas as pd

class ScritturaExcel:

    def __init__(self,filepath):
        self.filepath = filepath


    def Scrittura(self,df):
        writer = pd.ExcelWriter(self.filepath, engine='xlsxwriter')

        # Write each dataframe to a different worksheet.
        df.to_excel(writer, sheet_name='Filtrati')

        # Close the Pandas Excel writer and output the Excel file.
        writer.close()
        

    def Scrittura_F_S(self,df,df_filtrato,statistica_F,statistica):# Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(self.filepath, engine='xlsxwriter')

        # Write each dataframe to a different worksheet.
        df.to_excel(writer, sheet_name='Originali')
        df_filtrato.to_excel(writer, sheet_name='Filtrati')
        dascrivere = pd.DataFrame(statistica_F).T
        #dascrivere.to_excel(writer, sheet_name='Statistiche')
        dascrivere.applymap(lambda x: x.values[0] if isinstance(x, pd.Series) else x).to_excel(writer, sheet_name='Statistiche Filtrate')
        dascrivere2 = pd.DataFrame(statistica).T
        #dascrivere.to_excel(writer, sheet_name='Statistiche')
        dascrivere2.applymap(lambda x: x.values[0] if isinstance(x, pd.Series) else x).to_excel(writer, sheet_name='Statistiche')
        # Close the Pandas Excel writer and output the Excel file.
        writer.close()

    def Scrittura_F_NS(self,df,df_filtrato):# Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(self.filepath, engine='xlsxwriter')

        # Write each dataframe to a different worksheet.
        df.to_excel(writer, sheet_name='Originali')
        df_filtrato.to_excel(writer, sheet_name='Filtrati')

        # Close the Pandas Excel writer and output the Excel file.
        writer.close()

    def Scrittura_NF_S(self,df,statistica):# Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(self.filepath, engine='xlsxwriter')

        # Write each dataframe to a different worksheet.
        df.to_excel(writer, sheet_name='Originali')
        dascrivere = pd.DataFrame(statistica).T
        #dascrivere.to_excel(writer, sheet_name='Statistiche')
        dascrivere.applymap(lambda x: x.values[0] if isinstance(x, pd.Series) else x).to_excel(writer, sheet_name='Statistiche')
        # Close the Pandas Excel writer and output the Excel file.
        writer.close()

    def Scrittura_NF_NS(self,df):# Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(self.filepath, engine='xlsxwriter')

        # Write each dataframe to a different worksheet.
        df.to_excel(writer, sheet_name='Originali')

        # Close the Pandas Excel writer and output the Excel file.
        writer.close()

    def Scrittura_COP(self,df,df_COP):
        writer = pd.ExcelWriter(self.filepath, engine='xlsxwriter')

        # Write each dataframe to a different worksheet.
        df.to_excel(writer, sheet_name='Originali')
        df_COP.to_excel(writer, sheet_name='COP')

        # Close the Pandas Excel writer and output the Excel file.
        writer.close()
