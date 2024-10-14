import tkinter as tk
import random

def produce_stat():
    dice_rolls = [random.randint(1, 6) for x in range(4)]
    dice_rolls.sort(reverse=True)
    return sum(dice_rolls[:3])

def roll_stats():
    for box in statboxes:
        resultat = produce_stat()
        box.configure(text=resultat)

root = tk.Tk()

statboxes = []
for i in range(6):
    stat = tk.Label(root, text='-', width=10, height=5)
    stat.grid(row=0, column=i)
    statboxes.append(stat)


button = tk.Button(root, text="Roll stats", command=roll_stats, width=25)
button.grid(row=1, column=2, columnspan=2, pady=10)

root.mainloop()