import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk

personer = [
    {'fornavn': 'Kari', 'etternavn': 'Hansen', 'fødselsår': 2001},
    {'fornavn': 'Gustav', 'etternavn': 'Monsen', 'fødselsår': 1995},
    {'fornavn': 'Anette', 'etternavn': 'Ås', 'fødselsår': 1998},
    {'fornavn': 'Marius', 'etternavn': 'Lie', 'fødselsår': 2002},
    {'fornavn': 'Wenche', 'etternavn': 'Hovland', 'fødselsår': 1999},
]

def sorter():
    pass

df = pd.DataFrame(personer)

root = tk.Tk()
root.title("Persontabell med sortering")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack()


sorteringsvalg = tk.Entry(root)
sorteringsvalg.pack()

button = tk.Button(root, text="Sorter", command=sorter)
button.pack()

root.mainloop()