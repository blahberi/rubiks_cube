# Rubik's cube

___
A program that can solve a rubik's cube

___
### How to install
`git clone https://github.com/blahberi/rubiks_cube.git`

Then all you need is in the Cube folder,
so take it out and put it in your project

___
### How to use
```python
from Cube.cube import Cube # import cube
from Cube import solver # import solver

cube = Cube() # create a cube
cube.scramble() # scramble cube
solver.solve(cube) # solve the cube
```
```python
scramble = cube.scramble() # Cube.scramble() returns a string of the scramble
solution = solver.solve(cube) # solver.solve() returns a string of the solution
```
```python
scrambleSize = 10
cube.scramble(scrambleSize) # you can decide how complex the scramble will be. default of 20
```
```python
print(cube) # you can also get the string of a cube
```
Getting the string of a cube will return this:

**each square of colors is a side on the cube which goes in the order:**
1. Top
2. Left
3. Front
4. Right
5. Back
6. Bottom
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

- w = White
- o = Orange
- g = Green
- r = Red
- b = Blue
- y = Yellow

So this is a solved cube with white on top and green on front

___

### About this project
I created this project for fun and to learn more programming

___

### How does it work
The program uses the "beginner's method" to solve a cube.
The beginner's method is one of the easiest ways to solve a cube.
as you guessed it, beginners use this method to solve a cube as well.

___

### How does beginners method work
Beginners method solves the cube layer by layer.

- You first solve a cross on the bottom layer, then you insert the corners of the bottom layer.
- Then you use user algorithms to insert pieces into the second layer.
- After that you use more algorithms to solve a cross on the top side and then you solve it entirely.
- Finally, you use even more algorithms to solve the top layer corners and then edges.

___
### Currently in the work
- Show cube with openGL.
- Make algorithm more efficient.
- Add another algorithm that solves the cube with a shorter solution.