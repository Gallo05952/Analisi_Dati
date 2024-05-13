import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import datetime
import os
  # Importa AperturaFile all'inizio del file

class Interfaccia:
        
    def __init__(self,root):
        self.root = root
        self.path_in = ""
        self.save_path = ""
        self.tempo = []
        self.FiltroIntervallo = False
        self.Filtro2 = False
        self.tempoIN = tk.StringVar()  # Inizializza self.tempoIN
        self.Tin = ttk.Combobox(textvariable=self.tempoIN)  
        # Inizializza self.Tin
        self.MediaS = False
        self.MedianaS = False
        self.ModaS = False
        self.DeviazioneS = False
        self.VarianzaS = False  
        self.minimoS = False
        self.massimoS = False
        self.Dati_grezziS = False
        self.Dati_filtratiS = False      
        self.current_time = datetime.datetime.now().strftime("%d-%m-%Y")
        self.filepathD = os.path.join(os.path.expanduser("~"), "Desktop")   
        self.filenameD = f"{self.current_time}_default_filename"

    def FinestraPrincipale(self):
        self.root.title("Finestra Principale")
        self.root.geometry("500x300")

        # TITOLO
        self.label_titolo= tk.Label(self.root, 
                                    text="Analisi Dati",
                                    font=("Helvetica", 18, "bold"))
        self.label_titolo.grid(row=0, column=0)

        # Import del file
        self.label_file_in= tk.Label(self.root, 
                                    text="File da importare",
                                    font=("Helvetica", 10, "bold"))
        self.label_file_in.grid(row=1, column=0)

        # TIPO DI PROGETTO - X IL FUTURO
        self.sfoglia_input=tk.Button(self.root,
                                    text="Seleziona file",
                                    font=("Helvetica", 10, "bold"),
                                    command=self.file_input_sfoglia)
        self.sfoglia_input.grid(row=1, column=1)

        #! MENU A DISCESA per la selezione del progetto nel caso di formato diversi con la stessa estensione
        # self.diversi_progetti = [
        #     "CD - DisCO2very",
        #     "CD - COP Aski",
        #     "Nitrati"]
        # self.progetto_selezionata = tk.StringVar(self.root)
        # self.menu_a_discesa = tk.OptionMenu(self.root, self.progetto_selezionata, *self.diversi_progetti)
        # self.menu_a_discesa.grid(row=1, column=2)
        
        # FILTRO
        self.pulsante_filtro = tk.Button(
                            self.root,
                            text="Filtra",
                            command=self.FinestraFiltro)
        self.pulsante_filtro.grid(row=2, column=0)

        # STATISTICHE
        self.pulsante_statistiche = tk.Button(
                            self.root,
                            text="Statistiche",
                            command=self.FinestraStatistiche)
        self.pulsante_statistiche.grid(row=2, column=1)

        # SALVATAGGIO
        # Label per mostrare il percorso di salvataggio
        self.save_label = tk.Label(self.root, 
                                text="Nessuna cartella di salvataggio selezionata",
                                font=("Helvetica", 10, "bold"))
        self.save_label.grid(row=3, column=1, padx=10, pady=10)

        # Bottone per sfogliare le cartelle di salvataggio
        self.save_button = tk.Button(self.root, 
                                    text="Sfoglia",
                                    command=self.save_in)
        self.save_button.grid(row=3, column=2, padx=10, pady=10)

            # Label per mostrare il percorso di salvataggio
        self.FileName = tk.Label(self.root,
                                text="Nome file finale:",
                                font=("Helvetica", 10, "bold"))
        self.FileName.grid(row=3, column=3, padx=10, pady=10)

        # Entry per inserire il nome del file
        self.file_nameC = tk.Entry(self.root)
        self.file_nameC.grid(row=3, column=4, padx=10, pady=10)
        self.OpzSalva=tk.BooleanVar()
        self.pulsante_salva = tk.Checkbutton(
            self.root,
            text="Salva",
            font=("Helvetica", 10, "bold"),
            variable=self.OpzSalva)
        self.pulsante_salva.grid(row=3, column=0)

        # Bottone OK
        self.ok_button = tk.Button(self.root,
                                text="OK",
                                font=("Helvetica", 18, "bold"),command=self.Salvataggio)
        self.ok_button.grid(row=4, column=2, padx=10, pady=10)

        self.filepath = ""
        self.save_path = ""
        self.FileName = ""

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
            self.OpzSalvaS=self.OpzSalva.get()
            self.file_name = self.file_nameC.get()
            print(self.file_name)
            if not self.file_name:  # Check if file_name is empty
                self.file_name = self.filenameD  
            if not self.save_path:
                self.save_path = self.filepathD
            self.savename = self.save_path + '/' + self.file_name + '_' + self.current_time +  ".xlsx"
            self.savename = self.savename.replace("/", '\\')
        except AttributeError:
            print("Errore")
        finally:
            getattr(self.root, 'destroy', lambda: None)()

    def FinestraStatistiche(self):
        self.finestra_stat = tk.Toplevel(self.root)
        self.finestra_stat.title("Finestra Statistiche")
        self.finestra_stat.geometry("1000x200")

        # CREAZIONE DELLE VARIABILI PER I CHECKBUTTON
        self.Media_var = tk.BooleanVar()
        self.Mediana_var = tk.BooleanVar()
        self.Moda_var = tk.BooleanVar()
        self.Deviazione_var = tk.BooleanVar()
        self.Varianza_var = tk.BooleanVar()
        self.minimo_var = tk.BooleanVar()
        self.massimo_var = tk.BooleanVar()
        self.Dati_grezzi_var = tk.BooleanVar()
        self.Dati_filtrati_var = tk.BooleanVar()

        # SEZIONE STATISTICHE
        self.testoStat = tk.Label(self.finestra_stat,
                            text="Seleziona la tipologia di statistica",
                            font=("Helvetica", 10, "bold"))
        self.testoStat.grid(row=0, column=0)
        # STATISTICA: MEDIA
        self.Media = tk.Checkbutton(self.finestra_stat, text="Media", variable=self.Media_var)
        self.Media.grid(row=1, column=0)
        # STATISTICA: MEDIANA
        self.Mediana = tk.Checkbutton(self.finestra_stat, text="Mediana", variable=self.Mediana_var)
        self.Mediana.grid(row=2, column=0)
        # STATISTICA: MODA
        self.Moda = tk.Checkbutton(self.finestra_stat, text="Moda", variable=self.Moda_var)
        self.Moda.grid(row=3, column=0)
        # STATISTICA: DEVIAZIONE STANDARD
        self.Deviazione = tk.Checkbutton(self.finestra_stat, text="Deviazione Standard", variable=self.Deviazione_var)
        self.Deviazione.grid(row=4, column=0)
        # STATISTICA: VARIANZA
        self.Varianza = tk.Checkbutton(self.finestra_stat, text="Varianza", variable=self.Varianza_var)
        self.Varianza.grid(row=5, column=0)
        # STATISTICA: MINIMO
        self.Minimo = tk.Checkbutton(self.finestra_stat, text="Minimo", variable=self.minimo_var)
        self.Minimo.grid(row=6, column=0)
        # STATISTICA: MASSIMO
        self.Massimo = tk.Checkbutton(self.finestra_stat, text="Massimo", variable=self.massimo_var)
        self.Massimo.grid(row=7, column=0)

        # SELEZIONA DATI    
        self.SelezionaDati = tk.Label(self.finestra_stat, 
                    text="Seleziona i dati su cui fare le statistiche",
                    font=("Helvetica", 10, "bold"))
        
        self.SelezionaDati.grid(row=0, column=2)
        self.Dati_grezzi = tk.Checkbutton(self.finestra_stat, text="Dati grezzi", variable=self.Dati_grezzi_var)
        self.Dati_grezzi.grid(row=1, column=2)
        self.Dati_filtrati = tk.Checkbutton(self.finestra_stat, text="Dati filtrati", variable=self.Dati_filtrati_var)
        self.Dati_filtrati.grid(row=2, column=2)


        # BOTTONE OK E CHIUSURA
        self.ok_button_stat = tk.Button(self.finestra_stat, text="OK", command=self.SalvataggioStat)
        self.ok_button_stat.grid(row=4, column=2, padx=10, pady=10)

    def SalvataggioStat(self):
        try:
            self.MediaS=self.Media_var.get()
            self.MedianaS=self.Mediana_var.get()
            self.ModaS=self.Moda_var.get()
            self.DeviazioneS=self.Deviazione_var.get()
            self.VarianzaS=self.Varianza_var.get()
            self.minimoS=self.minimo_var.get()
            self.massimoS=self.massimo_var.get()
            self.Dati_grezziS=self.Dati_grezzi_var.get()
            self.Dati_filtratiS=self.Dati_filtrati_var.get()
        except AttributeError:
            print("Errore")
        finally:
            getattr(self.finestra_stat, 'destroy', lambda: None)()

    def save_in(self):
        # Apri il dialogo per selezionare la directory
        self.save_path = filedialog.askdirectory()
        if self.save_path:
            self.save_label.config(text=f"Salva in: {self.save_path}")