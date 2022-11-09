#Hangman
# Create a version of the Hangman game using Lists. The program should ask for the word to guess and the number of chances to be given
#For every guess you should update the user with which letters they have guessed incorrectly, as well as replacing the letters in the guess word with the ones they have guessed correctly.
#You should also show the user how many chances they have left.

word=input("Enter the word to guess: ")
chances=input("Enter how many chances should be given: ")

guess = []
for i in range(len(word)):
  guess.append("_ ")

print(guess)
count = 0
usrguess = ""
while count <= 10 and usrguess != word:
  #enter user guess
  #if guess correct
    #add letter to guess array
  # if not
    #tell them incorrect
  
  #count increases
  