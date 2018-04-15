from random import randint
import math
from controller import Controller

class Engine_Print:
    def __init__(self, width, height):
        self.controller = Controller(height-1, width-2)

    def destroy(self):
        pass

    def render(self):
        status = self.controller.get_current_status()
        for i in range(0,20):
            print('')
            for j in range(0,20):
                if( i==19 or j==0 or j==19):
                    print('*',end='')
                elif(status[i][j-1] > 0):
                    print('*',end='')
                else:
                    print(' ',end='')

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
            print('')
            ch = input("input: w,s(rotate),a(left),d(right),q(quit),other(down):  ")
            if ch == "q":
                exiting = True
            elif ch == "d":
                valid = self.controller.move_figure_right()
            elif ch == "a":
                valid = self.controller.move_figure_left()
            elif ch == "s":
                valid = self.controller.rotate_figure_anticlockwise()
                # valid = True    # rotate piece counter clockwise, what is counter?
            elif ch == "w":
                valid = self.controller.rotate_figure_clockwise()
            else:
                valid = True
