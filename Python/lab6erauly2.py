#eivydas raulynaitis
#monday @ 5pm
#in this project i had to make two functions that change the color of a picture accordingly

# function for making a black-green image
def makeBlackGreen():
  print'eivydas raulynaitis, erauly2'
  # pick an image to use
  file = pickAFile()
  pic = makePicture(file)
  # for loop to go through every pixel
  for y in range(1,getHeight(pic),1):
    for x in range(1,getWidth(pic),1):
      pixel = getPixel(pic,x,y)
      # get all the colors of the pixel
      r = getRed(pixel)
      g = getGreen(pixel)
      b = getBlue(pixel)
      
      # weigh the colors correctly
      color = int((r*.299)+(g*.567)*(b*.114))
      
      # set the different colors
      setRed(pixel,0)
      setGreen(pixel,color)
      setBlue(pixel,0)
  # show the image
  show(pic)
  # prompt to save the new image
  save = pickAFile()
  # save the image to selected file
  writePictureTo(pic,save)

# function for making a green-white image
def makeGreenWhite():
  print'eivydas raulynaitis, erauly2'
  file = pickAFile()
  # pick an image to use
  pic = makePicture(file)
  # for loop to go through every pixel
  for y in range(1,getHeight(pic),1):
    for x in range(1,getWidth(pic),1):
      pixel = getPixel(pic,x,y)
      # get all the colors of the pixel
      r = getRed(pixel)
      g = getGreen(pixel)
      b = getBlue(pixel)
      
      # weigh the colors correctly
      color = int((r*.299)+(g*.567)*(b*.114))
      
      # set the different colors
      setRed(pixel,color)
      setGreen(pixel,255)
      setBlue(pixel,color)
  # show the image
  show(pic)
  # prompt to save the new image
  save = pickAFile()
  # save the image to selected file
  writePictureTo(pic,save)
  
# run the functions
makeBlackGreen()
makeGreenWhite()