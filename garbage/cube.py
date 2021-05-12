import numpy as np

class Cube:
    def __init__(self):
        cube = np.array(list('wwwwwwwwwooooooooogggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyy'))
        self.cube = cube.reshape(6, 3, 3)
        self.__sidesDict = {'w':0, 'o':1, 'g':2, 'r':3, 'b':4, 'y':5}
        self.__sides = ['w', 'o', 'g', 'r', 'b', 'y']
        self.__opposite = {'w': 'y', 'o': 'r', 'g': 'b', 'r': 'o', 'b': 'g', 'y': 'w'}


    def load_scramble(self, scramble):
        scramble = list(scramble)
        if len(scramble) != 54:
            return

        i = 0
        for x in range(len(self.cube)):
            for y in range(3):
                for z in range(3):
                    self.cube[x][y][z] = scramble[i]
                    i += 1

    def rotate_side(self, side, direction):
        directions = {'r ':-1, 'l':1}
        self.cube[self.__sidesDict[side]] = np.rot90(self.cube[self.__sidesDict[side]], directions[direction])

        turning_sides = []
        for i in range(6):
            currentSide = self.__sides[i]
            if currentSide != self.__opposite[side] and currentSide != side:
                turning_sides.append(currentSide)

        turning_sides = self.__order_sides(turning_sides)
        print(turning_sides)



    def __order_sides(self, turning_sides):
        if turning_sides == []:
            return
        res = []
        last_side = None
        for turning_side in turning_sides:
            if not last_side:
                last_side = turning_side
                res.append(turning_side)
            elif turning_side != self.__opposite[last_side]:
                last_side = turning_side
                res.append(turning_side)

        for side in res:
            turning_sides.remove(side)

        next = self.__order_sides(turning_sides)

        if next == None:
            return res
        for side in next:
            res.append(side)

        return res