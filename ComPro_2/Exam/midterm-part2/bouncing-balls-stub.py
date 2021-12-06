import time
import tkinter as tk
from threading import Thread


class BouncingBalls(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill="both", expand=True)
        self.yellow_ball = Thread(target=self.animate_yellow_ball)
        self.yellow_ball.start()
        self.red_ball = Thread(target=self.animate_red_ball)
        self.red_ball.start()

    def animate_yellow_ball(self):
        x = 0
        ball = self.canvas.create_oval(x, 100, x+50, 150, fill="yellow")
        while True:
            while x < 450:
                self.canvas.coords(ball, x, 100, 50+x, 150)
                x += 5
                time.sleep(0.02)

            while x > 0:
                self.canvas.coords(ball, x, 100, 50+x, 150)
                x -= 5
                time.sleep(0.02)

    def animate_red_ball(self):
        y = 0
        ball = self.canvas.create_oval(300, y, 350, y+50, fill="red")
        while True:
            while y < 350:
                self.canvas.coords(ball, 300, y, 350, y+50)
                y += 3
                time.sleep(0.02)

            while y > 0:
                self.canvas.coords(ball, 300, y, 350, y+50)
                y -= 3
                time.sleep(0.02)

    def update_screen(self):
        self.update()
        self.after(50, self.update_screen)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bouncing Balls")
    root.geometry("500x400")
    root.resizable(False, False)
    app = BouncingBalls(root)
    root.mainloop()

