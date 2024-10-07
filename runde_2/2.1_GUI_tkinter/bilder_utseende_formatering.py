""" I denne filen brukes grid() i stedet for pack() som layout. Med en grid-layout må man spesifisere
row og column for å plassere en komponent."""
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

def skriv_ut():
    hilsen.configure(text=f"Hallo {navn.get()}!")

root = tk.Tk()

# Endrer standard-skrift, gjelder ikke for Entry()-komponenten
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=20)

# Endrer tekst på tittellinjen
root.title("Inndata/Utdata")

# Legg til et bilde, krever import av Image og ImageTk fra PIL-modulen
# Dette kan kreve å kjøre "pip install pillow", eller "pip install --upgrade pillow" fra terminalen.

bilde = Image.open("img/tkinter.jpg")   # Relativ sti til bilde
bilde = bilde.resize((150, 150), Image.Resampling.LANCZOS) # Oppgi bildets størrelse som (bredde, høyde)
bilde = ImageTk.PhotoImage(bilde)
# padx = horisontal padding, pady = vertikal padding
tk.Label(root, image=bilde).grid(row=0, column=0, padx=5, pady=5)

# Lag en ramme for høyre del. En Frame() kan inneholde andre komponenter.
frame = tk.Frame(root, padx=10, pady=10)
frame.grid(row=0, column=1, padx=5, pady=15)

navn = tk.Entry(frame, width=15, font=("Arial 20"))
navn.insert(0, "Hva heter du?")
navn.grid(row=0, column=0, padx=5, pady=13)

tk.Button(frame, text="Les navn", command=skriv_ut, width=10) \
    .grid(row=0, column=1, padx=5)

# fg = Foreground color, bg = Background color
hilsen = tk.Label(frame, width=25, bg="#3877ac", fg="white", pady=3)
hilsen.grid(row=1, column=0, columnspan=2, pady=13)

root.mainloop()