#eivydas raulynaitis
#erauly2
#monday @ 5pm
#i had to duplicate an image based on a value given

#request an integer between 1 and 10
value = requestIntegerInRange("How many times do you want to duplicate the image? Pick between 1-10",1,10)
#print the value
print("User entered: " + str(value))

#pick a picture to be duplicated
file = pickAFile()
#turn file into a picture
pic = makePicture(file)

#function that duplicates the image
#parameters are the integer amount entered and picture used
#the return value sends the new duplicated image
#this function duplicates an image and makes it into one big new image
def duplicateImage(picture,amount):
  #get the height of the picture
  height = getHeight(picture)
  #get the width of the picture
  width = getWidth(picture)
  #make a new empty image that'll fit duplicates
  newImage = makeEmptyPicture(width,height*amount)
  
  #loop for the number entered
  for loop in range(0,amount,1):
    #loop for x values
    for x in range(1,width,1):
      #loop for y values
      for y in range(1,height,1):
        #get the current pixel
        pixel = getPixel(picture,x,y)
        #get the color from the pixel
        color = getColor(pixel)
        #get the new pixel
        pixel2 = getPixel(newImage,x,y+(height*loop))
        #set the color of the new pixel
        setColor(pixel2,color)
        
  #return the new image
  return newImage

#run the duplication function and set the returned image to a variable
image2 = duplicateImage(pic,value)
#show the new image
show(image2)

#pick a file to write the image to
file2 = pickAFile()
#write the image into the file
writePictureTo(image2,file2)