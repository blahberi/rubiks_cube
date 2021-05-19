from Cube.cube import Cube
from Cube import solver
import time
import math

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


cube = Cube()
print(f'scramble: {cube.scramble()}, length = 20')
print('cube after scramble:')
print(cube)
start = time.time()
alg = solver.solve(cube)
end = time.time()
print(f'solution: {alg}, length = {len(alg.split())}')
print('cube after solve:')
print(cube)
print(f"time: {round_half_up((end - start), 3)} seconds")
