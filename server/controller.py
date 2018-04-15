from block import Block
from figure import Figure1,Figure2,Figure3,Figure4,Figure5
import math
import random

class Controller:
    def __init__(self, height, width):
        self.block = Block(height, width)
        self.status = [[0 for i in range(0, width)] for i in range(0, height)]
        self.figures = []
        self.figures.append(Figure1())
        self.figures.append(Figure2())
        self.figures.append(Figure3())
        self.figures.append(Figure4())
        self.figures.append(Figure5())
        random.seed()
        self.figidx,self.figure = self._generate_figure()

    def _generate_figure(self):
        idx = random.randint(0, len(self.figures) - 1)
        fig = self.figures[idx]
        fig.y = 0
        fig.x = math.floor((self.block.width/2)-2)
        return idx,fig

    def get_current_status(self):
        return self.status

    def recoverGame(self, block, figure):
        # print(figure)
        self.figidx = figure['idx']
        self.figure = self.figures[self.figidx]
        self.figure.y = figure['y']
        self.figure.x = figure['x']
        self.figure.current_sprite_index = figure['cidx']
        self.block.lees = block
        valid,self.status = self.figure.draw(self.block,self.status)

    def initGame(self):
        self.figidx,self.figure = self._generate_figure()
        valid,self.status = self.figure.draw(self.block,self.status)

    def is_gameover(self):
        return self.block.is_full()

    def move_figure_down(self):
        self.figure.y += 1
        valid, self.status = self.figure.draw(self.block, self.status)
        if(valid==False):   #rollback and add figure to lees
            self.figure.y -= 1
            self.block.lees_figure(self.figure)
            self.block.delete_full_lines()
            self.figidx,self.figure = self._generate_figure()
            return False
        else:
            return True

    def move_figure_right(self):
        self.figure.x += 1
        valid, self.status = self.figure.draw(self.block, self.status)
        if(valid==False): #rollback
            self.figure.x -= 1
            return False
        else:
            return True

    def move_figure_left(self):
        self.figure.x -= 1
        valid, self.status = self.figure.draw(self.block, self.status)
        if(valid==False):   #rollback
            self.figure.x += 1
            return False
        else:
            return True

    def rotate_figure_anticlockwise(self):
        self.figure.rotate_anticlockwise()
        valid, self.status = self.figure.draw(self.block, self.status)
        if(valid==False):   #rollback
            self.figure.rotate_clockwise()
            return False
        else:
            return True

    def rotate_figure_clockwise(self):
        self.figure.rotate_clockwise()
        valid, self.status = self.figure.draw(self.block, self.status)
        if(valid==False):   #rollback
            self.figure.rotate_anticlockwise()
            return False
        else:
            return True
