import tkinter as tk
import math
from datetime import datetime


class AnalogClock(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="brown")
        self.grid(row=0, column=0, sticky='NEWS')
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0, bg="yellow")
        self.canvas.grid(row=0, column=0, padx=10, pady=10, sticky='NEWS')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.prepare_items()
        self.canvas.bind('<Button-1>', lambda e: self.update_clock())

    def prepare_items(self):
        self.clock_face = self.canvas.create_oval(0, 0, 0, 0, width=3, outline="blue")
        self.center_pin = self.canvas.create_oval(0, 0, 0, 0, fill="green")
        self.second_hand = self.canvas.create_line(0, 0, 0, 0, fill="gray", width=1)
        self.minute_hand = self.canvas.create_line(0, 0, 0, 0, fill="black", width=4)
        self.hour_hand = self.canvas.create_line(0, 0, 0, 0, fill="black", width=8)

    def center_coords(self):
        '''
        Return a tuple (x,y) representing the current center coordinates of the canvas
        '''
        return self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2

    def clock_radius(self):
        '''
        Return the desired clock's radius, which is set to be 90% of the canvas's shorter side
        '''
        cx, cy = self.center_coords()
        return min(cx, cy) * 0.9

    def update_clock(self):
        cx, cy = self.center_coords()
        radius = self.clock_radius()

        # update the item self.clock_face so that it has the radius of self.clock_radius()
        # and is centered at coordinates (cx,cy)
        self.canvas.coords(self.clock_face, cx - radius, cy - radius, cx + radius, cy + radius)

        # update the item self.center_pin so that it has the radius of 5 pixels and
        # is centered at coordinates (cx,cy)
        self.canvas.coords(self.center_pin, cx - 5, cy - 5, cx + 5, cy + 5)
        now = datetime.now()
        sec_angle = now.second/60*360
        minute_angle = (now.minute/60*360) + (now.second/3600*360)
        hour_angle = (now.hour/12*360) + (now.minute/720*360) + (now.second/43200*360)
        sx, sy = self.polar_to_canvas(radius * 0.9, sec_angle)
        mx, my = self.polar_to_canvas(radius * 0.75, minute_angle)
        hx, hy = self.polar_to_canvas(radius * 0.5, hour_angle)
        self.canvas.coords(self.second_hand, cx, cy, sx, sy)
        self.canvas.coords(self.minute_hand, cx, cy, mx, my)
        self.canvas.coords(self.hour_hand, cx, cy, hx, hy)
        self.after(1000, self.update_clock)

    def polar_to_canvas(self, radius, theta):
        '''
        Take polar coordinates (radius,theta) and return a tuple (x,y)
        representing the Cartesian coordinates on the canvas, with respect to
        the canvas's center.
        '''
        cx, cy = self.center_coords()
        x = cx + (radius * math.sin(math.radians(theta)))
        y = cy + -(radius * math.cos(math.radians(theta)))
        return x, y


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    root.title("Analog Clock")
    clock = AnalogClock(root)
    root.mainloop()
