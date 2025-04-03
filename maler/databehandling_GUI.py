import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns

class App:
    def __init__(self):
        # Data
        self.data = self.hent_data("tips")

        # Root
        self.root = tk.Tk()
        self.root.title("Databehandling GUI")
        self.root.geometry("800x600")
        self.root.protocol("WM_DELETE_WINDOW", self.ved_avslutning) # Sørger for korrekt avslutning

        # Lager mulighet for å bytte mellom tabell og diagram
        self.lag_visning()

        # Frame for innhold
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.canvas = None
        self.oppdater_visning()

    def hent_data(self, filnavn):
        # Laster inn og renser data fra fil - Må tilpasses hver enkelt problemstilling
        df = sns.load_dataset(filnavn)
        df = df.groupby("day")["tip"].mean().round(2).reset_index()
        df.columns = ["Weekday", "Average Tip"]
        return pd.DataFrame(df)

    def lag_visning(self):
        # Lager en ramme med radioknapper som kan kontrollere visning
        self.visning_frame = tk.Frame(self.root)
        self.visning_frame.pack(anchor=tk.N, pady=10)

        self.visning = tk.StringVar(value="tabell")
        tk.Radiobutton(self.visning_frame, text="Tabell", variable=self.visning, value="tabell", command=self.oppdater_visning).pack(side=tk.LEFT, anchor=tk.N)
        tk.Radiobutton(self.visning_frame, text="Diagram", variable=self.visning, value="diagram", command=self.oppdater_visning).pack(side=tk.LEFT, anchor=tk.N)

    def lag_tabell(self):
        # Lager en tabell med filtrerte data
        tree = ttk.Treeview(self.frame, columns=list(self.data.columns), show="headings", height=10)

        for col in self.data.columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.CENTER)

        for _, row in self.data.iterrows():
            tree.insert("", tk.END, values=list(row))

        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def lag_diagram(self):
        # Lager et diagram - Må tilpasses hvert enkelt datasett
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.barplot(data=self.data, x="Weekday", y="Average Tip", ax=ax, label="Average Tip per Weekday", palette="viridis")
        ax.set_title("Average Tip per Weekday")
        ax.set_xlabel("Weekday")
        ax.set_ylabel("Average Tip")

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

