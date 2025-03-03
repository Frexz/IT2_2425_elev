import tkinter as tk
import pandas as pd
import platform

personer = [
    {"navn": "Knut", "alder": 32},
    {"navn": "Tiril", "alder": 28},
    {"navn": "Anne", "alder": 41},
    {"navn": "Oscar", "alder": 35},
]

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tabell med fast bredde")
        self.root.geometry("325x200")

        # Sørger for skrifttype med fast bredde på alle platformer
        if platform.system() == "Windows":
            font = ("Consolas", 18)
        elif platform.system() == "Darwin": #macOS
            font = ("Menlo", 18)
        else:
            font = ("Monospace", 18)        # Linux

        # Setter standard skrifttype for alle tkinter-widgets
        self.root.option_add("*Font", font)
        df = pd.DataFrame(personer)

        # Fjerner index-kolonnen og gjør df om til tekst
        tekst = df.to_string(index=False)
        text_widget = tk.Text(self.root, wrap="none", padx=70, pady=10)
        text_widget.insert("1.0", tekst)

        # Gjør tekstfeltet skrivebeskyttet (kan ikke forandres når programmet kjører)
        text_widget.configure(state="disabled")
        text_widget.pack(padx=10, pady=10)
    
    def run(self):
        self.root.mainloop()


if __name__=="__main__":
    app = App()
    app.run()