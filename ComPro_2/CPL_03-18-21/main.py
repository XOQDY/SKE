import tkinter as tk

from gamelib import Sprite, GameApp, Text

from dir_consts import *
from maze import Maze

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

UPDATE_DELAY = 33

PACMAN_SPEED = 5


class Pacman(Sprite):
    def __init__(self, app, maze, r, c):
        self.r = r
        self.c = c
        self.maze = maze
        self.dot_eaten_observes = []

        self.direction = DIR_STILL
        self.next_direction = DIR_STILL

        x, y = maze.piece_center(r,c)
        super().__init__(app, 'images/pacman.png', x, y)

    def update(self):
        if self.maze.is_at_center(self.x, self.y):
            r, c = self.maze.xy_to_rc(self.x, self.y)

            if self.maze.has_dot_at(r, c):
                self.maze.eat_dot_at(r, c)
                for observer in self.dot_eaten_observes:
                    observer()
            
            if self.maze.is_movable_direction(r, c, self.next_direction):
                self.direction = self.next_direction
            else:
                self.direction = DIR_STILL

        self.x += PACMAN_SPEED * DIR_OFFSET[self.direction][0]
        self.y += PACMAN_SPEED * DIR_OFFSET[self.direction][1]

    def set_next_direction(self, direction):
        self.next_direction = direction


class PacmanGame(GameApp):
    def init_game(self):
        self.maze = Maze(self, CANVAS_WIDTH, CANVAS_HEIGHT)

        self.pacman1 = Pacman(self, self.maze, 1, 1)
        self.pacman2 = Pacman(self, self.maze, self.maze.get_height() - 2, self.maze.get_width() - 2)

        self.pacman1_score_text = Text(self, 'P1: 0', 100, 20)
        self.pacman2_score_text = Text(self, 'P2: 0', 600, 20)

        self.elements.append(self.pacman1)
        self.elements.append(self.pacman2)

        self.command_map = {'W': self.get_pacman_next_direction_function(self.pacman1, DIR_UP),
            # TODO:
            #   - add all other commands to the command_map
        }
        self.pacman1_score = 0
        self.pacman2_score = 0

        self.pacman1.dot_eaten_observes.append(self.dot_eaten_by_pacman1)
        self.pacman2.dot_eaten_observes.append(self.dot_eaten_by_pacman2)



    def update_scores(self):
        self.pacman1_score_text.set_text(f'P1: {self.pacman1_score}')
        self.pacman2_score_text.set_text(f'P2: {self.pacman2_score}')

    def dot_eaten_by_pacman1(self):
        self.pacman1_score += 1
        self.update_scores()

    def dot_eaten_by_pacman2(self):
        self.pacman2_score += 1
        self.update_scores()

    def pre_update(self):
        pass

    def post_update(self):
        pass

    def on_key_pressed(self, event):
        if event.char.upper() == 'A':
            self.pacman1.set_next_direction(DIR_LEFT)
        elif event.char.upper() == 'W':
            self.pacman1.set_next_direction(DIR_UP)
        elif event.char.upper() == 'S':
            self.pacman1.set_next_direction(DIR_DOWN)
        elif event.char.upper() == 'D':
            self.pacman1.set_next_direction(DIR_RIGHT)

        if event.char.upper() == 'J':
            self.pacman2.set_next_direction(DIR_LEFT)
        elif event.char.upper() == 'I':
            self.pacman2.set_next_direction(DIR_UP)
        elif event.char.upper() == 'K':
            self.pacman2.set_next_direction(DIR_DOWN)
        elif event.char.upper() == 'L':
            self.pacman2.set_next_direction(DIR_RIGHT)

        ch = event.char.upper()
        # TODO:
        #   - check if ch is in self.command_map, if it is in the map, call the function.

    def get_pacman_next_direction_function(self, pacman, next_direction):
        def f():
            pacman.set_next_direction(next_direction)
        return f


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Banana Game")
 
    # do not allow window resizing
    root.resizable(False, False)
    app = PacmanGame(root, CANVAS_WIDTH, CANVAS_HEIGHT, UPDATE_DELAY)
    app.start()
    root.mainloop()
