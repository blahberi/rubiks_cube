import numpy as np
from Cube.side import Side


class Cube:
    def __init__(self):
        self.front = Side('ggggggggg')
        self.__built_cube()

    def __str__(self):
        res = ""
        res += str(self.front.top) + '\n'
        res += str(self.front.left) + '\n'
        res += str(self.front) + '\n'
        res += str(self.front.right) + '\n'
        res += str(self.front.right.right) + '\n'
        res += str(self.front.bottom) + '\n'

        return res

    def __built_cube(self):
        top = Side('wwwwwwwww')
        right = Side('rrrrrrrrr')
        bottom = Side('yyyyyyyyy')
        left = Side('ooooooooo')
        back = Side('bbbbbbbbb')

        top.top = back
        top.right = right
        top.bottom = self.front
        top.left = left

        right.top = top
        right.right = back
        right.bottom = bottom
        right.left = self.front

        bottom.top = self.front
        bottom.right = right
        bottom.bottom = back
        bottom.left = left

        left.top = top
        left.right = self.front
        left.bottom = bottom
        left.left = back

        back.top = top
        back.right = right
        back.bottom = bottom
        back.left = left

        self.front.top = top
        self.front.right = right
        self.front.bottom = bottom
        self.front.left = left

    def __move(self, direction):
        if direction == "t":
            self.front.left.side = np.rot90(self.front.left.side, -1)
            self.front.right.side = np.rot90(self.front.right.side, 1)
            self.front = self.front.top
            self.front.right.right.side = np.rot90(self.front.right.right.side, 2)
        elif direction == "r":
            self.front.top.side = np.rot90(self.front.top.side, -1)
            self.front.bottom.side = np.rot90(self.front.bottom.side, 1)
            self.front = self.front.right
        elif direction == "b":
            self.front.right.side = np.rot90(self.front.right.side, -1)
            self.front.left.side = np.rot90(self.front.left.side, 1)
            self.front = self.front.bottom
            self.front.right.right.side = np.rot90(self.front.right.right.side, 2)
        elif direction == "l":
            self.front.bottom.side = np.rot90(self.front.bottom.side, -1)
            self.front.top.side = np.rot90(self.front.top.side, 1)
            self.front = self.front.left

    def __turn(self, direction):
        directions = {'r': -1, 'l': 1}
        self.front.side = np.rot90(self.front.side, directions[direction])
        if direction == 'l':
            for i in range(3):
                temp = self.front.top.side[2][i]
                self.front.top.side[2][i] = self.front.right.side[i][0]
                self.front.right.side[i][0] = self.front.bottom.side[0][2 - i]
                self.front.bottom.side[0][2 - i] = self.front.left.side[2 - i][2]
                self.front.left.side[2 - i][2] = temp
        if direction == 'r':
            for i in range(3):
                temp = self.front.right.side[i][0]
                self.front.right.side[i][0] = self.front.top.side[2][i]
                temp2 = self.front.bottom.side[0][2 - i]
                self.front.bottom.side[0][2 - i] = temp
                temp = temp2
                temp2 = self.front.left.side[2 - i][2]
                self.front.left.side[2 - i][2] = temp
                temp = temp2
                self.front.top.side[2][i] = temp

    def turn(self, side, direction):
        if side == 'U':
            self.__move('t')
            self.__turn(direction)
            self.__move('b')

        elif side == 'R':
            self.__move('r')
            self.__turn(direction)
            self.__move('l')

        elif side == 'D':
            self.__move('r')
            self.__turn(direction)
            self.__move('l')

        elif side == 'L':
            self.__move('l')
            self.__turn(direction)
            self.__move('r')

        elif side == 'B':
            self.__move('r')
            self.__move('r')
            self.__turn(direction)
            self.__move('l')
            self.__move('l')

        elif side == 'F':
            self.__turn(direction)

        elif side == 'M':
            pass

    def sequence(self, sequence):
        opposite = {'R': 'L', 'L': 'R', 'U': 'D', 'D': 'U', 'F': 'B', 'B': 'F'}
        moved = False
        sequence = sequence.split()
        for move in sequence:
            move = list(move)
            direction = 'r'
            if "`" in move:
                direction = 'l'

            elif "2" in move:
                for i in range(2):
                    if "W" in move:
                        self.turn(opposite[move[0]], direction)
                        # W moves are not fully done yet
                    else:
                        self.turn(move[0], direction)
                        moved = True

            elif "W" in move:
                self.turn(opposite[move[0]], direction)
                # W moves are not fully done yet

            if not moved:
                self.turn(move[0], direction)
            else:
                moved = False
