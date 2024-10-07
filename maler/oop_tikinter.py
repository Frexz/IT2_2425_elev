import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Enkel OOP-mal for tkinter")
        self.root.geometry("300x200")

        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.button = tk.Button(self.frame, text="Trykk meg!", command=self.on_click)
        self.button.pack(pady=10)

        self.label = tk.Label(self.frame, text="Antall trykk: 0")
        self.label.pack()
        
        self.teller = 0
    
    def on_click(self):
        self.teller += 1
        self.label.configure(text=f"Antall trykk: {self.teller}")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()