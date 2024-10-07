import tkinter as tk
import random

def kast_terninger():
    for t in terninger:
        resultat = random.randint(1, 6)
        t.configure(text=resultat)

root = tk.Tk()

terninger = []
for i in range(4):
    terning = tk.Label(root, text='-', width=10, height=5)
    terning.grid(row=0, column=i)
    terninger.append(terning)


button = tk.Button(root, text="Kast terning", command=kast_terninger, width=25)
button.grid(row=1, column=1, columnspan=2)

root.mainloop()