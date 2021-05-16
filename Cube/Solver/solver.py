import numpy as np
from Cube.cube import Cube


def __solve_cross(cube):
    edges = __get_yellow_edges(cube)
    b = 0
    for edge in edges:
        i = 0
        if edge.point[1] == 0:
            while True:
                if edge.norm[2] == -1:
                    if edge.point[0] == 1:
                        cube.sequence('R U R`')

                    elif edge.point[0] == -1:
                        cube.sequence('L` U` L')
                    for a in range(i):
                        cube.turn('M', 'l')

                    break
                else:
                    cube.turn('M', 'r')
                    i += 1

        elif edge.norm[1] == -1:
            while True:
                if edge.point[2] == -1:
                    break
                else:
                    cube.turn('U', 'r')

        elif edge.point[1] == -1:
            while True:
                if edge.norm[2] == -1:
                    cube.sequence('F R U` R` F` U2')
                    break
                else:
                    cube.turn('U', 'r')

        elif edge.norm[1] == 1:
            i = 0
            while True:
                if edge.point[2] == -1:
                    cube.sequence('F2')
                    for a in range(i):
                        cube.turn('D', 'l')
                    break
                else:
                    cube.turn('D', 'r')
                    i += 1

        elif edge.point[1] == 1:
            i = 0
            while True:
                if edge.norm[2] == -1:
                    cube.sequence('F` R U` R` F U2')
                    for a in range(i):
                        cube.turn('D', 'l')
                    break
                else:
                    cube.turn('D', 'r')
                    i += 1

        edgeColor = __get_neighbors(cube, edge)[0].color

        colors_to_turns = {'g': 'F', 'o': 'L', 'b': 'B', 'r': 'R'}

        for a in range(tuple(colors_to_turns).index(edgeColor)):
            cube.turn('U', 'r')
        for a in range(2):
            cube.turn(colors_to_turns[edgeColor], 'r')
        b += 1


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


def __solve_second_layer(cube):
    edges = __get_all_edges(cube)
    #i need to do that 2 times because it does not remove all of them in one go
    #idk y i will check later
    for i in range(2):
        for edge in edges:
            if edge.color == 'y':
                edges.remove(edge)
                edges.remove(__get_neighbors(cube, edge)[0])
            elif __get_neighbors(cube, edge)[0].color == 'y':
                edges.remove(edge)
                edges.remove(__get_neighbors(cube, edge)[0])
            elif edge.color == 'w':
                edges.remove(edge)
                edges.remove(__get_neighbors(cube, edge)[0])
            elif __get_neighbors(cube, edge)[0].color == 'w':
                edges.remove(edge)
                edges.remove(__get_neighbors(cube, edge)[0])

    b = 0
    for edge in edges:
        if edge.point[1] == 0:
            i = 0
            while True:
                if edge.norm[2] == -1:
                    if edge.point[0] == 1:
                        cube.sequence("U R U` R` U` F` U F")
                    elif edge.point[0] == -1:
                        cube.sequence("U` L` U L U F U` F`")
                    for a in range(i):
                        cube.turn('M', 'l')
                    break
                else:
                    cube.turn('M', 'r')
                    i += 1

        if edge.point[1] == -1:
            while True:
                if edge.point[2] == -1:
                    break
                else:
                    cube.turn('U', 'r')
            color1 = edge.color
            color2 = __get_neighbors(cube, edge)[0].color
            if edge.norm[1] == -1:
                color2 = color1
                color1 = __get_neighbors(cube, edge)[0].color

            #the tuples in the dict show the color that is in the right and the color that is in the left
            colors_to_turns = {'g': ('r', 'o'), 'o': ('g', 'b'), 'b': ('o', 'r'), 'r': ('b', 'g')}
            for i in range(tuple(colors_to_turns).index(color1)):
                cube.move('l')
                cube.turn('U', 'r')

            if color2 == colors_to_turns[color1][0]:
                cube.sequence("U R U` R` U` F` U F")
            elif color2 == colors_to_turns[color1][1]:
                cube.sequence("U` L` U L U F U` F`")
            for i in range(tuple(colors_to_turns).index(color1)):
                cube.move('r')

            edges.remove(__get_neighbors(cube, edge)[0])
            b += 1



def __oll_step_2(cube):
    side = __get_side_corners_map(cube, 'U', 'w')

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
            side = __get_side_corners_map(cube, 'U', 'w')

        elif side == solved:
            return

        else:
            cube.turn('U', 'r')
            side = __get_side_corners_map(cube, 'U', 'w')


