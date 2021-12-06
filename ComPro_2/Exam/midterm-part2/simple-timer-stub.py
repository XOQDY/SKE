import tkinter as tk
from tkinter import ttk

class SimpleTimer(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.str_remaining = tk.StringVar()
        self.str_remaining.set("0 second(s)")
        self.time_remaining = 0
        self.is_countdown = False
        self.create_widgets()

    def create_widgets(self):
        self.style = ttk.Style()
        self.style.configure("Remain.TLabel", font=("Arial", 24))
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky="news")
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)

        self.btn_minus = ttk.Button(self.mainframe, text="-", command=self.minus_time)
        self.btn_plus = ttk.Button(self.mainframe, text="+", command=self.plus_time)
        self.btn_start = ttk.Button(self.mainframe, text="Start", command=self.toggle_start)
        self.lbl_remain = ttk.Label(self.mainframe, style="Remain.TLabel",
                textvariable=self.str_remaining, padding="10 10 10 10")

        self.lbl_remain.grid(row=0, column=0, columnspan=3)
        self.btn_minus.grid(row=1, column=0)
        self.btn_start.grid(row=1, column=1)
        self.btn_plus.grid(row=1, column=2)

    def plus_time(self):
        self.time_remaining += 1
        self.str_remaining.set(f"{self.time_remaining} second(s)")

    def minus_time(self):
        if self.time_remaining > 0:
            self.time_remaining -= 1
        self.str_remaining.set(f"{self.time_remaining} second(s)")

    def toggle_start(self):
        self.is_countdown = not self.is_countdown
        if self.is_countdown:
            self.btn_start.config(text="Stop")
            self.btn_plus.config(state="disabled")
            self.btn_minus.config(state="disabled")
            self.after(1000, self.start)
        else:
            self.btn_start.config(text="Start")
            self.btn_plus.config(state="enabled")
            self.btn_minus.config(state="enabled")

    def start(self):
        if self.is_countdown:
            timer = self.after(1000, self.start)
            if self.time_remaining == 0:
                self.str_remaining.set("Time's up!")
                self.btn_plus.config(state="enabled")
                self.btn_minus.config(state="enabled")
                self.after_cancel(timer)
            else:
                self.time_remaining -= 1
                self.str_remaining.set(f"{self.time_remaining} second(s)")
                if self.time_remaining == 0:
                    self.str_remaining.set("Time's up!")
                    self.btn_plus.config(state="enabled")
                    self.btn_minus.config(state="enabled")
                    self.after_cancel(timer)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simple Timer")
    app = SimpleTimer(root)
    root.mainloop()

