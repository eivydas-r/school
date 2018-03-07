#eivydas raulynaitis
#monday @ 5pm
#i had to posterize an image to pink shades

# pick an image to use
file = pickAFile()
image = makePicture(file)

# for loop to go through every pixel
def posterize(pic):
  for y in range(1,getHeight(pic),1):
    for x in range(1,getWidth(pic),1):
      pixel = getPixel(pic,x,y)
      
      # get all the colors of the pixel
      r = getRed(pixel)
      g = getGreen(pixel)
      b = getBlue(pixel)
      
      # weigh the colors correctly
      grayAmount = int(r*.299+g*.587+b*.114)
      
      if (grayAmount < 42):
        # set the pixel to medium violet pink
        r = 199
        g = 21
        b = 133
      elif (grayAmount < 84):   
        # set the pixel to deep pink
        r = 255
        g = 20
        b = 147
      elif (grayAmount < 127):
        # set the pixel to violet
        r = 238
        g = 130
        b = 238
      elif (grayAmount < 170):
        # set the pixel to hot pink
        r = 255
        g = 105
        b = 180
      elif (grayAmount < 212):
        # set the pixel to light pink
        r = 255
        g = 182
        b = 193
      elif (grayAmount <= 255):
        # set the pixel to pink
        r = 255
        g = 192
        b = 203
      # make new color
      newColor = makeColor(r,g,b)
      
      # set the new color to the pixel
      setColor(pixel,newColor)
  # show the picture
  show(pic)  

# run the function
posterize(image)  