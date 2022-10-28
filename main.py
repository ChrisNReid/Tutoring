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

def countVowels():
  #Count Vowels in a text
  sentence1=input("Write your sentence:")
  array = ["a","e","i","o","u"]
  count1 = 0
  for i in range(len(sentence1)):
    if sentence1[i] in array:
      count1 = count1 + 1
  print(count1)

#Unit Converter
beginUnit = input("enter the unit being converted (celcius/..)")
beginValue = int(input("enter beginning value: "))
endUnit = input("enter the final unit (fahrenheit/..)")

if beginUnit == "celcius" and endUnit == "fahrenheit":
  endValue = (beginValue * 1.8) + 32
  print(endValue)