def __oll_step_1(cube):
    side = __get_side_edges_map(cube, 'U', 'w')

    case1 = '# w # \n' \
            'w w # \n' \
            '# # # \n'

    case2 = '# # # \n' \
            'w w w \n' \
            '# # # \n'

    case3 = '# # # \n' \
            '# w # \n' \
            '# # # \n'

    solved = '# w # \n' \
             'w w w \n' \
             '# w # \n'

    cases = (case1, case2, case3)

    while True:
        if side in cases:
            cube.sequence("F R U R` U` F`")
            side = __get_side_edges_map(cube, 'U', 'w')
        elif side == solved:
            return
        else:
            cube.turn('U', 'r')
            side = __get_side_edges_map(cube, 'U', 'w')


def __pll_step_1(cube):
    solvedCube = Cube()
    side = __get_side_corners(cube, 'L')
    didTPerm = False

    sides = ['U', 'L', 'F', 'R', 'B', 'D']
    for i in range(4):
        done = True
        for currentSide in sides:
            if __get_side_corners(cube, currentSide) != __get_side_corners(solvedCube, currentSide):
                done = False
        if done:
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
            side = __get_side_corners(cube, 'L')

    if not didTPerm:
        cube.sequence('F R U` R` U` R U R` F` R U R` U` R` F R F`')

    while True:
        done = True
        for side in sides:
            if __get_side_corners(cube, side) != __get_side_corners(solvedCube, side):
                done = False
        if done:
            return
        else:
            cube.turn('U', 'r')


def __pll_step_2(cube):
    side = cube.get_side_in_matrix('B')
    solvedCube = Cube()

    for i in range(4):
        if str(cube) == str(solvedCube):
            return
        else:
            cube.turn('U', 'r')

    while True:
        side = cube.get_side_in_matrix('B')
        for i in range(4):
            isOkToDoAlg = True
            for a in range(3):
                if side[0][a] != side[0][0]:
                    isOkToDoAlg = False
            if isOkToDoAlg:
                break
            else:
                cube.turn('U', 'r')
                side = cube.get_side_in_matrix('B')
        cube.sequence('R2 U R U R` U` R` U` R` U R`')
        for i in range(4):
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


def __get_all_edges(cube):
    edges = []
    for cell in cube.cells:
        i = 0
        for point in cell.point:
            if point == 0:
                i += 1
        if i == 1:
            edges.append(cell)

    return edges


def __get_all_corners(cube):
    corners = []
    for cell in cube.cells:
        if 0 not in cell.point:
            corners.append(cell)
    return corners


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
        if item.point == cell.point and item != cell:
            res.append(item)
    return res


def __get_side_corners(cube, side):
    res = ''
    mat = cube.get_side_in_matrix(side)
    cords = [0, -1]
    for y in cords:
        for x in cords:
            res += mat[y][x]
            res += ' '
        res += '\n'
    return res


def __get_side_edges(cube, side):
    res = ''
    mat = cube.get_side_in_matrix(side)
    for y in range(3):
        for x in range(3):
            if x-1 == 0 or y-1 == 0:
                res += mat[y][x]
                res += ' '
            else:
                res += '#'
                res += ' '
        res += '\n'
    return res


def __get_side_corners_map(cube, side, color):
    res = ''
    mat = cube.get_side_in_matrix(side)
    cords = [0, -1]
    for y in cords:
        for x in cords:
            current = mat[y][x]
            if current != '\n' and current != ' ' and current != color:
                res += '# '
            else:
                res += mat[y][x]
                res += ' '
        res += '\n'
    return res


def __get_side_edges_map(cube, side, color):
    res = ''
    mat = cube.get_side_in_matrix(side)
    for y in range(3):
        for x in range(3):
            if (x - 1 == 0 or y - 1 == 0) and mat[y][x] == color:
                res += mat[y][x]
                res += ' '
            else:
                res += '#'
                res += ' '
        res += '\n'
    return res


def __solve_3x3(cube):
    __solve_cross(cube)
    __solve_corners(cube)
    __solve_second_layer(cube)
    __oll_step_1(cube)
    __oll_step_2(cube)
    __pll_step_1(cube)
    __pll_step_2(cube)


def __solve_2x2(cube):
    __solve_corners(cube)
    __oll_step_2(cube)
    __pll_step_1(cube)


def solve(cube):
    if cube.dim == (2, 2):
        __solve_2x2(cube)
    elif cube.dim == (3, 3):
        __solve_3x3(cube)