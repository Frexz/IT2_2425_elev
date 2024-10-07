import tkinter as tk
from tkinter import font

def velg_farge():
    i = farge_var.get()
    if i != -1:
        valg.configure(text=farger[i], fg="white", bg=farger[i])

# Hovedvindu
root = tk.Tk()
root.title("Radioknapper")

# Standard-font
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=15)

farger = ["red", "blue", "green"] # Mulige fargevalg
farge_var = tk.IntVar(value=-1)   # Variabel som knyttes til valgt radioknapp. value=-1 betyr at ingen er valgt.

# Overskrift
overskrift = tk.Label(root, text="Velg farge:", bg="darkgrey", width=20, padx=5, pady=5)
overskrift.grid(row=0, column=0, padx=5, pady=5)

# enumerate gir både indeks og verdien til elementet. Dermed kan man gå gjennom en liste og både ha verdien
# og indeksen til elementet.
# variable = variabelen knappen knyttes til, value = en unik verdi til knappen (her indeksen), command = funksjon som 
# kalles når knappen velges, anchor = gjør at alle valgene er linet opp under hverandre, der "w" betyr west (eller venstre)
for i, farge in enumerate(farger):
    radio = tk.Radiobutton(root, text=farge, variable=farge_var, value=i, command=velg_farge, width=10, anchor="w")
    radio.grid(row=i + 1, column=0)

valg = tk.Label(root, text="")
# sticky = komponenten klistrer seg til angitte kanter av cellen i grid-layouten, eller med andre ord, komponenten
# fyller hele cellen når alle retninger er oppgitt
valg.grid(row=4, column=0, padx=5, pady=5, sticky="NSEW")

root.mainloop()