
def countVowels():
  #Count Vowels in a text
  sentence1=input("Write your sentence:")
  array = ["a","e","i","o","u"]
  count1 = 0
  for i in range(len(sentence1)):
    if sentence1[i] in array:
      count1 = count1 + 1
  print(count1)

  
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
