import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from .filtri import FiltroTempo
class Filtro:

    def __init__(self,root, tempo, df):
        self.root = root
        self.tempo = tempo
        self.df = df

    def FinestraFiltro(self ):
        self.finestra_filtro = tk.Toplevel(self.root)
        self.finestra_filtro.title("Finestra Filtro")
        self.finestra_filtro.geometry("1000x200")
        # Creazione delle variabili per i Checkbutton
        self.IntervalloT = tk.BooleanVar()
        self.IntervalloT.trace('w', self.update_checkboxes)
        self.DaTempo = tk.BooleanVar()
        self.DaTempo.trace('w', self.update_checkboxes)

        # SEZIONE FILTRO
        self.testoFiltro = tk.Label(self.finestra_filtro,
                            text="Seleziona la tipologia di filtro", 
                            font=("Helvetica", 14, "bold"),
                            fg="red")
        self.testoFiltro.grid(row=0, column=0)

        # FILTRO INTERVALLO DI TEMPO
        # TEMPO INIZIO
        self.checkFiltro1 = tk.Checkbutton(self.finestra_filtro, 
                                        text="Intervallo di tempo", 
                                        font=("Helvetica", 12),
                                        variable=self.IntervalloT)
        self.checkFiltro1.grid(row=1, column=0)

        self.TempoInizio = tk.Label(self.finestra_filtro,
                                    text="Tempo di inizio",
                                    font=("Helvetica", 12))
        self.TempoInizio.grid(row=1, column=1)

        self.tempoIN = tk.StringVar()
        self.Tin = ttk.Combobox(self.finestra_filtro,
                                textvariable=self.tempoIN,
                                values=self.tempo)  # Usa ttk.Combobox invece di tk.OptionMenu
        # self.Tin['values'] = self.tempo  # Imposta i valori del Combobox
        self.Tin.grid(row=1, column=2)
        # TEMPO FINE
        self.TempoFine = tk.Label(self.finestra_filtro,
                                text="Tempo di fine",
                                font=("Helvetica", 12))
        self.TempoFine.grid(row=1, column=3)

        self.tempoFIN = tk.StringVar()
        self.Tfin = ttk.Combobox(self.finestra_filtro, 
                                textvariable=self.tempoFIN,
                                values=self.tempo)
        # self.Tfin['values'] = self.tempo
        self.Tfin.grid(row=1, column=4)

        # FILTRO SCARTO INIZIALE TEMPORALE
        self.Filtro2 = tk.Checkbutton(self.finestra_filtro,
                                    text="Scarto Iniziale", 
                                    font=("Helvetica", 12),
                                    variable=self.DaTempo)
        self.Filtro2.grid(row=3, column=0)

        self.TempoDa = tk.Label(self.finestra_filtro,
                                text="Tempo d'inizio",
                                font=("Helvetica", 12))
        self.TempoDa.grid(row=3, column=1)

        self.tempoDa=tk.StringVar()
        self.TDa=ttk.Combobox(self.finestra_filtro,
                            textvariable=self.tempoDa,
                            values=self.tempo)
#        self.TDa['values']=self.tempo
        self.TDa.grid(row=3, column=2)

        #BOTTONE OK E CHIUSURA
        self.ok_button = tk.Button(self.finestra_filtro,
                                    text="OK",
                                    font=("Helvetica", 12),
                                    command=self.SalvataggioFiltro)
        self.ok_button.grid(row=4, column=2, padx=10, pady=10)

    def update_checkboxes(self, *args):
        if self.IntervalloT.get():
            self.Filtro2.config(state='disabled')
        elif self.DaTempo.get():
            self.checkFiltro1.config(state='disabled')
        else:
            self.checkFiltro1.config(state='normal')
            self.Filtro2.config(state='normal')

    def SalvataggioFiltro(self):
        try:
            # checkbox filtro intervallo di tempo
            self.FiltroIntervallo=self.IntervalloT.get() 
            # checkbox filtro scarto iniziale
            self.Filtro2=self.DaTempo.get()
            
            if (self.IntervalloT.get()==True and
                self.Tin.get() and
                self.Tfin.get()):
                # se sono in intervallo e i menu sono compilati
                self.TempoIniziale=self.Tin.get()
                # print(self.TempoIniziale)
                self.TempoFinale=self.tempoFIN.get()
                # print(self.TempoFinale)
            elif (self.Filtro2==True and self.TDa.get()):
                self.TempoDa=self.TDa.get() 
        except AttributeError:
            print("Errore: Il filtro non è stato ancora applicato.")
        finally:
            getattr(self.finestra_filtro, 'destroy', lambda: None)()  # Chiude la finestra secondaria

    def get_preferenze(self):
        return self.FiltroIntervallo, self.Filtro2
    
    def get_variabili(self):
        if type(self.TempoIniziale)==str:
            TempoIniziale = self.TempoIniziale
        else:
            TempoIniziale = None
        if type(self.TempoFinale)==str:
            TempoFinale = self.TempoFinale
        else:
            TempoFinale = None
        if type(self.TempoDa)==str:
            TempoDa = self.TempoDa
        else:
            TempoDa = None
 
        return TempoIniziale, TempoFinale, TempoDa
    
    def DataFrame_filtrato(self):
        pref=self.get_preferenze()
        if pref[0]==True:
            df_filtrato=FiltroTempo(self.df).FiltraPerTempo(self.TempoIniziale,
                                                self.TempoFinale)
        elif pref[1]==True:
            df_filtrato=FiltroTempo(self.df).FineTransitorio(self.TempoDa)
        else:
            # finestra di errore
            messagebox.showerror("Errore", "Nessun filtro selezionato")
            df_filtrato=[]
        return df_filtrato