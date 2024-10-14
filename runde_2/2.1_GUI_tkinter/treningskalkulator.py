import tkinter as tk
from tkinter import ttk

def kaloriforbruk():
    if valgt_aktivitet.get() == "" and valgt_intentistet.get() == " ":
        label3.configure(text="Du må velge aktivitet, \nintensitet og varighet først.")
        return
    
    antall_timer = int(spinbox.get()) / 60
    kalorier = aktiviteter[valgt_aktivitet.get()] * intensiteter[valgt_intentistet.get()] * antall_timer
    label3.configure(text=f"Du vil forbrenne {kalorier:.0f} kalorier.")

root = tk.Tk()
root.title("Treningskalkulator")
root.geometry("400x400")

aktiviteter = {
    "Aerobic": 814,
    "Bordtennis": 236,
    "Fotball": 510,
    "Golf": 244,
    "Jogging": 666
}

valgt_aktivitet = tk.StringVar()
combobox = ttk.Combobox(root, textvariable=valgt_aktivitet, values=list(aktiviteter.keys()), width=25)
combobox.pack(pady=15)

label1 = tk.Label(root, text="Velg intensitet: ", width=25, anchor="w")
label1.pack()

intensiteter = {
    "Lavt": 0.8,
    "Middels": 1,
    "Høyt": 1.2
}

valgt_intentistet = tk.StringVar(value=" ")
for intensitet in intensiteter.keys():
    radio = tk.Radiobutton(root, text=intensitet, variable=valgt_intentistet, value=intensitet, width=25, anchor="w")
    radio.pack(pady=5)

label2 = tk.Label(root, text="Oppgi varighet i antall minutter: ", width=25, anchor="w")
label2.pack(pady=5)

spinbox = tk.Spinbox(root, from_=0, to=24*60, increment=1, width=25)
spinbox.pack()

button = tk.Button(root, text="Beregn kaloriforbruk", command=kaloriforbruk, width=15, padx=10, pady=10)
button.pack(pady=15)

label3 = tk.Label(root, text="", width=25, justify='center')
label3.pack()

root.mainloop()