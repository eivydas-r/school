#Eivydas Raulynaitis
#erauly2
#CS 111
#Project 4
#Monday @ 5pm
#in this project i had to embed a message into a sound and then extract the message out

#purpose: this function embeds a message chosen by the user into a sound chosen by the user
#parameters: for this function i used no parameters
#return: for this function i did not return a value
def embed():
  print("Embedding...")
  
  #request a file and make it into a sound
  file = pickAFile()
  sound = makeSound(file)
  
  #get the legnth of the sound
  length = getLength(sound)
  #get the samples from the sound
  samples = getSamples(sound)
  
  #loop through every sample
  for i in range(0,length,1):
    #get the current sample
    sample = samples[i]
    #get the amplitude of the sample
    amplitude = getSampleValue(sample)
    #mod the amplitude
    smooth = amplitude % 128
    #smooth the sound
    amplitude2 = amplitude - smooth
  
  #request the user for the message that'll be embedded
  string = requestString("Message to embed:")

  #loop through every letter in the string
  for i in range(0,len(string),1):  
    #get the current sample
    sample = samples[i]
    #get the amplitude
    amplitude = getSampleValue(sample)
    #embed the ASCII value into the amplitude
    amplitude2 = amplitude + ord(string[i])
    #set the sample value to new amplitude
    setSampleValue(sample,amplitude2)

  #save the new embedded sound to a file
  writeSoundTo(sound,pickAFile())  
  print("Embedding complete")

#purpose: the purpose of this function is to extract a message out of the selected sound and show it
#parameters: for this function i used no parameters
#return: for this function i did not return a value
def extract():
  print("Extracting...")
  
  #request a file and make it into a sound
  file = pickAFile()
  sound = makeSound(file)
  
  #get the legnth of the sound
  length = getLength(sound)
  #get the samples from the sound
  samples = getSamples(sound)
  
  #make an empty string
  string = ''

  #loop through every sample
  for i in range(0,length,1):
    #get the current sample
    sample = samples[i]
    #get the amplitude
    amplitude = getSampleValue(sample)
    #find the embedded value
    amplitude2 = amplitude % 128
    #add the character into the string
    string = string + chr(amplitude2)

    #if there's no more embedded code, end the loop
    if (amplitude2 < 1):
      break

  #show the extracted message to the user
  showInformation(string)


#let user decide wether to embed or extract a messsage
choice = requestIntegerInRange("Enter 1 to embed, 2 to extract:",1,2)

#if choice is 1, run embed function
if (choice == 1):
  embed()
#if choice is 2, run extract function
else:
  extract()