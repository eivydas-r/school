#eivydas raulynaitis
#erauly2
#monday at 5pm
#i had to put text on an image and then save it

file = pickAFile()
pic = makePicture(file)

def addSomeText(picture,xpos,ypos,text):
  addText(picture,xpos,ypos,text,black)

addSomeText(pic,20,getHeight(pic)-20,"look at this dog")

file2 = pickAFile()
writePictureTo(pic,file2)

pic.show()