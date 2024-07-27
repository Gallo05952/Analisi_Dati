# import numpy as np
import numpy as np
import pandas as pd
from CoolProp.CoolProp import PropsSI
class ScambioTermico:

    def __init__(self,df_MRU):
        # in realtà gli passo tutto ma sono pigro e non ho voglia di cambiare i nomi in questa funzione
        self.df_MRU = df_MRU
    
    def fluido(self,MRU):
        fluido = []
        for i in range(0,len(self.df_MRU)):   
            print(self.df_MRU[f'CO2_{MRU}'][i])
            CO2 = float(self.df_MRU[f'CO2_{MRU}'][i])/100 if not np.isnan(self.df_MRU[f'CO2_{MRU}'][i]) else 0
            if CO2 < 0:
                CO2 = 0
            CH4 = float(self.df_MRU[f'CH4_{MRU}'][i])/100 if not np.isnan(self.df_MRU[f'CH4_{MRU}'][i]) else 0
            if CH4 < 0:
                CH4 = 0
            N2 = float(self.df_MRU[f'N2_{MRU}'][i])/100 if not np.isnan(self.df_MRU[f'N2_{MRU}'][i]) else 0
            if N2 < 0:
                N2 = 0
            O2 = float(self.df_MRU[f'O2_{MRU}'][i])/100 if not np.isnan(self.df_MRU[f'O2_{MRU}'][i]) else 0
            if O2 < 0:
                O2 = 0
            H2S = float(self.df_MRU[f'H2S_{MRU}'][i])/100 if not np.isnan(self.df_MRU[f'H2S_{MRU}'][i]) else 0
            if H2S < 0:
                H2S = 0
            if (CO2 + CH4 + O2 + N2 + H2S) < 0.95:
                f = np.nan
            else:
                CO2=1-(CH4+O2+N2+H2S)
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
        
    def Calcolo(self):
        for i in range(1, 6):
            self.df_MRU[f'Entalpia_fluido_MRU{i}'] = np.nan
        self.fluido('MRU1')
        self.fluido('MRU2')
        self.fluido('MRU3')
        self.fluido('MRU4')
        self.fluido('MRU5')
        if 'fluido_MRU1' in self.df_MRU.columns:
            self.Entalpia(self.df_MRU['fluido_MRU1'], self.df_MRU['TT201 Temperatura CO2 liquefatta dopo condensatore'], self.df_MRU['PT201 Pressione CO2 liquefatta post condensatore'], 'fluido_MRU1')
        if 'fluido_MRU2' in self.df_MRU.columns:
            self.Entalpia(self.df_MRU['fluido_MRU2'], self.df_MRU['TT201 Temperatura CO2 liquefatta dopo condensatore'], self.df_MRU['PT201 Pressione CO2 liquefatta post condensatore'], 'fluido_MRU2')
        if 'fluido_MRU3' in self.df_MRU.columns:
            self.Entalpia(self.df_MRU['fluido_MRU3'], self.df_MRU['TT122 Temperatura offgas ingresso condensatore'], self.df_MRU['PT120 Pressione offgas in ingresso alla torre distillazione'], 'fluido_MRU3')
        if 'fluido_MRU4' in self.df_MRU.columns:
            self.Entalpia(self.df_MRU['fluido_MRU4'], self.df_MRU['TT123 Temperatura offgas evaporato da colonna'], self.df_MRU['PT123 Pressione offgas evaporato da colonna'], 'fluido_MRU4')
        if 'fluido_MRU5' in self.df_MRU.columns:
            self.Entalpia(self.df_MRU['fluido_MRU5'], self.df_MRU['TT201 Temperatura CO2 liquefatta dopo condensatore'], self.df_MRU['PT300 Pressione gas incondensabili in uscita condensatore'], 'fluido_MRU5')
        self.Q()
        return self.df_MRU
# #         #! DA CAMBIARE LA TT300




