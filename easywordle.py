#Make wordle
#a list of words
#computer randomly choses a word from our list
#allows us to guess
#loop through guess array, if a letter matches in our word array
#print how many matches they have
import random

words = ["CARGO", "CRANE", "SMALL", "LARGE"]
randnum = random.randint(0,len(words)-1) # because len starts counting at 1
word = (words[randnum])
wordarr = list(word)
print(wordarr)

rawguess = input("enter your guess")
guess = rawguess.upper()

print(guess)
guessarr = list(guess)
print(guessarr)

#counter for going through arrays
i = 0
#count is to return how many letter matches we have
count = 0
#list of letters gone through, so it ignored duplicate counting
dups=[]
#a loop to go through the whole answer word
for i in range(0, len(guessarr)-1):
#if a letter in guess exists in the answer word
  if guessarr[i] in wordarr:
  #if that letter has not been gone through before
    if guessarr[i] not in dups:
      #record as a match
      count = count+1
      #add to letters gone through
      dups.append(guessarr[i])
    

print("You got ", count, "matching letters")
    



  
