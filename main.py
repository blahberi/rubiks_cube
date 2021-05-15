from Cube.cube import Cube
from Cube.Solver import solver
import time

start = time.time()
for i in range(100):
    cube = Cube()
    cube.scramble(50)
    solver.solve(cube)
    print(f'solved cube: {i}')
end = time.time()
print(f"time: {(end - start)} seconds")
