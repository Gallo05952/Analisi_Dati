import pandas as pd
from datetime import datetime, timedelta

class FiltroTempo:
    def __init__(self,df):
        self.df = df.copy()
        self.time=self.df.iloc[:,0]

    def FineTransitorio(self, tempo):
        tempo = datetime.strptime(tempo, '%H:%M').time()  # Convert the string to a datetime.time object
        start_time = datetime.strptime(self.time[0], '%H:%M').time()  
        # Convert the string to a time object

        # Convert both times to datetime objects with an arbitrary date
        start_datetime = datetime.combine(datetime(1, 1, 1), start_time)
        tempo_datetime = datetime.combine(datetime(1, 1, 1), tempo)

        # Add the timedelta to start_datetime
        end_datetime = start_datetime + (tempo_datetime - start_datetime)
        end_time = end_datetime.time()  # Convert back to time object

        # Convert the first column to datetime.time
        self.df.iloc[:, 0] = pd.to_datetime(self.df.iloc[:, 0], format='%H:%M').dt.time
        
        df_filtered = self.df[self.df.iloc[:, 0] >= end_time].copy()
        print(end_time)
        return df_filtered