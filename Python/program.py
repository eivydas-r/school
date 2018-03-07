file = pickAFile()
pic = makePicture(file)
show(pic)
t = makeTurtle(pic)
t.setPenColor(red)

def drawStar(turtle):
  turn(t,-18)
  x = 0
  while x < 5:
    turn(turtle,144)
    forward(turtle,50)
    x = x +1

drawStar(t)
penUp(t)
forward(t,200)
penDown(t)

y = 0
while y < 10:
 drawStar(t)
 turn(t,110)
 y = y + 1

#eivydas raulynaitis
#erauly2
#9/25/17 5pm
#i had to make a bunch of cool shapes using loops and functions