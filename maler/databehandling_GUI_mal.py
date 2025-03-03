import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
import platform
import tkinter.ttk as ttk
from tkinter.font import Font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App:
    def __init__(self):
        # Oppretter GUI og henter dataen
        self.gui = GUI(self)
        self.df = self.get_data()

    def get_data(self):
        # Returnerer data, gjerne fra en fil
        return pd.DataFrame({
            "Navn": ["Knut", "Tiril", "Anne", "Oscar"],
            "Alder": [32, 28, 41, 35]
        })
    
    def handle_request(self, request):
        # Behandler en forespørsel og ber GUI vise resultatet
        if request == "show_table":
            data = self.get_data().sort_values("Alder", ascending=False)
            data = data.to_string(index=False)
            data = f"Personer sortert etter alder: \n\n{data}"
            self.gui.display_table(data)
        elif request == "show_diagram":
            data = self.get_data().copy()
            self.gui.display_diagram(data, "Aldersfordeling")
    
    def run(self):
        # Start applikasjonen
        self.gui.mainloop()

class GUI(tk.Tk):
    def __init__(self, app):
        # Oppretter et GUI-vindu med kontroll- og visningsområder
        super().__init__()

        # Lagrer en referanse til app
        self.app = app

        # Tittel, dimensjoner og sentrering
        self.title("databehandling_GUI_mal.py")
        b, h = 500, 400
        bs, hs = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"{b}x{h}+{(bs // 2) - (b // 2)}+{(hs // 2) - (h // 2)}")
        self.resizable(False, False)

        # Skrifttype med lik bredde for alle platformer
        if platform.system() == "Windows":
            font = ("Consolas", 18)
        elif platform.system() == "Darwin":
            font = ("Menlo", 18)
        else:
            font = ("Monospace", 18)
        self.option_add("*Font", font)

        # Kontrollområde for valg av visning
        self.controls_frame = tk.Frame(self, relief="raised", bd=1)
        self.controls_frame.pack(side=tk.TOP, fill="x")
        self.setup_controls()

        # Visningsområde
        self.display_frame = tk.Frame(self)
        self.display_frame.pack(side=tk.RIGHT, fill="both", expand=True)
    
    def setup_controls(self):
        # Oppretter kontroller for valg av visning
        button1 = tk.Button(self.controls_frame, text="Vis Tabell", command=self.show_table_request)
        button1.grid(row=0, column=0, padx=10, pady=10)

        button2 = tk.Button(self.controls_frame, text="Vis Diagram", command=self.show_diagram_request)
        button2.grid(row=0, column=1, padx=10, pady=10)
    
    def show_table_request(self):
        # Ber app om å behandle request og deretter ber gui om å vise resultatet som tabell
        self.app.handle_request("show_table")
    
    def show_diagram_request(self):
        # ber app om å behandle request og deretter ber gui om å vise restultatet som diagram
        self.app.handle_request("show_diagram")
    
    def display_table(self, data):
        # Viser tabell i visningsområdet
        self.clear_display_frame()

        # Tekstfelt
        output = tk.Text(self.display_frame, wrap="word")
        output.pack(padx=10, pady=10, fill="both", expand=True)

        # Rullefelt
        scroll = ttk.Scrollbar(output, orient="vertical", command=output.yview)
        scroll.pack(side="right", fill="y")
        output["yscrollcommand"] = scroll.set

        # Tag for marger
        output.tag_configure("marg", lmargin1=10, lmargin2=10, rmargin=10)
        # Tag for fet skrift
        font = Font(output, output.cget("font"))
        font.config(weight="bold")
        output.tag_configure("fet", font=font)

        # Sett inn en tekst med fete kolonnenavn
        output.insert("1.0", data, "marg")
        output.tag_add("fet", "3.0", "3.end")
        output["state"] = "disabled"
    
    def display_diagram(self, data, title):
        # Vis diagram i visningsområdet
        self.clear_display_frame()

        sns.set_theme()
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        sns.barplot(data=data, x="Navn", y="Alder")
        self.ax.set_title(title)
        plt.tight_layout()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    
    def clear_display_frame(self):
        # Fjerner alle widgeter fra visningsområdet
        if hasattr(self, "canvas"):
            self.canvas.get_tk_widget().destroy()
        plt.close("all")
    
        for widget in self.display_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = App()
    app.run()