#Eivydas Raulynaitis
#erauly2
#Monday @ 5pm
#i had to change the volume of a sound based on the integer percent value entered by the user

#pick a file and make it into a sound
file = pickAFile()
sound = makeSound(file)

#request a percent integer from the user, using float for numbers less than 100
integer = float(requestInteger("Enter an integer percent value:"))

#this function modifies the volume of the sound based on the integer percent entered by the user
#the audio is the sound and the percent is the integer value entered
def modifySound(audio,percent):
  #make a sample list from the sound
  samplelist = getSamples(audio)
  #convert the integer into a percentage value
  value = percent/100
  
  #loop through all the samples of the sound
  for i in range(0,getLength(audio),1):
    #edit the current sample in the loop
    soundsample = samplelist[i]
    #get the amplitude of the sample
    amplitude = getSampleValue(soundsample)
    #make a new amplitude based on the percent, changing volume
    amplitude2 = amplitude*value
    
    #check to make sure the new amplitude is within limits so it doesn't clip
    if (amplitude2 > 32767):
      amplitude2 = 32767
    elif (amplitude2 < -32767):
      amplitude2 = -32767
    
    #set the new amplitude to the sample, changing the volume
    setSampleValue(soundsample,amplitude2)
  
  #explore the audio
  explore(audio)
  #request a file for the new sound to be written to
  writeSoundTo(audio,pickAFile())
  
#run the function
modifySound(sound,integer)