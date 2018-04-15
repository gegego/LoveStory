import math
import copy

class Figure:

    def __init__(self, y=0, x=0):
        self.current_sprite_index = 0
        self.y = y
        self.x = x

    def _is_window_point(self, width, height, y, x):
        if x < 0 or x > width \
           or y < 0 or y > height:
            return False
        else:
            return True

    def draw(self, block, oldstatus):
        current_sprite = self.sprites[self.current_sprite_index]
        status = copy.deepcopy(block.lees)
        x = self.x
        y = self.y
        for r, row in enumerate(current_sprite):
            for c, cell in enumerate(row):
                if cell > 0:
                    xx = int(x + c)
                    yy = int(y + r)
                    # print(xx,yy)
                    if self._is_window_point(block.width, block.height, yy, xx):
                        try:
                            if(status[yy][xx] == 1):
                                return False,oldstatus
                            else:
                                status[yy][xx]=1
                        except Exception:
                            return False,oldstatus
                    else:
                        return False,oldstatus

        return True,status

    def rotate_clockwise(self):
        self.current_sprite_index = self.get_next_sprite_index()

    def rotate_anticlockwise(self):
        self.current_sprite_index = self.get_prev_sprite_index()

    def get_next_sprite_index(self, current_index=None):
        if current_index == None:
            current_index = self.current_sprite_index

        current_index += 1
        current_index %= 4
        return current_index

    def get_prev_sprite_index(self, current_index=None):
        if current_index == None:
            current_index = self.current_sprite_index

        current_index -= 1
        if current_index < 0:
            current_index = 3

        return current_index

    def get_sprite(self, sprite_index=None):
        if sprite_index == None:
            sprite_index = self.current_sprite_index

        return self.sprites[sprite_index]

class Figure1(Figure):
    sprites = (
        ((0, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),
         (0, 0, 2, 0, 0),
         (0, 0, 1, 0, 0),
         (0, 0, 1, 0, 0)),

        ((0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0),
         (1, 1, 2, 1, 0),
         (0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0)),

        ((0, 0, 1, 0, 0),
         (0, 0, 1, 0, 0),
         (0, 0, 2, 0, 0),
         (0, 0, 1, 0, 0),
         (0, 0, 0, 0, 0)),

        ((0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0),
         (0, 1, 2, 1, 1),
         (0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0)),
    )
    def __init__(self, y=0, x=0):
        Figure.__init__(self, y, x)

class Figure2(Figure):
    sprites = (
        ((0, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),
         (0, 0, 2, 0, 0),
         (0, 1, 1, 0, 0),
         (0, 0, 0, 0, 0)),

        ((0, 0, 0, 0, 0),
         (0, 1, 0, 0, 0),
         (0, 1, 2, 1, 0),
         (0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0)),

        ((0, 0, 0, 0, 0),
         (0, 0, 1, 1, 0),
         (0, 0, 2, 0, 0),
         (0, 0, 1, 0, 0),
         (0, 0, 0, 0, 0)),

        ((0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0),
         (0, 1, 2, 1, 0),
         (0, 0, 0, 1, 0),
         (0, 0, 0, 0, 0)),
    )
    def __init__(self, y=0, x=0):
        Figure.__init__(self, y, x)

class Figure3(Figure):
    sprites = (
        ((0, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),
         (0, 0, 2, 0, 0),
         (0, 0, 1, 1, 0),
         (0, 0, 0, 0, 0)),

        ((0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0),
         (0, 1, 2, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 0, 0, 0)),

        ((0, 0, 0, 0, 0),
         (0, 1, 1, 0, 0),
         (0, 0, 2, 0, 0),
         (0, 0, 1, 0, 0),
         (0, 0, 0, 0, 0)),

        ((0, 0, 0, 0, 0),
         (0, 0, 0, 1, 0),
         (0, 1, 2, 1, 0),
         (0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0)),
    )
    def __init__(self, y=0, x=0):
        Figure.__init__(self, y, x)

class Figure4(Figure):
    sprites = (
        ((0, 0, 0, 0, 0),
         (0, 1, 1, 0, 0),
         (0, 0, 2, 1, 0),
         (0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0)),

        ((0, 0, 0, 0, 0),
         (0, 0, 0, 1, 0),
         (0, 0, 2, 1, 0),
         (0, 0, 1, 0, 0),
         (0, 0, 0, 0, 0)),

        ((0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0),
         (0, 1, 2, 0, 0),
         (0, 0, 1, 1, 0),
         (0, 0, 0, 0, 0)),

        ((0, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),
         (0, 1, 2, 0, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 0, 0, 0)),
    )
    def __init__(self, y=0, x=0):
        Figure.__init__(self, y, x)

class Figure5(Figure):
    sprites = (
        ((0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0),
         (0, 0, 2, 1, 0),
         (0, 0, 1, 1, 0)),

        ((0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0),
         (0, 0, 2, 1, 0),
         (0, 0, 1, 1, 0)),

        ((0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0),
         (0, 0, 2, 1, 0),
         (0, 0, 1, 1, 0)),

        ((0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0),
         (0, 0, 2, 1, 0),
         (0, 0, 1, 1, 0)),
    )
    def __init__(self, y=0, x=0):
        Figure.__init__(self, y, x)
