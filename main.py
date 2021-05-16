from Cube.cube import Cube
from Cube.Solver import solver
import time
import math

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

start = time.time()
for i in range(1):
    cube = Cube()
    cube.scramble()
    solver.solve(cube)
    print(f'solved cube:  {i + 1}')
end = time.time()
print(f"time: {round_half_up((end - start), 3)} seconds")
