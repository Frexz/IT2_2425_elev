import tkinter as tk
from tkinter import ttk

by_data = [["Askim", "Fredrikstad", "Halden", "Moss", "Mysen", "Sarpsborg"],
           [14259, 65415, 25300, 31855, 6513, 45852]]

# *args legges til her siden trace_add metoden sender inn 3 argumenter som vi ikke bruker
# men funksjonen må kunne ta imot disse argumentene. *args kan brukes som parameter når man ikke
# vet hvor mange argumenter som sendes inn til funksjonen.
def oppdater_tekst(*args):
    print(args)
    indeks = combobox.current() # Returnerer indeksen til den valgte byen.
    if indeks >= 0: # Sjekker om gyldig indeks er valgt
        by = by_data[0][indeks]
        innbyggere = by_data[1][indeks]
        melding = f"{by} har {innbyggere} innbyggere."
        tekst_ut.configure(text=melding)

# Hovedvindu
root = tk.Tk()
root.geometry("400x200") # Spesifiserer dimensjonene til vinduet ved start
root.title("Combobox")

# Sentrert frame - med place kan komponenter plasseres ved en spesifikk posisjon.
frame = ttk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Overskrift
overskrift = tk.Label(frame, text="Velg by:")
overskrift.grid(row=0, column=0, padx=5, pady=5)

# Combobox - Combobox (nedtrekksmeny) finnes ikke i standard tkinter så vi bruker en undermodul som heter
# ttk. Comboboxen knyttes til en strengvariabel.
valgt_by = tk.StringVar()
combobox = ttk.Combobox(frame, textvariable=valgt_by, values=by_data[0], state="readonly", width=15)
combobox.grid(row=0, column=1, padx=5, pady=5)
combobox.current(0) # Setter startvalg. 0 er første i listen.
# height velger hvor mange alternativer som vises om gangen
#combobox.configure(height=3)

# Kaller funksjonen oppdater_tekst når varabelen valgt_by endres
valgt_by.trace_add("write", oppdater_tekst)

# Utdata
tekst_ut = tk.Label(frame, text="")
tekst_ut.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()