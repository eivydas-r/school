#Eivydas Raulynaitis
#erauly2
#Monday @ 5pm
#i had to combine two sounds together, one foreground and one background, with the background quieter than the foreground, also making the background sound repeat to fir the foreground

#pick and make the foreground sound
file1 = pickAFile()
sound1 = makeSound(file1)

#pick and make the background sound
file2 = pickAFile()
sound2 = makeSound(file2)

#get the samples of both of the sounds
samples1 = getSamples(sound1)
samples2 = getSamples(sound2)

#this function combines both of the audios together, making one sound
#the parameters are both of the sounds
def combineSounds(audio1,audio2):
  #loop every sample for the foreground audio
  for i in range(0,getLength(audio1),1):
    #get the value of the foreground sample
    value1 = getSampleValue(samples1[i])
    #get the value of the background sample and make it 1/3 of the volume, also making the sound repeat so it fits the first audio
    value2 = (getSampleValue(samples2[i%getLength(audio2)]))/3
    #add both sound values together to make the final value
    value3 = value1 + value2
  
    #check to make sure the new amplitude is within limits so it doesn't clip
    if (value3 > 32767):
      value3 = 32767
    elif (value3 < -32767):
      value3 = -32767
    
    #set the new sound value to the first audio
    setSampleValue(samples1[i],value3)
  
  #explore the changed sound
  explore(audio1)
    
#run the function to combine the sounds
combineSounds(sound1,sound2)