#Eivydas Raulynaitis
#erauly2
#Monday @ 5pm
#i had to take the preamble sound and construct a new sentence using the words from the preamble audio


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
  

#this function combines audios together into one single audio
#parameters: audio1 is the first sound, audio2 is the second sound given
def join(audio1,audio2):
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
  
#this function makes separate words and puts them together to make the correct sentence
def main():
  #pick a file and make it into sound
  file = pickAFile()
  sound = makeSound(file)
  
  #make sound bytes of the words needed using their locations
  first = makeSoundByte(sound,18742,29767)
  second = makeSoundByte(sound,101363,116027)
  third = makeSoundByte(sound,58653,64386)
  fourth = makeSoundByte(sound,64386,67561)
  fifth = makeSoundByte(sound,174240,185130)
  sixth = makeSoundByte(sound,116027,132829)
  
  #join the words together to make the final sentence
  part1 = join(first,second)
  part2 = join(part1,third)
  part3 = join(part2,fourth)
  part4 = join(part3,fifth)
  final = join(part4,sixth)
  
  #explore the sound
  explore(final)
  #write the sound to a file
  writeSoundTo(final,pickAFile())
  
#run the main function
main()