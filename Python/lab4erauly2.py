#Eivydas Raulynaitis
#erauly2
#Monday at 5PM
#in this project, i had to draw squares, and then surround the squares with more squares

def makeSquare(turtle,size):
  forward(turtle,size)
  turnRight(t)
  forward(turtle,size)
  turnRight(t)
  forward(turtle,size)
  turnRight(t)
  forward(turtle,size)
  turnRight(t)

world = makeWorld()
t = makeTurtle(world)

x = 0
while (x < 25):
  makeSquare(t,50+10*x)
  penUp(t)
  turnLeft(t)
  forward(t,5)
  turnRight(t)
  backward(t,5)
  penDown(t)
  x = x + 1