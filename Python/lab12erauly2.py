#Eivydas Raulynaitis
#erauly2
#Monday @ 5pm
#i had to take an audio, for the first 3 seconds i had to make the volume increase, the last 3 seconds i had to make the volume decrease, and in between it needed to stay at normal volume

#this function makes a small snippet of audio from an original audio
#parameters: the audio is the sound, start where the new audio will start, and the end is where it will end
def makeSoundByte(audio,start,end):
  #make an empty sound by using the parameters
  newSound = makeEmptySound(end-start)
  #get samples of the audio
  samples1 = getSamples(audio)
  #get samples of the new sound
  samples2 = getSamples(newSound)

  #loop for the range in parameters for selected samples
  for i in range(0,end-start,1):
    #get sample value for selected sample
    value = getSampleValue(samples1[i+start])
    #set sample value to new audio
    setSampleValue(samples2[i],value)

  #return the new sound
  return newSound

#this function changes the volume of the audio inputed based on the integer given
#parameters: audio is the sound given, and the percent is the integer given
def modifyVolume(audio,percent):
  percent = float(percent)
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

#this function combines audios together into one single audio
#parameters: audio1 is the first sound, audio2 is the second sound given
def joinSounds(audio1,audio2):
  #get samples for both sounds
  samples1 = getSamples(audio1)
  samples2 = getSamples(audio2)

  #get the length of both sounds
  length1 = getLength(audio1)
  length2 = getLength(audio2)

  #make a new sound that'll fit both the given audio lengths
  newSound = makeEmptySound(length1+length2)
  #get samples from the new sound
  newSamples = getSamples(newSound)

  #set a starting position
  pos = 0
  #loop for applying samples from first sound to the new sound
  for i in range(0,length1,1):
    #get sample value for selected sample
    value = getSampleValue(samples1[i])
    #set sample value to new audio
    setSampleValue(newSamples[pos],value)
    #update the position
    pos = pos + 1

  #loop for applying samples from second sound to the new sound
  for j in range(0,length2,1):
    #get sample value for selected sample
    value = getSampleValue(samples2[j])
    #set sample value to new audio
    setSampleValue(newSamples[pos],value)
    #update the position
    pos = pos + 1

  #return the new sound
  return newSound

#this is the main function of the program, it will run everything that's needed to make the program work
def main():
  #request a file and make it into a sound
  file = pickAFile()
  sound = makeSound(file)

  #get the sampling rate from the sound
  rate = int(getSamplingRate(sound))
  #get the length of the sound
  length = getLength(sound)

  #if the sound is less than 6 seconds, run an error
  if (getLength(sound) < rate*6):
    #run error message
    print("Error: the sound is less than 6 seconds long, try again")
    #run main again to retry
    main()

  #make sound byte for first second
  byte1 = makeSoundByte(sound,0,(rate*1))
  #make sound byte for second second
  byte2 = makeSoundByte(sound,(rate*1),(rate*2))
  #make sound byte for third second
  byte3 = makeSoundByte(sound,(rate*2),(rate*3))
  #make sound byte for audio between the first and last 3 seconds
  byte4 = makeSoundByte(sound,(rate*3),length-(rate*3))
  #make sound byte for x-3 second
  byte5 = makeSoundByte(sound,length-(rate*3),length-(rate*2))
  #make sound byte for x-2 second
  byte6 = makeSoundByte(sound,length-(rate*2),length-(rate*1))
  #make sound byte for x(last) second
  byte7 = makeSoundByte(sound,length-(rate*1),length)

  #change all the volumes so that they're 1/4, 1/2, 1/3, and normal volume respectively
  modifyVolume(byte1,25)
  modifyVolume(byte2,50)
  modifyVolume(byte3,75)
  modifyVolume(byte4,100)
  modifyVolume(byte5,75)
  modifyVolume(byte6,50)
  modifyVolume(byte7,25)

  #combine all the changed bytes into one final sound
  newSound1 = joinSounds(byte1,byte2)
  newSound2 = joinSounds(newSound1,byte3)
  newSound3 = joinSounds(newSound2,byte4)
  newSound4 = joinSounds(newSound3,byte5)
  newSound5 = joinSounds(newSound4,byte6)
  finalSound = joinSounds(newSound5,byte7)

  #explore the final sound
  explore(finalSound)

#run the main function that'll run the whole program
main()
