
import pandas as pd

class UnisciDF2:
    def __init__(self, df_DaUnire, df_Unito):
        self.df_DaUnire = df_DaUnire
        self.df_Unito = None

    def converti_datetime(self, df, colonna, formato):
        try:
            df[colonna] = pd.to_datetime(df[colonna], format=formato)
        except ValueError as e:
            print(f"Errore di conversione: {e}")

    def correzione_secondi(self, x):
        return x - pd.Timedelta(seconds=1) if x.second % 2 != 0 else x

    def Unisci(self):
        

        # Conversione delle date in modo vettorializzato
        self.converti_datetime(self.df, self.df.columns[0], '%Y-%m-%d %H:%M:%S')
        self.converti_datetime(self.df_VAR, self.df_VAR.columns[0], '%d.%m.%Y %H:%M:%S')
        self.converti_datetime(self.df_VAR2, self.df_VAR2.columns[0], '%d.%m.%Y %H:%M:%S')

        # Applicazione della correzione dei secondi
        self.df_VAR.iloc[:, 0] = self.df_VAR.iloc[:, 0].apply(self.correzione_secondi)
        self.df_VAR2.iloc[:, 0] = self.df_VAR2.iloc[:, 0].apply(self.correzione_secondi)
        self.df.rename(columns={self.df.columns[0]: 'Ora'}, inplace=True)
        self.df_VAR.rename(columns={self.df_VAR.columns[0]: 'Ora'}, inplace=True)
        self.df_VAR2.rename(columns={self.df_VAR2.columns[0]: 'Ora'}, inplace=True)
        # Merge dei DataFrame
        merged_df = pd.merge(self.df, self.df_VAR, on='Ora', how='outer')
        self.df_VAR2 = self.df_VAR2.rename(columns=lambda x: x + "_2")
        merged_df = pd.merge(merged_df, self.df_VAR2, left_on='Ora', right_on='Ora_2', how='outer')

        print("Merge completato")
        # tempo start is when the majority of the column is not empty
        # Step 1: Count non-NaN values per row
        non_empty_counts = merged_df.notna().sum(axis=1)

        # Step 2: Calculate the majority threshold
        majority_threshold = len(merged_df.columns) / 2

        # Step 3: Find the row index where the majority of columns become non-NaN
        majority_row_index = non_empty_counts[non_empty_counts > majority_threshold].index[0]

        # Step 4: Filter 'tempo' variable from the identified row onwards
        tempo = list(merged_df.iloc[majority_row_index:, 0])

        # tempo = list(merged_df.iloc[:, 0])
        return merged_df, tempo
