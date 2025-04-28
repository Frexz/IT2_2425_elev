import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns

class App:
    def __init__(self):
        # Data
        self.data = self.hent_data("fodselstall.csv")
        self.filtrert_data = self.data.copy()

        # Root
        self.root = tk.Tk()
        self.root.title("Føsdselstall GUI")
        self.root.geometry("800x600")
        self.root.protocol("WM_DELETE_WINDOW", self.ved_avslutning) # Sørger for korrekt avslutning

        # Lager mulighet for visning
        self.lag_visning()

        # Lager mulighet for filtrering
        self.lag_filter()

        # Frame for innhold
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.canvas = None
        self.oppdater_visning()

    def hent_data(self, filnavn):
        # Laster inn og renser data fra fil
        df = pd.read_csv(filnavn, encoding="latin", sep="\t").fillna(0)
        df.columns = ["år", "fødselstall", "innflyttinger", "utflyttinger"]
        df.replace("..", 0, inplace=True)
        df = df.apply(pd.to_numeric, errors="coerce", axis=1).fillna(0)
        df["netto folkevekst"] = df["fødselstall"] + df["innflyttinger"] - df["utflyttinger"]
        return df

    def lag_visning(self):
        # Lager en ramme med radioknapper som kan kontrollere visning
        self.visning_frame = tk.Frame(self.root)
        self.visning_frame.pack(anchor=tk.N, pady=10)

        self.visning = tk.StringVar(value="tabell")
        tk.Radiobutton(self.visning_frame, text="Tabell", variable=self.visning, value="tabell", command=self.oppdater_visning).pack(side=tk.LEFT, anchor=tk.N)
        tk.Radiobutton(self.visning_frame, text="Diagram", variable=self.visning, value="diagram", command=self.oppdater_visning).pack(side=tk.LEFT, anchor=tk.N)

    def lag_filter(self):
        # Lager nedtrekksmenyer med mulighet for filtrering på årstall
        self.filter_frame = tk.Frame(self.root)
        self.filter_frame.pack(anchor=tk.N, pady=10)

        self.startår = tk.StringVar(value=str(self.data["år"].min()))
        self.sluttår = tk.StringVar(value=str(self.data["år"].max()))

        tk.Label(self.filter_frame, text="Startår").pack(side=tk.LEFT, padx=5)
        self.startår_dropdown = ttk.Combobox(self.filter_frame, textvariable=self.startår, values=list(self.data["år"]), state="readonly")
        self.startår_dropdown.pack(side=tk.LEFT, padx=5)

        tk.Label(self.filter_frame, text="Sluttår").pack(side=tk.LEFT, padx=5)
        self.sluttår_dropdown = ttk.Combobox(self.filter_frame, textvariable=self.sluttår, values=list(self.data["år"]), state="readonly")
        self.sluttår_dropdown.pack(side=tk.LEFT, padx=5)

        tk.Button(self.filter_frame, text="Oppdater", command=self.oppdater_data, padx=10, pady=10).pack(side=tk.LEFT, padx=10)

    def oppdater_data(self):
        # Oppdaterer data ut fra filtreringen
        startår = int(self.startår.get())
        sluttår = int(self.sluttår.get())
        self.filtrert_data = self.data[(self.data["år"] >= startår) & (self.data["år"] <= sluttår)]
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
        # Lager et diagram med filtrerte data
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.lineplot(data=self.filtrert_data, x="år", y="netto folkevekst", ax=ax, label="Netto Folkevekst")
        ax.set_title("Netto Folkevekst")
        ax.set_xlabel("År")
        ax.set_ylabel("Netto Folkevekst")

        self.canvas = FigureCanvasTkAgg(fig, master=self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def oppdater_visning(self):
        # Oppdater visning

        # Slett hva som allerede vises
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

