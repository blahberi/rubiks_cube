import numpy as np
import random
from Cube.cell import Cell

class MagicalMatrix:
    def __init__(self):
        self.magical_matrix = np.array([
            [
                [[0, 0, 1], [0, 1, 0], [-1, 0, 0]],
                [[0, 0, -1], [0, 1, 0], [1, 0, 0]]
            ],
            [
                [[1, 0, 0], [0, 0, -1], [0, 1, 0]],
                [[1, 0, 0], [0, 0, 1], [0, -1, 0]]
            ],
            [
                [[0, -1, 0], [1, 0, 0], [0, 0, 1]],
                [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
            ],
            [
                [[1, 0, 0], [0, 0, 1], [0, -1, 0]],
                [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
            ],
            [
                [[0, 1, 0], [-1, 0, 0], [0, 0, 1]],
                [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
            ],
            [
                [[0, 0, -1], [0, 1, 0], [1, 0, 0]],
                [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]
            ]])

    def get_matrix(self, move, direction):
        moveInt = 0
        directions = {'r': 1, 'l': 0}
        moves = ['U', 'L', 'F', 'R', 'B', 'D']
        for m in moves:
            if m == move:
                moveInt = moves.index(m)
        return self.magical_matrix[moveInt][directions[direction]]


class Cube:
    def __init__(self, scramble=None):
        self.magical_matrix = MagicalMatrix()
        self.cells = []
        self.dim = (3, 3)
        self.positionNums = []
        self.__build_cube(scramble)
        self.colorToNorm = {'U': (0, -1, 0), 'L': (-1, 0, 0), 'F': (0, 0, -1), 'R': (1, 0, 0), 'B': (0, 0, 1), 'D': (0, 1, 0)}

    def __build_cube(self, scramble):
        if not scramble:
            scramble = self.__get_solved_scramble()
        sideSize = self.dim[0] * self.dim[1]
        scramble = list(scramble)

        self.positionsNums = []
        
        if sideSize % 2 == 0:
            nums = range(int(self.dim[0] / 2))
            for i in nums:
                self.positionsNums.append(-i - 1)
            self.positionsNums.reverse()
            
            for i in nums:
                self.positionsNums.append(i + 1)
        else:
            nums = range(int((self.dim[0] - 1) / 2))
            for i in nums:
                self.positionsNums.append(-i - 1)
            self.positionsNums.reverse()
            self.positionsNums.append(0)
            for i in nums:
                self.positionsNums.append(i + 1)

        i = 0
        #top
        for z in self.positionsNums:
            for x in self.positionsNums:
                self.cells.append(Cell(point=(x, -1, z), norm=(0, -1, 0), color=scramble[i]))
                i += 1
        #left
        for y in self.positionsNums:
            for z in self.positionsNums:
                self.cells.append(Cell(point=(-1, y, z), norm=(-1, 0, 0), color=scramble[i]))
                i += 1
        #front
        for y in self.positionsNums:
            for x in self.positionsNums:
                self.cells.append(Cell(point=(x, y, -1), norm=(0, 0, -1), color=scramble[i]))
                i += 1
        #right
        for y in self.positionsNums:
            for z in self.positionsNums:
                self.cells.append(Cell(point=(1, y, z), norm=(1, 0, 0), color=scramble[i]))
                i += 1
        #back
        for y in self.positionsNums:
            for x in self.positionsNums:
                self.cells.append(Cell(point=(x, y, 1), norm=(0, 0, 1), color=scramble[i]))
                i += 1

        #bottom
        for z in self.positionsNums:
            for x in self.positionsNums:
                self.cells.append(Cell(point=(x, 1, z), norm=(0, 1, 0), color=scramble[i]))
                i += 1

    def __get_side(self, side):
        res = []
        temp = []
        for cell in self.cells:
            if cell.norm == self.colorToNorm[side]:
                temp.append(cell)

        for a in self.positionsNums:
            for b in self.positionsNums:
                point = []
                for i in range(3):
                    if self.colorToNorm[side][i] == 0:
                        if i == 0:
                            point.append(b)
                        elif i == 1:
                            point.append(a)
                        elif i == 2:
                            if self.colorToNorm[side][0] == 0:
                                point.append(a)
                            else:
                                point.append(b)
                    else:
                        point.append(self.colorToNorm[side][i])
                for cell in temp:
                    if cell.point == tuple(point):
                        res.append(cell)
        return res

    def get_side_in_matrix(self, side):
        res = []
        cells = self.__get_side(side)
        if side in ('B', 'U', 'L'):
            i = 1
            if side == 'U':
                i = 0
            cells = np.array(cells)
            cells = cells.reshape(self.dim[0], self.dim[1])
            cells = np.flip(cells, i)
            cells = cells.reshape(1, self.dim[0] * self.dim[1])
            cells = cells.tolist()[0]
        colors = []
        for cell in cells:
            colors.append(cell.color)
        i = 0
        res = np.array(colors)
        res = res.reshape(self.dim[0], self.dim[1])

        return res

    def __get_solved_scramble(self):
        res = ''
        sides = ['w', 'o', 'g', 'r', 'b', 'y']
        sideSize = self.dim[0] * self.dim[1]
        for side in sides:
            for i in range(sideSize):
                res += side
        return res

    def move(self, direction):
        opposite = {'r': 'l', 'l': 'r'}
        self.turn('U', direction)
        self.turn('M', direction)
        self.turn('D', opposite[direction])

    def turn(self, side, direction):
        cells = []
        #smallest cordinates possible
        negative = self.positionsNums[0]
        #biggest cordinates possible
        positive = self.positionsNums[-1]
        mid = 0
        #the first number in the tuple means which axis on the cordinates are we going to compare
        sidesPoint = {'U': (1, negative), 'L': (0, negative), 'F': (2, negative), 'R': (0, positive), 'B': (2, positive), 'D': (1, positive), 'M': (1, mid)}

        for cell in self.cells:
            if cell.point[sidesPoint[side][0]] == sidesPoint[side][1]:
                cells.append(cell)

        sideCells = []
        if side != 'M':
            sideCells = self.__get_side(side)
        beltCells = []
        for cell in cells:
            if cell not in sideCells:
                beltCells.append(cell)

        if side == 'M':
            if self.dim != (3, 3):
                return
            for cell in cells:
                if cell in beltCells:
                    cell.point = tuple(np.dot(list(cell.point), self.magical_matrix.get_matrix(side, direction)))
                    cell.norm = tuple(np.dot(list(cell.norm), self.magical_matrix.get_matrix(side, direction)))
            return

        for cell in cells:
            cell.point = tuple(np.dot(list(cell.point), self.magical_matrix.get_matrix(side, direction)))
            if cell in beltCells:
                cell.norm = tuple(np.dot(list(cell.norm), self.magical_matrix.get_matrix(side, direction)))

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

    def scramble(self, size=20):
        sides = ['U', 'L', 'F', 'R', 'B', 'D']
        scramble = ''
        for i in range(size):
            addedMove = random.choice(sides)
            rand = random.randint(1, 5)
            if rand in (1, 2):
                pass
            elif rand in (3, 4):
                addedMove += '`'
            else:
                addedMove += '2'
            scramble += addedMove + ' '
        self.sequence(scramble)
        return scramble

    def __str__(self):
        res = ''
        sides = ['U', 'L', 'F', 'R', 'B', 'D']
        for side in sides:
            cells = self.__get_side(side)
            if side in ('B', 'U', 'L'):
                i = 1
                if side == 'U':
                    i = 0
                cells = np.array(cells)
                cells = cells.reshape(self.dim[0], self.dim[1])
                cells = np.flip(cells, i)
                cells = cells.reshape(1, self.dim[0] * self.dim[1])
                cells = cells.tolist()[0]
            colors = []
            for cell in cells:
                colors.append(cell.color)
            i = 0
            for a in range(self.dim[0]):
                for b in range(self.dim[1]):
                    res += colors[i]
                    res += " "
                    i += 1
                res += '\n'
            res += '\n'
        return res
