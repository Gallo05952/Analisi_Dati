import tkinter as tk

class Filtro:

    def __init__(self,root):
        self.root = root

    def FinestraFiltro(self, ):
        self.finestra_filtro = tk.Toplevel(self.root)
        self.finestra_filtro.title("Finestra Filtro")
        self.finestra_filtro.geometry("1000x200")

        # # Creazione delle variabili per i Checkbutton
        # self.IntervalloT = tk.BooleanVar()
        # self.IntervalloT.trace('w', self.update_checkboxes)
        # self.DaTempo = tk.BooleanVar()
        # self.DaTempo.trace('w', self.update_checkboxes)

        # # SEZIONE FILTRO
        # self.testoFiltro = tk.Label(self.finestra_filtro,
        #                     text="Seleziona la tipologia di filtro", 
        #                     font=("Helvetica", 10, "bold"),
        #                     fg="red")
        # self.testoFiltro.grid(row=0, column=0)
        # # FILTRO INTERVALLO DI TEMPO
        # # TEMPO INIZIO
        # self.checkFiltro1 = tk.Checkbutton(self.finestra_filtro, text="Intervallo di tempo", variable=self.IntervalloT)
        # self.checkFiltro1.grid(row=1, column=0)
        # self.TempoInizio = tk.Label(self.finestra_filtro, text="Tempo di inizio")
        # self.TempoInizio.grid(row=1, column=1)
        # self.tempoIN = tk.StringVar()
        # self.Tin = ttk.Combobox(self.finestra_filtro, textvariable=self.tempoIN)  # Usa ttk.Combobox invece di tk.OptionMenu
        # self.Tin['values'] = self.tempo  # Imposta i valori del Combobox
        # self.Tin.grid(row=1, column=2)
        # # TEMPO FINE
        # self.TempoFine = tk.Label(self.finestra_filtro, text="Tempo di fine")
        # self.TempoFine.grid(row=1, column=3)
        # self.tempoFIN = tk.StringVar()
        # self.Tfin = ttk.Combobox(self.finestra_filtro, textvariable=self.tempoFIN)
        # self.Tfin['values'] = self.tempo
        # self.Tfin.grid(row=1, column=4)
        # # FILTRO SCARTO INIZIALE TEMPORALE
        # self.Filtro2 = tk.Checkbutton(self.finestra_filtro, text="Scarto Iniziale", variable=self.DaTempo)
        # self.Filtro2.grid(row=3, column=0)
        # self.TempoDa = tk.Label(self.finestra_filtro, text="Tempo d'inizio")
        # self.TempoDa.grid(row=3, column=1)
        # self.tempoDa=tk.StringVar()
        # self.TDa=ttk.Combobox(self.finestra_filtro, textvariable=self.tempoDa)
        # self.TDa['values']=self.tempo
        # self.TDa.grid(row=3, column=2)
        # # BOTTONE OK E CHIUSURA
        # self.ok_button = tk.Button(self.finestra_filtro, text="OK", command=self.SalvataggioFiltro)
        # self.ok_button.grid(row=4, column=2, padx=10, pady=10)