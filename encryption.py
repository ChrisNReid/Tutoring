
def easy(sentence):

  for i in range(0, len(sentence)):
    word = sentence[i]
  #[::1] is forewards, [::-1] backwards
    backwardsWord = word[::-1]
  
  # print(forwardsWord)
    print(backwardsWord)
  
 

def encryption():

  sentence = input("enter a sentence ")
  revsent = sentence[::-1]
  print(revsent)
  
  listsent = sentence.split()

  easy(sentence)
  print(listsent)







encryption()