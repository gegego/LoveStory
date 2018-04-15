import curses
from random import randint
import math
from controller import Controller

class Engine:
    def __init__(self, width, height):
        self.ptrcur = curses.initscr()
        self.window = curses.newwin(height, width, 1, 1)
        self.window.timeout(100)
        self.window.keypad(1)
        self.window.border('*','*',' ','*','*','*','*','*')
        curses.noecho()
        curses.curs_set(0)
        self.controller = Controller(height-1, width-2)

    def destroy(self):
        curses.nocbreak()
        self.ptrcur.keypad(0)
        curses.echo()
        curses.endwin()
        curses.curs_set(1)

    def render(self):
        self.window.erase()
        self.window.border('*','*',' ','*','*','*','*','*')
        status = self.controller.get_current_status()
        for y, row in enumerate(status):
            for x, cel in enumerate(row):
                if cel > 0:
                    try:
                        self.window.move(y, x+1)
                        self.window.echochar('*')
                    except:
                        self.window.refresh()

    def _initGame(self):
        self.controller.initGame()
        pass

    def run(self):
        exiting = False
        self._initGame()
        self.render()
        valid =False
        while not exiting:
            if(self.controller.is_gameover()):
                exiting = True

            if(valid == True):
                valid = self.controller.move_figure_down()
                if(valid):
                    self.render()
                    valid =False

            ch = self.window.getch()
            if ch == ord("q") or ch == ord("Q"):
                exiting = True
            if ch == ord("d") or ch == ord("D"):
                valid = self.controller.move_figure_right()
            if ch == ord("a") or ch == ord("a"):
                valid = self.controller.move_figure_left()
            if ch == ord("s") or ch == ord("S"):
                # valid = self.controller.rotate_figure_anticlockwise()
                valid = True    # rotate piece counter clockwise, what is counter?
            if ch == ord("w") or ch == ord("W"):
                valid = self.controller.rotate_figure_clockwise()
