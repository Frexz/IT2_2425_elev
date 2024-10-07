import tkinter as tk
from tkinter import font

# Funksjonen ganger sammen verdiene i de to spinboksene, og håndterer mulige ugyldige input.
def gange():
    try:
        # Henter verdiene fra de to spinboksene, gjør dem om til tall og ganger dem sammen
        svar = float(tall_1.get()) * float(tall_2.get())
    except ValueError:
        # Hvis ugyldig input fjernes alt som er skrevet i boksene
        # i tilegg til resultatet hvis det var et resultat fra før av.
        tall_1.delete(0, tk.END)
        tall_2.delete(0, tk.END)
        resultat.configure(text="")
    else:
        # Hvis det er ingen feil så kjøres denne linjen og endrer resultat-labelen
        # til verdien av svaret med 0 desimaler.
        resultat.configure(text=f"{svar:.0f}")

# Hovedvindu
root = tk.Tk()
root.title("Spinbox")

# Henter en standard-font og endrer font-familie og størrelse
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=20)

# Spinbox for første tallet. Gyldig intervall er angitt med from og to. increment bestemmer hvor mye verdien
# øker med når man klikke på pilene.
tall_1 = tk.Spinbox(root, from_=0, to=10, increment=1, width=5, font=("Arial 20"))
tall_1.grid(row=0, column=0, padx=10, pady=10)

# Gangetegnet
gangetegn = tk.Label(root, text="*")
gangetegn.grid(row=0, column=1, padx=10, pady=10)

# Spinbox med andre tallet
tall_2 = tk.Spinbox(root, from_=0, to=10, increment=1, width=5, font=("Arial 20"))
tall_2.grid(row=0, column=2, padx=10, pady=10)

# Knapp som kaller funksjonen gange når den klikkes
button = tk.Button(root, text="=", command=gange, width=5)
button.grid(row=0, column=3, padx=10, pady=10)

# Resultatet av regnestykket vises her
resultat = tk.Label(root, width=5)
resultat.grid(row=0, column=4, padx=10, pady=10)

root.mainloop()