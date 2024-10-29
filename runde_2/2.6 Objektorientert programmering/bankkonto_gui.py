import tkinter as tk
from tkinter import font
import sys


class Bankkonto():
    def __init__(self, eier):
        self.eier = eier
        self.saldo = 0
    
    def sett_inn(self, beløp):
        self.saldo += beløp
        return ""
    
    def ta_ut(self, beløp):
        if beløp <= self.saldo:
            self.saldo -= beløp
            return ""
        else:
            return f"Du kan ikke ta ut mer enn {self.saldo} kr."
    
    def __str__(self):
        return f"Eier: \t{self.eier}\nSaldo: \t{self.saldo} kr"

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bankkonto")
        self.root.geometry("600x300")

        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(family="Arial", size=12)

        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.konto = Bankkonto("Fredrik Pettersen")
        self.melding = ""

        self.status = tk.Label(self.frame, text=str(self.konto), justify="left", width=30, anchor="w")
        self.status.pack(pady=20)

        self.beskjed = tk.Label(self.frame, text="Skriv inn et beløp: ", width=30, anchor="w")
        self.beskjed.pack()

        self.spinbox = tk.Spinbox(self.frame, from_=0, to=sys.maxsize, width=42)
        self.spinbox.pack()

        self.button_frame = tk.Frame(self.frame)
        self.button_frame.pack(pady=20)

        self.button_inn = tk.Button(self.button_frame, text="Sett inn", width=12, command=self.håndter_sett_inn)
        self.button_inn.grid(row=0, column=0, padx=10)

        self.button_ut = tk.Button(self.button_frame, text="Ta ut", width=12, command=self.håndter_ta_ut)
        self.button_ut.grid(row=0, column=1, padx=10)

        self.tilbakemelding = tk.Label(self.frame, text=self.melding, width=30, fg="red")
        self.tilbakemelding.pack()

    
    def run(self):
        self.root.mainloop()

    def håndter_sett_inn(self):
        self.melding = self.konto.sett_inn(float(self.spinbox.get()))
        self.status.configure(text=str(self.konto))
        self.tilbakemelding.configure(text=self.melding)

    def håndter_ta_ut(self):
        self.melding = self.konto.ta_ut(float(self.spinbox.get()))
        self.status.configure(text=str(self.konto))
        self.tilbakemelding.configure(text=self.melding)

if __name__ == "__main__":
    app = App()
    app.run()