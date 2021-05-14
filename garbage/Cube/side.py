import numpy as np


class Side:
    def __init__(self, dim):
        self.side = None
        self.dim = dim

        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

    def load_colors(self, colors):
        """
        loads the colors onto the side
        :param colors:
        :return: void
        """
        colors = list(colors)[:self.dim[0] * self.dim[1]]
        self.side = np.array(colors)
        self.side = self.side.reshape(*self.dim)

        i = 0
        for y in range(len(self.side)):
            for x in range(len(self.side[y])):
                self.side[y][x] = colors[i]
                i += 1

    def __str__(self):
        res = ""
        for y in range(len(self.side)):
            for x in range(len(self.side[y])):
                res += self.side[y][x] + " "
            res += '\n'
        res += " " + '\n'

        return res

    def turn(self, direction):
        directions = {'r': -1, 'l': 1}
        self.side = np.rot90(self.side, directions[direction])
        """
        if direction == 'r':
            temp = self.top
            self.top = self.left
            self.left = self.bottom
            self.bottom = self.right
            self.right = temp

        if direction == 'l':
            temp = self.top
            self.top = self.right
            self.right = self.bottom
            self.bottom = self.left
            self.left = temp
        """ # this is for later when i use some more advanced methods to solve the cube
