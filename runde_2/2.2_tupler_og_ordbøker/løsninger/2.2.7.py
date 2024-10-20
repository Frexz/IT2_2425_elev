import tkinter as tk

def fibonacci(n):
    f0 = 0
    f1 = 1
    f2 = f0 + f1
    fib = [f1]

    while f2 < n:
        fib.append(f2)
        f0, f1 = f1, f2
        f2 = f0 + f1
    
    return fib

root = tk.Tk()
root.title("Fibonacci")
root.geometry("400x400")
root.config(bg="#5083a1")

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")
tittel = tk.Label(frame, text="Fibonaccitallene under 10 000", padx=10, pady=5, bg="#3d93c4", bd=1, relief="solid", width=40)
tittel.grid(row=0, column=0, columnspan=5, sticky="NSEW")

for i, f in enumerate(fibonacci(10000)):
    label = tk.Label(frame, text=f"{f}", padx=10, pady=5, bd=1, relief="solid", bg="#71b6de")
    label.grid(row=(i // 5) + 1, column=i % 5, sticky="NSEW")

root.mainloop()
