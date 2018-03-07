#eivydas raulynaitis
#erauly2
#10/27/17
#combine two images to make a 3D effect

#promp user for two pictures
file1 = pickAFile()
file2 = pickAFile()

#create two pictures
pic1 = makePicture(file1)
pic2 = makePicture(file2)

#tint the image to a red-scale
def tintRed(pic):
  #for every pixel
  for x in range(0,getWidth(pic),1):
    for y in range(0,getHeight(pic),1):

      p = getPixel(pic,x,y)
      #get the color values of the pixel
      r = getRed(p)
      g = getGreen(p)
      b = getGreen(p)
      
      #weigh the colors into a grayscale
      avg = int(r*.299+g*.587+b*.114)
      
      #set the new color values to the image
      setRed(p,avg)
      setGreen(p,0)
      setBlue(p,0)

#tint the image to a blue-scale
def tintBlue(pic):
  #for every pixel
  for x in range(0,getWidth(pic),1):
    for y in range(0,getHeight(pic),1):
      #get the pixel
      p = getPixel(pic,x,y)
      #get the color values of the pixel
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      
      #weigh the colors into a grayscale
      avg = int(r*.299+g*.587+b*.114)
      
      #set the new color values to the image
      setRed(p,0)
      setGreen(p,avg)
      setBlue(p,avg)

def combine3D():
  #for every pixel
  for x in range(0,getWidth(pic2),1):
    for y in range(0,getHeight(pic2),1):
      #get the pixels
      p1 = getPixel(pic1,x,y)
      p2 = getPixel(pic2,x,y)
      #get the color values of the pixels and weigh them
      r = (getRed(p1)+getRed(p2))
      g = (getGreen(p1)+getGreen(p2))
      b = (getBlue(p1)+getBlue(p2))
      
      #set the new color values to the new image
      setRed(p2,r)
      setGreen(p2,g)
      setBlue(p2,b)
      
#check to see if the images are the same height
if (getHeight(pic1) == getHeight(pic2)):
  #check to see if the images are the same width
  if (getWidth(pic1) == getWidth(pic2)):
    #if the same size, run the functions
    tintRed(pic1)
    tintBlue(pic2)
    combine3D()
    #show image
    show(pic2)
  else:
    #if not the same width, print error
    print("The images are not the same size, close JES.")
else:
  #if not the same height, print error
  print("The images are not the same size, close JES.")



