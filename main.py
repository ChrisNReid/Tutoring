#Count words in a string
#hello world this is a sentence
def easy():
  sentence=input("Write your sentence:")
  sentenceSplit = sentence.split()
  print(len(sentenceSplit))

def hard():
  sentence=input("Write your sentence:")
  sentenceList= list(sentence)
  print(sentenceList)
  count = 1
  for i in range (len(sentenceList)):
    if sentenceList[i] == " ":
      count = count + 1
  
  print(count)

def pigLatin():
  #Pig Latin converter
  array =[]
  words = input("enter a sentence: ")
  wordsSplit = words.split()
  for word in wordsSplit:
    newword = word[1:] + word[0] +"ay"
    print(newword)
    array.append(newword)
  print(array)
  print(" ".join(array))

