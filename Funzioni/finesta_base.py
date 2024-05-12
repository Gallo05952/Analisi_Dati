import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
  # Importa AperturaFile all'inizio del file

class Interfaccia:
        
    def __init__(self,root):
        self.root = root
        self.path_in = ""
        self.save_path = ""
        self.tempo = []
        self.FiltroIntervallo = False
        self.tempoIN = tk.StringVar()  # Inizializza self.tempoIN
        self.Tin = ttk.Combobox(textvariable=self.tempoIN)  # Inizializza self.Tin
        

    def FinestraPrincipale(self):
        self.root.title("Finestra Principale")
        self.root.geometry("500x300")

        # TITOLO
        self.label_titolo= tk.Label(self.root, text="Analisi Dati")
        self.label_titolo.grid(row=0, column=0)

        # Import del file
        self.label_file_in= tk.Label(self.root, text="File da importare")
        self.label_file_in.grid(row=1, column=0)

        # TIPO DI PROGETTO - X IL FUTURO
        self.sfoglia_input=tk.Button(self.root,
                                    text="Seleziona da file",
                                    command=self.file_input_sfoglia)
        self.sfoglia_input.grid(row=1, column=1)

        self.diversi_progetti = [
            "CD - DisCO2very",
            "CD - COP Aski",
            "Nitrati"]
        self.progetto_selezionata = tk.StringVar(self.root)
        self.menu_a_discesa = tk.OptionMenu(self.root, self.progetto_selezionata, *self.diversi_progetti)
        self.menu_a_discesa.grid(row=1, column=2)
        
        # FILTRO
        self.pulsante_filtro = tk.Button(
                            self.root,
                            text="Filtra",
                            command=self.FinestraFiltro)
        self.pulsante_filtro.grid(row=2, column=0)

        # Bottone OK
        self.ok_button = tk.Button(self.root, text="OK", command=self.Salvataggio)
        self.ok_button.grid(row=4, column=2, padx=10, pady=10)

    def file_input_sfoglia(self):
        ####
        # SELEZIONE DEL FILE E CARICAMENTO DEI DATI
        ####
        from . import AperturaFile
        self.path_in = filedialog.askopenfilename()
        if self.path_in:  # Aggiorna il Label solo se è stato selezionato un file
            self.label_file_in.config(text=self.path_in)
            self.df=AperturaFile(self.path_in).Apertura() #se cambia il formato vai in AperuraFile e aggiungi la funzione di conversione da file a dataframe
            self.tempo=list(self.df['Data'].unique())
            print(self.df['Data'])

    def FinestraFiltro(self):
        self.finestra_filtro = tk.Toplevel(self.root)
        self.finestra_filtro.title("Finestra Filtro")
        self.finestra_filtro.geometry("1000x200")

        # Creazione delle variabili per i Checkbutton
        self.IntervalloT = tk.BooleanVar()
        self.IntervalloT.trace('w', self.update_checkboxes)
        self.DaTempo = tk.BooleanVar()
        self.DaTempo.trace('w', self.update_checkboxes)

        # SEZIONE FILTRO
        self.testoFiltro = tk.Label(self.finestra_filtro, text="Seleziona la tipologia di filtro")
        self.testoFiltro.grid(row=0, column=0)
        # FILTRO INTERVALLO DI TEMPO
        # TEMPO INIZIO
        self.checkFiltro1 = tk.Checkbutton(self.finestra_filtro, text="Intervallo di tempo", variable=self.IntervalloT)
        self.checkFiltro1.grid(row=1, column=0)
        self.TempoInizio = tk.Label(self.finestra_filtro, text="Tempo di inizio")
        self.TempoInizio.grid(row=1, column=2)
        self.tempoIN = tk.StringVar()
        self.Tin = ttk.Combobox(self.finestra_filtro, textvariable=self.tempoIN)  # Usa ttk.Combobox invece di tk.OptionMenu
        self.Tin['values'] = self.tempo  # Imposta i valori del Combobox
        self.Tin.grid(row=1, column=3)
        # TEMPO FINE
        self.TempoFine = tk.Label(self.finestra_filtro, text="Tempo di fine")
        self.TempoFine.grid(row=1, column=5)
        self.tempoFIN = tk.StringVar()
        self.Tfin = ttk.Combobox(self.finestra_filtro, textvariable=self.tempoFIN)
        self.Tfin['values'] = self.tempo
        self.Tfin.grid(row=1, column=6)
        # FILTRO SCARTO INIZIALE TEMPORALE
        self.Filtro2 = tk.Checkbutton(self.finestra_filtro, text="Scarto Iniziale", variable=self.DaTempo)
        self.Filtro2.grid(row=3, column=0)
        self.TempoDa = tk.Label(self.finestra_filtro, text="Tempo d'inizio")
        self.TempoDa.grid(row=3, column=1)
        self.tempoDa=tk.StringVar()
        self.TDa=ttk.Combobox(self.finestra_filtro, textvariable=self.tempoDa)
        self.TDa['values']=self.tempo
        self.TDa.grid(row=3, column=2)
        # BOTTONE OK E CHIUSURA
        self.ok_button = tk.Button(self.finestra_filtro, text="OK", command=self.SalvataggioFiltro)
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
                print(self.TempoIniziale)
                self.TempoFinale=self.tempoFIN.get()
                print(self.TempoFinale)
            elif (self.Filtro2==True and self.TDa.get()):
                self.TempoDa=self.TDa.get() 
        except AttributeError:
            print("Errore: Il filtro non è stato ancora applicato.")
        finally:
            getattr(self.finestra_filtro, 'destroy', lambda: None)()  # Chiude la finestra secondaria

    def Salvataggio(self):  
        try:
            print("BEPPEEE")
        except AttributeError:
            print("Errore")
        finally:
            getattr(self.root, 'destroy', lambda: None)()