# # class ScambioTermico:
#     def __init__(self, df_MRU):
#         self.df_MRU = df_MRU

    def Entalpia(self, fluido, T, p, nome):
        self.df_MRU[f'Entalpia_{nome}'] = np.nan
        for i in range(len(fluido)):
            T_i = float(T[i])
            p_i = float(p[i])
            fluido_i = fluido[i]
            if pd.isna(fluido_i) or pd.isna(T_i) or pd.isna(p_i):
                self.df_MRU.loc[i, f'Entalpia_{nome}'] = np.nan
            else:
                try:
                    if nome == 'fluido_MRU2':                       
                        h = self.CalcolaEntalpiaL(fluido[i], T[i], p[i])
                        self.df_MRU.loc[i, f'Entalpia_{nome}'] = h
                    else:
                        h = self.CalcolaEntalpia(fluido[i], T[i], p[i])
                        self.df_MRU.loc[i, f'Entalpia_{nome}'] = h
                except ValueError as e:
                    print(f"Errore nel calcolo dell'entalpia per {nome} alla riga {i}: {e}")
                    self.df_MRU.loc[i, f'Entalpia_{nome}'] = np.nan
                # h = self.CalcolaEntalpia(fluido_i, T_i, p_i)
                # self.df_MRU.loc[i, f'Entalpia_{nome}'] = h

    def CalcolaEntalpia(self, fluido, T, p):
        try:
            p = (float(p) + 1) * 10**5
            T = float(T) + 273.15
            h = PropsSI('H', 'P|gas', p, 'T', T, fluido)
            return h / 1000
        except Exception as e:
            raise ValueError(f"Errore nel calcolo dell'entalpia: {e}")
        
    def CalcolaEntalpiaL(self, fluido, T, p):
        try:
            p = (float(p) + 1) * 10**5
            T = float(T) + 273.15
            h = PropsSI('H', 'P', p, 'T|liquid', T, fluido)
            return h / 1000
        except Exception as e:
            raise ValueError(f"Errore nel calcolo dell'entalpia: {e}")

    def Q(self):
        self.df_MRU['Q [kW]'] = np.nan
        for i in range(len(self.df_MRU)):
            if  pd.isna(self.df_MRU['fluido_MRU2'][i]) or pd.isna(self.df_MRU['fluido_MRU3'][i]) or pd.isna(self.df_MRU['fluido_MRU4'][i]) or pd.isna(self.df_MRU['fluido_MRU5'][i]):
                self.df_MRU.loc[i, 'Q [kW]'] = np.nan
            else:
                try:
                    h_120 = self.df_MRU['Entalpia_fluido_MRU3'][i]
                    m_120=self.df_MRU['FT120 Portata offgas in ingresso alla torre distillazione'][i]
                    h_123 = self.df_MRU['Entalpia_fluido_MRU4'][i]
                    m_123=self.df_MRU['FT123 Portata offgas evaporato da colonna'][i]
                    h_201 = self.df_MRU['Entalpia_fluido_MRU2'][i]
                    m_201=self.df_MRU['FT201 Portata CO2 liquefatta dopo condensatore'][i]
                    h_300 = self.df_MRU['Entalpia_fluido_MRU5'][i]
                    if m_120+m_123-m_201 > 0:
                        m_300=m_120+m_123-m_201
                    else:
                        m_300=0
                    self.df_MRU.loc[i, 'Q [kW]'] = (m_120*h_120+m_123*h_123-m_201*h_201-m_300*h_300)/3600
                except ValueError as e:
                    print(f"Errore nel calcolo del calore scambiato alla riga {i}: {e}")
                    self.df_MRU.loc[i, 'Q [kW]'] = np.nan
#     def Calcolo(self):
#         # Creare le colonne necessarie se non esistono
#         for i in range(1, 6):
#             col_name = f'fluido_MRU{i}'
#             if col_name not in self.df_MRU.columns:
#                 self.df_MRU[col_name] = np.nan
#             self.df_MRU[f'Entalpia_{col_name}'] = np.nan
#         self.fluido('MRU1')
#         self.fluido('MRU2')
#         self.fluido('MRU3')
#         self.fluido('MRU4')
#         self.fluido('MRU5')
#         if 'fluido_MRU1' in self.df_MRU.columns:
#             self.Entalpia(self.df_MRU['fluido_MRU1'], self.df_MRU['TT201 Temperatura CO2 liquefatta dopo condensatore'], self.df_MRU['PT201 Pressione CO2 liquefatta post condensatore'], 'fluido_MRU1')
#         if 'fluido_MRU2' in self.df_MRU.columns:
#             self.Entalpia(self.df_MRU['fluido_MRU2'], self.df_MRU['TT201 Temperatura CO2 liquefatta dopo condensatore'], self.df_MRU['PT201 Pressione CO2 liquefatta post condensatore'], 'fluido_MRU2')
#         if 'fluido_MRU3' in self.df_MRU.columns:
#             self.Entalpia(self.df_MRU['fluido_MRU3'], self.df_MRU['TT122 Temperatura offgas ingresso condensatore'], self.df_MRU['PT120 Pressione offgas in ingresso alla torre distillazione'], 'fluido_MRU3')
#         if 'fluido_MRU4' in self.df_MRU.columns:
#             self.Entalpia(self.df_MRU['fluido_MRU4'], self.df_MRU['TT123 Temperatura offgas evaporato da colonna'], self.df_MRU['PT123 Pressione offgas evaporato da colonna'], 'fluido_MRU4')
#         if 'fluido_MRU5' in self.df_MRU.columns:
#             self.Entalpia(self.df_MRU['fluido_MRU5'], self.df_MRU['TT201 Temperatura CO2 liquefatta dopo condensatore'], self.df_MRU['PT300 Pressione gas incondensabili in uscita condensatore'], 'fluido_MRU5')
#         return self.df_MRU

#     def fluido(self, nome):
#         # Implementazione del metodo fluido
#         pass