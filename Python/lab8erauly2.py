#eivydas raulynaitis
#erauly2
#monday @ 5pm
#i had request an integer and make 3 functions that rotate an image based on the integer

#print info
print("Eivydas Raulynaitis, erauly2")
#ask for integer value and then print it
value = requestIntegerInRange("Enter an integer between 1 and 3",1,3)
print("User entered: ",value)

#request a picture
file = pickAFile()
picture = makePicture(file)

#rotate the picture 90 degrees
def rotate90(pic):
  #make an empty picture for the new picture
  pic2 = makeEmptyPicture(getHeight(pic), getWidth(pic))
  #loops for all pixels
  for x in range(0,getWidth(pic),1):
    for y in range(0,getHeight(pic),1):
      #get the pixel
      p = getPixel(pic,x,y)
      #get the color of the pixel
      color = getColor(p)
      #set the new x and y values
      x2 = getHeight(pic)-1-y
      y2 = x
      #make a new pixel
      p2 = getPixel(pic2,x2,y2)
      #set the color of the pixel
      setColor(p2,color)
 
  #show the new pic
  show(pic2)
  #save new pic to a file on machine
  file2 = pickAFile()
  writePictureTo(pic2,file2)

#rotate the picture 180 degrees
def rotate180(pic):
  #make an empty picture for the new picture
  pic2 = makeEmptyPicture(getWidth(pic), getHeight(pic))
  #loops for all pixels
  for x in range(0,getWidth(pic),1):
    for y in range(0,getHeight(pic),1):
      #get the pixel
      p = getPixel(pic,x,y)
      #get the color of the pixel
      color = getColor(p)
      #set the new x and y values
      x2 = getWidth(pic)-1-x
      y2 = getHeight(pic)-1-y
      #make a new pixel
      p2 = getPixel(pic2,x2,y2)
      #set the color of the pixel
      setColor(p2,color)
      
  #show the new pic
  show(pic2)
  #save new pic to a file on machine
  file2 = pickAFile()
  writePictureTo(pic2,file2)

#rotate the picture 270 degrees
def rotate270(pic):
  #make an empty picture for the new picture
  pic2 = makeEmptyPicture(getHeight(pic), getWidth(pic))
  #loops for all pixels
  for x in range(0,getWidth(pic),1):
    for y in range(0,getHeight(pic),1):
      #get the pixel
      p = getPixel(pic,x,y)
      #get the color of the pixel
      color = getColor(p)
      #set the new x and y values
      x2 = y
      y2 = getWidth(pic)-1-x
      #make a new pixel
      p2 = getPixel(pic2,x2,y2)
      #set the color of the pixel
      setColor(p2,color)
 
  #show the new pic
  show(pic2)
  #save new pic to a file on machine
  file2 = pickAFile()
  writePictureTo(pic2,file2)

#based on the integer picked, run the specific function for that integer
if value == 1:
  #if integer is 1, run rotate90
  rotate90(picture)
elif value == 2:
  #if integer is 2, run rotate180
  rotate180(picture)
elif value == 3:
  #if integer is 3, run rotate270
  rotate270(picture)