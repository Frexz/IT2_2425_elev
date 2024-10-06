import tkinter as tk

# Funksjonen kjøres når knappen klikkes.
def skriv_ut():
    # I utgangspunkten er Label()-komponenten tom. configure-metoden lar oss endre
    # komponenten, blant annet teksten som vises med parameteren text. Entry()-komponenten
    # har også en metoden som heter get() som brukes for å hente verdien som er skrevet
    # i tekstfeltet.
    hilsen.configure(text=f"Hallo {navn.get()}")

# Tk() er root-komponenten, eller hovedvinduet. Dette hovedvinduet kan lytte til blant annnet
# klikk og tastetrykk
root = tk.Tk()

# Entry()-komponenten er et input-felt som brukeren kan skrive informasjon inn i.
# Her settes det en standard-tekst med metoden insert() og festes til root-komponenten med pack()
navn = tk.Entry(root)
navn.insert(0, "Hva heter du?")
navn.pack()

# Button()-komponenten er en knapp som kan klikkes. Parameteren text angir tekst på knappen
# mens parameteren command tar en funksjon som kalles når knappen klikkes.
button = tk.Button(root, text="Les navn", command=skriv_ut)
button.pack()

# Label() er en komponent som kan vise frem tekst. root angis her som forelder-komponent
# altså, komponenten Label eksisterer inni. Metoden pack() "fester" Label til root-komponenten.
hilsen = tk.Label(root)
hilsen.pack()

# Metoden mainloop() er en funksjon som setter i gang og opprettholder vinduet så lenge det ikke blir lukke ved å
# klikke på krysset. I et GUI-rpogram kalles denne metoden helt til slutt etter alle komponenter er opprettet
# og lagt til hovedvinduet.
root.mainloop()