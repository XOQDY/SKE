import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Clock")
        self.geometry("450x150")
        self.style = ttk.Style()
        self.style.configure(".", font=("Arial", 24))
        self.str_date = tk.StringVar()
        self.str_time = tk.StringVar()
        self.label1 = ttk.Label(self, textvariable=self.str_date)
        self.label1.pack()
        self.label2 = ttk.Label(self, textvariable=self.str_time)
        self.label2.pack()
        self.btnQuit = tk.Button(self, text="Quit", command=self.destroy)
        self.btnQuit.pack()
        self.update_time()

    def update_time(self):
        self.str_date.set(datetime.now().strftime("%d %B %Y"))
        self.str_time.set(datetime.now().strftime("%H:%M:%S"))
        self.after(1000, self.update_time)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
