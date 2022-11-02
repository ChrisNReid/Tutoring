
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
