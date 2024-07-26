# import numpy as np
import numpy as np
import pandas as pd
class ScambioTermico:

#     def __init__(self,df_MRU):
#         # in realtà gli passo tutto ma sono pigro e non ho voglia di cambiare i nomi in questa funzione
#         self.df_MRU = df_MRU
    
    def fluido(self,MRU):
        fluido = []
        for i in range(0,len(self.df_MRU)):   
            print(self.df_MRU[f'CO2_{MRU}'][i])
            CO2 = float(self.df_MRU[f'CO2_{MRU}'][i]) if not np.isnan(self.df_MRU[f'CO2_{MRU}'][i]) else 0
            if CO2 < 0:
                CO2 = 0
            CH4 = float(self.df_MRU[f'CH4_{MRU}'][i]) if not np.isnan(self.df_MRU[f'CH4_{MRU}'][i]) else 0
            if CH4 < 0:
                CH4 = 0
            N2 = float(self.df_MRU[f'N2_{MRU}'][i]) if not np.isnan(self.df_MRU[f'N2_{MRU}'][i]) else 0
            if N2 < 0:
                N2 = 0
            O2 = float(self.df_MRU[f'O2_{MRU}'][i]) if not np.isnan(self.df_MRU[f'O2_{MRU}'][i]) else 0
            if O2 < 0:
                O2 = 0
            H2S = float(self.df_MRU[f'H2S_{MRU}'][i]) if not np.isnan(self.df_MRU[f'H2S_{MRU}'][i]) else 0
            if H2S < 0:
                H2S = 0
            if (CO2 + CH4 + O2 + N2 + H2S) < 95:
                f = np.nan
            else:
                CO2=100-(CH4+O2+N2+H2S)
                f = f'CarbonDioxide[{CO2}]&Methane[{CH4}]&Nitrogen[{N2}]&Oxygen[{O2}]&HydrogenSulfide[{H2S}]'
            fluido.append(f)
        #aggiungi al dataframe df_MRU la colonna fluido_FT300
        self.df_MRU[f'fluido_{MRU}'] = fluido

    
#     def Entalpia(self,fluido,T,p,nome):
#         for i in range(0,len(self.df_MRU)):
#             if np.isnan(fluido[i]):
#                 self.df_MRU[f'Entalpia_{nome}'][i] = np.nan
#                 continue
#             else:
#                 h = self.CalcolaEntalpia(fluido[i],T[i],p[i])
#                 self.df_MRU[f'Entalpia_{nome}'][i] = h

#     def CalcolaEntalpia(self,fluido,T,p):
#         from CoolProp.CoolProp import PropsSI
#         p=(float(p)+1)*10**5
#         T=float(T)+273.15
#         h = PropsSI('H', 'P', p, 'T', T, fluido)
#         return h/1000
        
#     def Calcolo(self):
#         for i in range(1, 6):
#             self.df_MRU[f'Entalpia_fluido_MRU{i}'] = np.nan
#         self.fluido('MRU1')
#         self.fluido('MRU2')
#         self.fluido('MRU3')
#         self.fluido('MRU4')
#         self.fluido('MRU5')
#         self.Entalpia(self.df_MRU['fluido_MRU2'],self.df_MRU['TT201 Temperatura CO2 liquefatta dopo condensatore'],self.df_MRU['PT201 Pressione CO2 liquefatta post condensatore'],'fluido_MRU2')
#         self.Entalpia(self.df_MRU['fluido_MRU3'],self.df_MRU['TT122 Temperatura offgas ingresso condensatore'],self.df_MRU['PT120 Pressione offgas in ingresso alla torre distillazione'],'fluido_MRU3')
#         self.Entalpia(self.df_MRU['fluido_MRU4'],self.df_MRU['TT123 Temperatura offgas evaporato da colonna'],self.df_MRU['PT123 Pressione offgas evaporato da colonna'],'fluido_MRU4')
#         #! DA CAMBIARE LA TT300
#         self.Entalpia(self.df_MRU['fluido_MRU5'],self.df_MRU['TT201 Temperatura CO2 liquefatta dopo condensatore'],self.df_MRU['PT300 Pressione gas incondensabili in uscita condensatore'],'fluido_MRU5')
#         return self.df_MRU
#         #calcolo entalpia
#         #calcolo scambio termico



# class ScambioTermico:
    def __init__(self, df_MRU):
        self.df_MRU = df_MRU

    def Entalpia(self, fluido, T, p, nome):
        for i in range(len(fluido)):
            if pd.isna(fluido[i]) or pd.isna(T[i]) or pd.isna(p[i]):
                self.df_MRU.loc[i, f'Entalpia_{nome}'] = np.nan
                continue
            else:
                h = self.CalcolaEntalpia(fluido[i], T[i], p[i])
                self.df_MRU.loc[i, f'Entalpia_{nome}'] = h

    def CalcolaEntalpia(self, fluido, T, p):
        from CoolProp.CoolProp import PropsSI
        p = (float(p) + 1) * 10**5
        T = float(T) + 273.15
        h = PropsSI('H', 'P', p, 'T', T, fluido)
        return h / 1000

    def Calcolo(self):
        # Creare le colonne necessarie se non esistono
        for i in range(1, 6):
            col_name = f'fluido_MRU{i}'
            if col_name not in self.df_MRU.columns:
                self.df_MRU[col_name] = np.nan
            self.df_MRU[f'Entalpia_{col_name}'] = np.nan
        self.fluido('MRU1')
        self.fluido('MRU2')
        self.fluido('MRU3')
        self.fluido('MRU4')
        self.fluido('MRU5')
        if 'fluido_MRU2' in self.df_MRU.columns:
            self.Entalpia(self.df_MRU['fluido_MRU2'], self.df_MRU['TT201 Temperatura CO2 liquefatta dopo condensatore'], self.df_MRU['PT201 Pressione CO2 liquefatta post condensatore'], 'fluido_MRU2')
        if 'fluido_MRU3' in self.df_MRU.columns:
            self.Entalpia(self.df_MRU['fluido_MRU3'], self.df_MRU['TT122 Temperatura offgas ingresso condensatore'], self.df_MRU['PT120 Pressione offgas in ingresso alla torre distillazione'], 'fluido_MRU3')
        if 'fluido_MRU4' in self.df_MRU.columns:
            self.Entalpia(self.df_MRU['fluido_MRU4'], self.df_MRU['TT123 Temperatura offgas evaporato da colonna'], self.df_MRU['PT123 Pressione offgas evaporato da colonna'], 'fluido_MRU4')
        if 'fluido_MRU5' in self.df_MRU.columns:
            self.Entalpia(self.df_MRU['fluido_MRU5'], self.df_MRU['TT201 Temperatura CO2 liquefatta dopo condensatore'], self.df_MRU['PT300 Pressione gas incondensabili in uscita condensatore'], 'fluido_MRU5')
        return self.df_MRU

    def fluido(self, nome):
        # Implementazione del metodo fluido
        pass