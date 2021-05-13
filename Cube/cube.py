import numpy as np
from Cube.side import Side


class Cube:
    def __init__(self, dim):
        self.dim = dim
        self.front = Side(self.dim)
        self.__build_cube()

    def __str__(self):
        res = ""
        res += str(self.front.top) + '\n'
        res += str(self.front.left) + '\n'
        res += str(self.front) + '\n'
        res += str(self.front.right) + '\n'
        res += str(self.front.right.right) + '\n'
        res += str(self.front.bottom) + '\n'

        return res

    def __build_cube(self):
        top = Side(self.dim)
        right = Side(self.dim)
        bottom = Side(self.dim)
        left = Side(self.dim)
        back = Side(self.dim)

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

        sideSize = self.dim[0] * self.dim[1]
        scramble = ""
        colors = ['w', 'o', 'g', 'r', 'b', 'y']
        for color in colors:
            for i in range(sideSize):
                scramble += color
        self.load_scramble(scramble)

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
        end = self.dim[0] - 1
        if direction == 'l':
            for i in range(self.dim[0]):
                temp = self.front.top.side[end][i]
                self.front.top.side[end][i] = self.front.right.side[i][0]
                self.front.right.side[i][0] = self.front.bottom.side[0][end - i]
                self.front.bottom.side[0][(self.dim[0] - 1) - i] = self.front.left.side[end - i][end]
                self.front.left.side[end - i][end] = temp
        if direction == 'r':
            for i in range(self.dim[0]):
                temp = self.front.right.side[i][0]
                self.front.right.side[i][0] = self.front.top.side[end][i]
                temp2 = self.front.bottom.side[0][end - i]
                self.front.bottom.side[0][end - i] = temp
                temp = temp2
                temp2 = self.front.left.side[end - i][end]
                self.front.left.side[end - i][end] = temp
                temp = temp2
                self.front.top.side[end][i] = temp

    def turn(self, side, direction):
        """
        run a single move on the cube
        :param side:
        :param direction:
        :return: void
        """
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
        """
        run a sequence of moves on the cube
        :param sequence:
        :return: void
        """
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
                        pass
                        # W moves are not fully done yet
                    else:
                        self.turn(move[0], direction)
                        moved = True

            elif "W" in move:
                pass
                # W moves are not fully done yet

            if not moved:
                self.turn(move[0], direction)
            else:
                moved = False

    def load_scramble(self, scramble):
        """
        loads the scramble onto the cube

        :param scramble:
        :return: void
        """

        sideSize = self.dim[0] * self.dim[1]
        scramble = list(scramble)[:sideSize * 6]

        front = self.front
        top = self.front.top
        right = self.front.right
        bottom = self.front.bottom
        left = self.front.left
        back = self.front.right.right

        sides = [top, left, front, right, back, bottom]
        i = 0
        for side in sides:
            side.load_colors(scramble[i:i + sideSize])
            i += sideSize
