import math
from figure import Figure

class Block:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.lees = [[0 for i in range(0, self.width)] for i in range(0, self.height)]

    def get_lees_top(self, x):
        top = self.height

        if x < 1 or x >= self.width:
            return top

        for row in range(self.height - 1, -1, -1):
            if self.lees[row][x] > 0:
                top = row

        return top

    def lees_figure(self, figure):
        sprite = figure.get_sprite()

        for y, row in enumerate(sprite):
            for x, cel in enumerate(row):
                if cel > 0:
                    self.lees[figure.y + y][figure.x + x] = 1

    def delete_full_lines(self):
        deleted_lines = 0
        y = self.height - 1
        while y >= 0:
            if self._is_line_full(y):
                self._remove_line(y)
                deleted_lines += 1
            else:
                y -= 1

        return deleted_lines

    def _remove_line(self, y):
        for x in range(0, self.width):
            # Empty this line.
            self.lees[y][x] = 0

            # Make upper lines "fall" down.
            for yy in range(y, -1, -1):
                if yy > 0:
                    cel = self.lees[yy -1][x]
                else:
                    cel = 0

                self.lees[yy][x] = cel

    def _is_line_full(self, y):
        for cel in self.lees[y]:
            if cel == 0:
                return False

        return True

    def is_full(self):
        for x in range(0, self.width):
            if self.get_lees_top(x) <= 3:
                return True
