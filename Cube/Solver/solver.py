import numpy as np
from Cube.cube import Cube

def __solve_cross(cube):
    pass


def __solve_corners(cube):
    norms = {'u': (0, -1, 0), 'r': (1, 0, 0), 'd': (0, 1, 0), 'l': (-1, 0, 0), 'b': (0, 0, 1), 'f': (0, 0, -1)}
    corners = __get_yellow_corners(cube)
    solved = []
    for corner in corners:
        if corner.norm == norms['d'] and corner not in solved:
            i = 0
            cornerSide = ''
            on = True
            while on:
                if corner.point == (1, 1, -1):
                    on = False
                    cornerSide = 'r'
                elif corner.point == (-1, 1, -1):
                    on = False
                    cornerSide = 'l'
                else:
                    i += 1
                    cube.turn('D', 'r')

            if cornerSide == 'r':
                cube.sequence('R U R`')
            if cornerSide == 'l':
                cube.sequence('L` U` L')

            for a in range(i):
                cube.turn('D', 'l')


        if corner.norm == norms['u']:
            cornerSide = ''
            on = True
            while on:
                if corner.point == (1, -1, -1):
                    on = False
                    cornerSide = 'r'
                elif corner.point == (-1, -1, -1):
                    on = False
                    cornerSide = 'l'
                else:
                    cube.turn('U', 'r')

            howMuchToTurn = ['g', 'o', 'b', 'r']
            neighbors = __get_neighbors(cube, corner)
            sideNeighbor = None
            for neighbor in neighbors:
                if neighbor.norm == norms[cornerSide]:
                    sideNeighbor = neighbor

            for i in range(howMuchToTurn.index(sideNeighbor.color)):
                cube.turn('D', 'r')
            if cornerSide == 'r':
                for i in range(3):
                    cube.sequence('U R U` R`')
            elif cornerSide == 'l':
                for i in range(3):
                    cube.sequence('U` L` U L')
            for i in range(howMuchToTurn.index(sideNeighbor.color)):
                cube.turn('D', 'l')
            solved.append(corner)

        if corner not in solved:
            if corner.point[1] == 1:
                on = True
                i = 0
                while on:
                    if corner.norm == (0, 0, -1):
                        if corner.point == (1, 1, -1):
                            on = False
                            cube.sequence('F` U` F U')
                        elif corner.point == (-1, 1, -1):
                            on = False
                            cube.sequence('F U F` U`')
                    else:
                        cube.turn('D', 'r')
                        i += 1
                for a in range(i):
                    cube.turn('D', 'l')

            cornerSide = ''
            on = True
            while on:
                if corner.norm == (0, 0, -1):
                    if corner.point == (1, -1, -1):
                        on = False
                        cornerSide = 'r'
                    elif corner.point == (-1, -1, -1):
                        on = False
                        cornerSide = 'l'
                else:
                    cube.turn('U', 'r')
            howMuchToTurn = ['g', 'o', 'b', 'r']
            neighbors = __get_neighbors(cube, corner)
            topNeighbor = None
            for neighbor in neighbors:
                if neighbor.norm == norms['u']:
                    topNeighbor = neighbor
            for i in range(howMuchToTurn.index(topNeighbor.color)):
                cube.turn('D', 'r')
            if cornerSide == 'r':
                cube.sequence('U R U` R`')
            elif cornerSide == 'l':
                cube.sequence('U` L` U L')
            for i in range(howMuchToTurn.index(topNeighbor.color)):
                cube.turn('D', 'l')
            solved.append(corner)


def __oll_step_2(cube):
    side = __get_side(cube, 'U', 'w')

    no_corners = '# # \n' \
                 '# # \n'

    one_corner = '# # \n' \
                 'w # \n'

    close_corners = '# w \n' \
                    '# w \n'

    diagonal_corners = 'w # \n' \
                       '# w \n'

    solved = 'w w \n' \
             'w w \n'

    cases = [no_corners, one_corner, close_corners, diagonal_corners]

    while True:
        if side in cases:
            cube.sequence('R U R` U R U2 R`')
            side = __get_side(cube, 'U', 'w')

        elif side == solved:
            return

        else:
            cube.turn('U', 'r')
            side = __get_side(cube, 'U', 'w')

def __pll_step_1(cube):
    solvedCube = Cube()
    side = cube.get_side_in_matrix('L')
    didTPerm = False

    for i in range(4):
        if str(cube) == str(solvedCube):
            return
        else:
            cube.turn('U', 'r')

    for a in range(4):
        isTperm = True
        i = 0
        for color in side:
            if i == 2:
                break
            if color != '\n' and color != ' ':
                i += 1
                if color != side[0]:
                    isTperm = False
                    break

        if isTperm:
            cube.sequence('R U R` U` R` F R2 U` R` U` R U R` F`')
            didTPerm = True
            break
        else:
            cube.turn('U', 'r')
            side = cube.get_side_in_matrix('L')

    if not didTPerm:
        cube.sequence('F R U` R` U` R U R` F` R U R` U` R` F R F`')

    while True:
        if str(cube) == str(solvedCube):
            return
        else:
            cube.turn('U', 'r')


def __get_yellow_edges(cube):
    edges = []
    for cell in cube.cells:
        if cell.color == 'y':
            i = 0
            for point in cell.point:
                if point == 0:
                    i += 1
            if i == 1:
                edges.append(cell)

    return edges


def __get_yellow_corners(cube):
    corners = []
    for cell in cube.cells:
        if cell.color == 'y':
            if 0 not in cell.point:
                corners.append(cell)
    return corners


def __get_neighbors(cube, cell):
    res = []
    for item in cube.cells:
        if item.point == cell.point:
            res.append(item)
    return res


def __get_side(cube, side, color):
    res = cube.get_side_in_matrix(side)
    res = list(res)
    for piece in res:
        if piece != color and piece != '\n' and piece != ' ':
            res[res.index(piece)] = '#'

    res = ''.join(res)
    return res

def solve(cube):
    __solve_corners(cube)
    __oll_step_2(cube)
    __pll_step_1(cube)