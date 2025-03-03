import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

df = pd.DataFrame({
    "Navn": ["Knut", "Tiril", "Anne", "Oscar"],
    "Alder": [32, 28, 41, 35]
})

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("diagramvisning.py")
        self.geometry("800x600")
        self.resizable(False, False)

        sns.set_theme()
        self.fig, self.ax = plt.subplots(figsize=(9, 6))
        sns.barplot(data=df, x="Navn", y="Alder")
        self.fig.suptitle("Seaborn-diagram i tkinter-vindu", fontsize=20)
        self.ax.set_title("Aldersfordeling")
        plt.tight_layout()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def run(self):
        self.mainloop()
    
    def destroy(self):
        plt.close("all")
        super().destroy()

if __name__ == "__main__":
    app = App()
    app.run()