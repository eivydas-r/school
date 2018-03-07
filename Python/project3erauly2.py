#Eivydas Raulynaitis
#erauly2
#Monday @ 5pm
#i had to make a collage of pictures that represented a flag visually, while using 3 different image manipulation techniques
#the flag i chose to make is the russian flag

#hard coding so only need to pick a file once
folder = pickAFile()
#need two slashes because one escapes the quote
directorypos = folder.rfind("\\")
#if statement to see if running on a mac or a PC
if (directorypos == -1):
  directorypos = folder.rfind("/")

#moves up a directory
dirname = folder[0:directorypos+1]

#a picture of a bear, known largely as russia's animal
whiteimage = dirname + "bear.jpg"
#a picture of the prodiment city in russia, moscow
blueimage = dirname + "moscow.jpg"
#a picture of the president of russia, vladimir putin, winking ;)
redimage = dirname + "putin.jpg"

#makes three pictures based on the images picked
picA = makePicture(whiteimage)
picB = makePicture(blueimage)
picC = makePicture(redimage)


#this function makes the white portion of the flag, using the bear image
#the bear image is simply manipulated so that it is given a white hue
def makeWhite(pic):
  #run through all pixels of image
  for x in range(0,getWidth(pic),1):
    for y in range(0,getHeight(pic),1):
      #get the pixel
      p = getPixel(pic,x,y)
      
      #weigh the colors of the pixel
      avg = int(getRed(p)*.299+getGreen(p)*.587+getBlue(p)*.114)
      #use the avg to make the new color
      color = makeColor(avg*4,avg*4,avg*4)
      
      #set the color to the pixel
      setColor(p,color)
  #return the picture
  return pic


#posterize image into blue shades based on average greyscale value
#this function makes a pictue of moscow into different shades of blue by using posterization
def makeBlue(pic):
  #run through all pixels of image
  for x in range(0,getWidth(pic),1):
    for y in range(0,getHeight(pic),1):
      #get the pixel
      p = getPixel(pic,x,y)
      
      #for this function we need the r,g,b values specifically, get those values
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      
      #weigh the colors of the pixel
      avg = int(r*.299+g*.587+b*.114)
      
      #to posterize, we check if the weighted color is less bright than a color, if it is, then we set to new r,g,b values
      #setting colors to different shades of blue
      if (avg < 40):
        r = 0
        g = 102
        b = 204
      elif (avg < 80):
        r = 33
        g = 144
        b = 255
      elif (avg < 150):
        r = 66
        g = 151
        b = 237
      elif (avg < 250):
        r = 81
        g = 161
        b = 247
      #if not any of the others, make it this shade
      else:
        r = 123
        g = 182
        b = 242
        
      #making the new color using r,g,b
      color = makeColor(r,g,b)
      
      #setting the pixel to the new color
      setColor(p,color)
  #return the picture
  return pic


#this function makes the red portion of the flag
#the pictue of putin is mirrored and then given a red hue
def makeRed(pic):
  #make an empty picture
  pic2 = makeEmptyPicture(getWidth(pic),getHeight(pic))
  #run through all pixels of image
  for x in range(0,getWidth(pic),1):
    for y in range(0,getHeight(pic),1):
      #get the pixel
      p = getPixel(pic,x,y)
      #get the pixel of the empty picture, but get the mirrored position
      p2 = getPixel(pic2,getWidth(pic)-x-1,y)
      
      #weigh the colors of the pixel
      avg = int(getRed(p)*.299+getGreen(p)*.587+getBlue(p)*.114)
      #use the avg to make a new color
      color = makeColor(avg*2,0,0)
      
      setColor(p2,color)
  #return the picture
  return pic2


#this function combines all of the new manipulated images into one
#the function also crops the image so it fits the flag
def combineImages(pic1,pic2,pic3):
  #make a new empty picture, for this i made the flag 500x300 pixels
  newpic = makeEmptyPicture(500,300)
  #make the white picture
  whitepic = makeWhite(pic1)
  #nake the blue picture
  bluepic = makeBlue(pic2)
  #make the red picture
  redpic = makeRed(pic3)
  
  #combine white picture
  #for all x pixels of empty pic, and a third of the y pixels
  for x in range(0,getWidth(newpic),1):
    for y in range(0,getHeight(newpic)/3,1):
      #get the pixel
      p = getPixel(newpic,x,y)
      #get the pixel of the manipulated picture and crop it
      p2 = getPixel(whitepic,x,y+getHeight(whitepic)/4)
      
      #get the color of the manipulated picture
      newcolor = getColor(p2)
      #set the empty picture color to the manipulated picture
      setColor(p,newcolor)
  
  #combine blue picture
  #for all x pixels of empty pic, and a third of the y pixels
  for x in range(0,getWidth(newpic),1):
    for y in range(0,getHeight(newpic)/3,1):
      #get the pixel
      p = getPixel(newpic,x,y+getHeight(newpic)/3)
      #get the pixel of the manipulated picture and crop it
      p2 = getPixel(bluepic,x,y+getHeight(bluepic)/3)
      
      #get the color of the manipulated picture
      newcolor = getColor(p2)
      #set the empty picture color to the manipulated picture
      setColor(p,newcolor)
  
  #combine red picture
  #for all x pixels of empty pic, and a third of the y pixels
  for x in range(0,getWidth(newpic),1):
    for y in range(0,getHeight(newpic)/3,1):
      #get the pixel
      p = getPixel(newpic,x,y+2*(getHeight(newpic)/3))
      #get the pixel of the manipulated picture and crop it
      p2 = getPixel(redpic,x,y+getHeight(redpic)/5)
      
      #get the color of the manipulated picture
      newcolor = getColor(p2)
      #set the empty picture color to the manipulated picture
      setColor(p,newcolor)

  #show the new image
  show(newpic)
  #since saving the image isn't on the requirements, we won't save it


#run the complete function that combines the manipulated images to make a flag
combineImages(picA,picB,picC)