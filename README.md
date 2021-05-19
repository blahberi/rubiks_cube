# rubik's cube

---
a program that can solve a rubik's cube

---
### how to install
`git clone https://github.com/blahberi/rubiks_cube.git`

then all you need is in the Cube folder,
so take it out and put it in your project

---
### how to use
```python
from Cube.cube import Cube # import cube
from Cube import solver # import solver

cube = Cube() # create a cube
cube.scramble() # scramble cube
solver.solve(cube) # solve the cube
```
```python
scramble = cube.scramble() # Cube.scramble returns a string of the scramble
solution = solver.solve(cube) # solver.solve() returns a string of the solution
```
```python
scrambleSize = 10
cube.scramble(scrambleSize) # you can decide how complex the scramble will be. default of 20
```
```python
print(cube) # you can also get the string of a cube
```
getting the string of a cube will return this
each square of colors is a side which goes in the worder
- top
- left
- front
- right
- back
- bottom
```
w w w 
w w w 
w w w 

o o o 
o o o 
o o o 

g g g 
g g g 
g g g 

r r r 
r r r 
r r r 

b b b 
b b b 
b b b 

y y y 
y y y 
y y y 
```
so this is a solved cube with white on top and green on front

---

### about this project
I created this project for fun and to learn more programming

---

### how does it work
the program uses the "beginner's method" to solve a cube
the beginner's method is the easiest way to solve a cube
as you guessed it, beginners use this method to solve a cube

---

### how does beginners method work
beginners method solves the cube layer by layer

- you first solve a cross on the bottom layer, then you insert the corners of the bottom layer
- then you use user algorithms to insert pieces into the second layer
- after that you use more algorithms to solve a cross on the top side and then you solve it entirely
- finally, you use even more algorithms to solve the top layer corners and then edges.

---
### currently in work
#### the priority is in the same order
- show cube with openGL
- make algorithm more efficient
- add another algorithm that solves the cube with a shorter solution