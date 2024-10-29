import tkinter as tk

class Bankkonto():
    def __init__(self, navn: str):
        self.eier = navn
        self.saldo = 0
    
    def sett_inn(self, beløp):
        self.saldo += beløp
        return f"Du har satt inn {beløp:.2f} kr."
    
    def ta_ut(self, beløp):
        if beløp > self.saldo:
            return "Du kan ikke ta ut mer enn du har på konto."
        else:
            self.saldo -= beløp
            return f"Du har tatt ut {beløp:.2f} kr."

    def __str__(self):
        return f"Eier: \t{self.eier}\nSaldo: \t{self.saldo:.2f} kr"

def håndter_inn():
    beløp_inn = float(beløp.get())
    melding = konto.sett_inn(beløp_inn)
    tilbakemelding.configure(text=melding, fg="black")
    info.configure(text=str(konto))
    beløp.delete(0, tk.END)

def håndter_ut():
    beløp_ut = float(beløp.get())
    melding = konto.ta_ut(beløp_ut)
    if melding.startswith("Du kan ikke"):
        tilbakemelding.configure(text=melding, fg="red")
    else:
        tilbakemelding.configure(text=melding, fg="black")
    tilbakemelding.configure(text=melding)
    info.configure(text=str(konto))
    beløp.delete(0, tk.END)

konto = Bankkonto("Fredrik Pettersen")
root = tk.Tk()
root.title("Bankkonto")
root.geometry("600x300")

info = tk.Label(root, text=str(konto), justify="left", padx=5, pady=5)
info.pack(padx=20, pady=20)

l1 = tk.Label(root, text="Skriv inn et beløp:", padx=5, pady=5, width=30, anchor="w")
l1.pack()

beløp = tk.Spinbox(root, from_=0, to=100000, width=30)
beløp.pack(padx=20)

button_frame = tk.Frame(root, padx=20, pady=20)
button_frame.pack()

ut = tk.Button(button_frame, text="Ta ut", command=håndter_ut, padx=5, pady=5, width=20)
ut.grid(row=0, column=1, padx=5, pady=5)

inn = tk.Button(button_frame, text="Sett inn", command=håndter_inn, padx=5, pady=5, width=20)
inn.grid(row=0, column=0, padx=5, pady=5)

tilbakemelding = tk.Label(root, text="", padx=20, pady=20)
tilbakemelding.pack()





root.mainloop()

