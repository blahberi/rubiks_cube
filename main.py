from Cube.cube import Cube
from Cube import solver
import time
import math

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


cube = Cube()
"""
cube.load_scramble('wrw'
      'oww'
      'ryb'
      
      'oyg'
      'gog'
      'grr'
      
      'yry'
      'ygo'
      'bbo'
      
      'obr'
      'brw'
      'wry'
      
      'bwb'
      'obw'
      'oor'
      
      'gbg'
      'yyg'
      'ygw')
"""
scramble = cube.scramble()
print(f'scramble: {scramble}, length = {len(scramble.split())}')
print('cube after scramble:')
print(cube)
start = time.time()
alg = solver.solve(cube)
end = time.time()
print(f'solution: {alg}, length = {len(alg.split())}')
print('cube after solve:')
print(cube)
print(f"time: {round_half_up((end - start), 3)} seconds")
input()