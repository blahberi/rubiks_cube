from Cube.cube import Cube
import time

cube = Cube()
start = time.time()
cube.sequence('R U R` U` R` F R2 U` R` U` R U R` F`')
end = time.time()
print(cube)
print(f"time: {(end - start)} seconds")
