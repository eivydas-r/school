file = pickAFile()
pic = makePicture(file)

#world = makeWorld(1000,1000)

def drawSpiral(turtle,size):
  x = 0
  scale = 0
  print "this ran"
  while (x < size):
    t.setPenColor(makeColor(220-(x*3),x*3,x*9))
    forward(t,50)
    turn(turtle,6+scale)
    x = x + 1
    scale = scale + 1

def drawHexagon(turtle,size):
  x = 0
  while (x < 5):
    forward(turtle,size)
    turn(turtle,360/6)
    x = x + 1

def drawSwirl(turtle,size):
  x = 0
  while (x < 5):
    forward(turtle,size)
    turn(turtle,360/90)
    x = x + 1

t = makeTurtle(pic)
t.setPenWidth(1)
t.setPenColor(red)    
penUp(t)
printNow("1")
forward(t,250)
turn(t,90)
backward(t,180)
penDown(t)
printNow("yes")
drawSpiral(t,50)

f = makeTurtle(pic)
f.setPenWidth(2)
f.setPenColor(green)
penUp(f)
turnLeft(f)
forward(f,250)
turnRight(f)
forward(f,300)
penDown(f)
x = 0
while (x < 20): #makes second swirl
  drawSwirl(f,2*x)
  f.setPenColor(makeColor(0,50+(x*10),x*9))
  forward(f,15)
  turn(f,50)
  x = x + 1

w = makeTurtle(pic)
w.setPenWidth(2)
w.setPenColor(blue)
penUp(w)
turnRight(w)
forward(w,380)
turnLeft(w)
forward(w,200)
penDown(w)
x = 0
while (x < 30):
  drawSwirl(w,x)
  w.setPenColor(makeColor(0,x*10,x*30))
  forward(w,20)
  turn(w,20)
  x = x + 1

g = makeTurtle(pic)
g.setPenWidth(2)
g.setPenColor(white)
penUp(g)
backward(g,200)
turnLeft(g)
forward(g,300)
turn(g,-45)
penDown(g)
x = 0
while (x < 15):
  drawHexagon(g,x*10)
  g.setPenColor(makeColor(255,150,x*30))
  x = x + 1

g = makeTurtle(pic)
g.setPenWidth(2)
g.setPenColor(orange)
penUp(g)
backward(g,200)
turnRight(g)
forward(g,300)
turn(g,-45)
penDown(g)
x = 0
while (x < 15):
  drawHexagon(g,x*10)
  g.setPenColor(makeColor(0,0,x*10))
  forward(g,x*3)
  turn(g,9)
  x = x + 1

g = makeTurtle(pic)
g.setPenWidth(2)
g.setPenColor(orange)
penUp(g)
forward(g,50)
turnRight(g)
backward(g,500)
turn(g,-45)
penDown(g)
x = 0
while (x < 15):
  drawHexagon(g,x*5)
  g.setPenColor(makeColor(255,255-x*10,255-x*5))
  forward(g,x*3)
  turn(g,90)
  x = x + 1

pic.show() #always last