#palindrome checker
#a word that is the same forewards as backwards

#enter a word
#to get the word backwards
#check the inputted is the same as the backwards version


   

def hard():
  word = input("Enter a word:")
  forwardWord = list(word)
  
  #go through list backwards (length-1, to the first element, backwards)
  backwardsWord = []
  for i in range (len(forwardWord)-1, -1,-1):
    backwardsWord.append(forwardWord[i])
  
  if forwardWord == backwardsWord:
    print("this is a palindrome")
  else:
      print("this is not a palindrome")

  
def easy():
  forwardsWord= input("Enter a word:")
  #[::1] is forewards, [::-1] backwards
  backwardsWord = forwardsWord[::-1]
  
  # print(forwardsWord)
  # print(backwardsWord)
  
  if forwardsWord == backwardsWord:
    print("this is a palindrome")
  else:
      print("this is not a palindrome")
 