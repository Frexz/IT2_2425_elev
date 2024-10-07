import tkinter as tk
from tkinter import font

def print_level():
    total = sum([x.get() for x in variables])

    if total > 2:
        resultat.configure(text="Du er en mester!")
    elif total > 0:
        resultat.configure(text="Du kan litt!")
    else:
        resultat.configure(text="Du har aldri programmert!")
    

# Hovedvindu
root = tk.Tk()
root.title("Avkrysningsbokser")

# Standard-font
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=15)

# Overskrift-label
overskrift = tk.Label(text="Velg programmeringsspråkene du kan.", padx=5, pady=5)
overskrift.pack()

languages = ["Python", "JavaScript", "Java", "C#", "Andre"]
variables = []
checkboxes = []

# Hver avkrysningsboks må ha en egen variabel knyttet til seg.
# Variabelen har verdien 1 hvis avkrysset og 0 hvis ikke.
for lang in languages:
    var = tk.IntVar()
    check = tk.Checkbutton(root, text=lang, variable=var, onvalue=1, offvalue=0, command=print_level, width=10, anchor="w")
    check.pack()
    variables.append(var)
    checkboxes.append(check)

# Viser resultatet
resultat = tk.Label(text="", padx=5, pady=5)
resultat.pack()


root.mainloop()