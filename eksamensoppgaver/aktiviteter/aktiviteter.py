import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns

class App:
    def __init__(self):
        # Data - Må tilpasses filen du bruker
        self.data = self.hent_data("tips")
        self.filtrert_data = self.data.copy()

        # Root
        self.root = tk.Tk()
        self.root.title("Databehandling GUI")
        self.root.geometry("800x600")
        self.root.protocol("WM_DELETE_WINDOW", self.ved_avslutning) # Sørger for korrekt avslutning

        # Lager mulighet for å bytte mellom tabell og diagram
        self.lag_visning()

        self.lag_filter()

        # Frame for innhold
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.canvas = None
        self.oppdater_visning()

    def hent_data(self, filnavn):
        # Laster inn og renser data fra fil - Må tilpasses hver enkelt problemstilling
        df = pd.read_csv("aktiviteter.csv", sep=";", encoding="utf-8")
        df.columns = ["Aktiviteter", "Kjønn", "Tidsbruk"]
        return df

    def lag_visning(self):
        # Lager en ramme med radioknapper som kan kontrollere visning
        self.visning_frame = tk.Frame(self.root)
        self.visning_frame.pack(anchor=tk.N, pady=10)

        self.visning = tk.StringVar(value="tabell")
        tk.Radiobutton(self.visning_frame, text="Tabell", variable=self.visning, value="tabell", command=self.oppdater_visning).pack(side=tk.LEFT, anchor=tk.N)
        tk.Radiobutton(self.visning_frame, text="Diagram", variable=self.visning, value="diagram", command=self.oppdater_visning).pack(side=tk.LEFT, anchor=tk.N)

    def lag_filter(self):
        self.filter_frame = tk.Frame(self.root)
        self.filter_frame.pack(anchor=tk.N, pady=10)

        self.valg = tk.StringVar(value="Alle")

        tk.Label(self.filter_frame, text="Velg kjønn").pack(side=tk.LEFT, padx=5)
        self.valg_dropdown = ttk.Combobox(self.filter_frame, textvariable=self.valg, values=["Alle", "Menn", "Kvinner"], state="readonly")
        self.valg_dropdown.pack(side=tk.LEFT, padx=5)

        tk.Button(self.filter_frame, text="Oppdater", command=self.oppdater_data, padx=10, pady=10).pack(side=tk.LEFT, padx=10)

    def oppdater_data(self):
        valg = self.valg.get()
        self.filtrert_data = self.data[self.data["Kjønn"] == valg]
        self.oppdater_visning()

    def lag_tabell(self):
        # Lager en tabell med filtrerte data
        tree = ttk.Treeview(self.frame, columns=list(self.filtrert_data.columns), show="headings", height=10)

        for col in self.filtrert_data.columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.CENTER)

        for _, row in self.filtrert_data.iterrows():
            tree.insert("", tk.END, values=list(row))

        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def lag_diagram(self):
        # Lager et diagram - Må tilpasses hvert enkelt datasett

        # Lager figur med to diagrammer (1 rad og 2 kolonner)
        fig, ax = plt.subplots(1, 2, figsize=(14, 6))

        # Filtrerer vekk linjene der Aktivitet starter med det rare symbolet og gjerner "I alt"-linjen
        aktiviteter = self.filtrert_data[~self.filtrert_data["Aktiviteter"].str.startswith("�")]
        aktiviteter = aktiviteter[aktiviteter["Aktiviteter"] != "I alt"]

        # ax[0] er første diagram, ax[1] er andre diagram.
        # I første diagram er x og y byttet slik at man før et horisontalt stolpediagram
        sns.barplot(data=aktiviteter, y="Aktiviteter", x="Tidsbruk", ax=ax[0], label="Tidsbruk i timer", palette="viridis")
        ax[0].set_title("Tidsbruk")

        ax[1].pie(aktiviteter["Tidsbruk"], labels=aktiviteter["Aktiviteter"], autopct="%0.1f%%")
        ax[1].set_title("Andel tidsbruk")
        
        # Layout slik at at man får med seg alt av innhold. Visning fungerer best utvidet til full skjerm
        fig.tight_layout()

        self.canvas = FigureCanvasTkAgg(fig, master=self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def oppdater_visning(self):
        # Oppdater visning

        # Slett alt innhold i self.frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.frame.pack(anchor=tk.N, pady=10, fill=tk.BOTH, expand=True)

        if self.visning.get() == "tabell":
            self.lag_tabell()
        elif self.visning.get() == "diagram":
            self.lag_diagram()

    def ved_avslutning(self):
        # Håndterer avslutning korrekt
        if self.canvas:
            plt.close('all')
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()