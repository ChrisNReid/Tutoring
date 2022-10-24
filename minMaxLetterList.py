def minMax():
#Min Max list
  list = []
  max = 0
  min = 10000000000000000000000
  
  minLimit = int(input("what is the minimum entry"))
  maxLimit = int(input("what is the maximum entry"))
  
  
  for i in range(5):
    
    number = int(input("enter a number: "))
    if number > minLimit and number < maxLimit:
      list.append(number)
    
      if number > max:
        max = number
      if number < min:
        min = number
      print("Min: " ,min)
      print("Max: " ,max)
      print("\n")
  print(list)

def LetterList():
  list = ['Hello', 'Geeks', 'for', 'geeks']
  letter = input("enter a letter: ")

  for i in range (len(list)):
    word = list[i]
    print("starts with letter")
    if word[0] == letter.upper() or word[0] == letter.lower() :
      print(list[i])
    print("containing letter")
    for j in word:
      if j == letter.upper() or j ==letter.lower():
         print(list[i])
      
LetterList()


