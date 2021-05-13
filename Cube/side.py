import numpy as np


class Side:
    def __init__(self, colors):
        colors = list(colors)
        self.side = np.array(colors)
        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

        self.side = self.side.reshape(3, 3)

        i = 0
        for y in range(len(self.side)):
            for x in range(len(self.side[y])):
                self.side[y][x] = colors[i]
                i += 1

    def print_side(self):
        for y in range(len(self.side)):
            for x in range(len(self.side[y])):
                print(self.side[y][x], end=" ")
            print("")
        print(" ")

    def __str__(self):
        res = ""
        for y in range(len(self.side)):
            for x in range(len(self.side[y])):
                res += self.side[y][x] + " "
            res += '\n'
        res += " " + '\n'

        return res
