from Cube.cube import Cube
from Cube import solver
import time
import math


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


times = []
print('Running 100 tests...')
for i in range(100):
    cube = Cube()
    cube.scramble()
    start = time.time()
    solver.solve(cube)
    end = time.time()
    times.append(end - start)
print('Done!')
average = sum(times) / len(times)
print(f"Average time: {round_half_up(average, 3)} seconds.")
print(f"Total time: {round_half_up(sum(times), 3)} seconds.")