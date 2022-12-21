#Hangman
# Create a version of the Hangman game using Lists. The program should ask for the word to guess and the number of chances to be given
#For every guess you should update the user with which letters they have guessed incorrectly, as well as replacing the letters in the guess word with the ones they have guessed correctly.
#You should also show the user how many chances they have left.

word=input("Enter the word to guess: ")
chances=int(input("Enter how many chances should be given: "))

guess = []
attempts = []
for i in range(len(word)):
  guess.append("_ ")
print(guess)

count = 1
usrguess = ""
while (count <= chances) and (usrguess != word):
  print(guess)
  #enter user guess 
  usrguess=input("Enter a letter to guess:")
  
  #if they guess the whole word correct
  #appropriate print msg
  #leave the loop
  if usrguess == word:
    print("word correct")
    print("you go it in ",count, " goes")
    count += 1
    break

  #if they have already guessed the letter
  #checks correct and incorrect guess arrays
  elif (usrguess in guess) or (usrguess in attempts):
    print("you have already guessed this letter")
    
  #if they guess t=a correct letter
  #loop through correct word, if there usrguess is in word
  # replace empty underscore with the correct letter they guessed
  # increase count
  elif usrguess in word:
    for i in range(0, len(word)):
      if usrguess == word[i]:
        guess[i] = word[i]
    print("correct letter")
    count += 1

  #if incorrect, print msg
  # add usrguess to incorrect array
  # increase count
  else:
    print("not present")
    attempts.append(usrguess)
    count += 1
  #count increases
  