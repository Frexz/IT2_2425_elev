import tkinter as tk
from tkinter import font

def vis_valgt_by(_):
    # Gir valgt by sin indeks
    indeks = listbox.curselection()[0]
    valgt_by = by_data[0][indeks]
    innbyggere = by_data[1][indeks]
    melding = f"{valgt_by} har {innbyggere} innbyggere."
    tekst_ut.configure(text=melding)

root = tk.Tk()
root.geometry("400x200")
root.title("Listbox")

default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=15)

by_data = [["Askim", "Fredrikstad", "Halden", "Moss", "Mysen", "Sarpsborg"],
           [14259, 65415, 25300, 31855, 6513, 45852]]

ramme = tk.Frame(root)
ramme.pack(pady=25)

scrollbar = tk.Scrollbar(ramme, orient="vertical")
scrollbar.pack(side="right", fill="y")

# yscrollcommand = kobler til Scrollbal, selectmode = kun ett alternativ kan velges om gangen
listbox = tk.Listbox(ramme, height=3, width=10, yscrollcommand=scrollbar.set, selectmode="single")
for by in by_data[0]:
    listbox.insert(tk.END, by)
listbox.pack()

# kobler scrollbar til listbox
scrollbar.configure(command=listbox.yview)

# Når hendelser "ListboxSelect" skjer, kalles funksjonen vis_valgt_by. Hendelsen er når en by blir valgt
listbox.bind("<<ListboxSelect>>", vis_valgt_by)

tekst_ut = tk.Label(root, text="")
tekst_ut.pack(pady=10)

root.mainloop()