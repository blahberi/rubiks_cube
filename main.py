from Cube.cube import Cube
from Cube.Solver import kociemba
from Cube.Solver import beginners
import time
import math


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


cube = Cube('ywogwwrry'
            'rrbooyogb'
            'wbrrgywgg'
            'grbbrywyo'
            'ybbobbgwg'
            'owroygwoy')
print(cube)
start = time.time()
solution = kociemba.solve(cube)
cube.sequence(solution)
end = time.time()
print('Done!')
print(f'solution: {solution}')
print(cube)
time = end - start
print(f"time: {round_half_up(time, 3)} seconds.")