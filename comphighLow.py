#computer plays higher or lower with itself
import random
answer = int(input("enter a number 1-100: "))

#setting starting values for the range
compguess = 0
min = 1
max = 100
counter = 0
#loops untill guess is correct
while compguess != answer:
  compguess = random.randint(min,max)
  print("guess is : ",compguess)
  counter = counter + 1
  # if the answer is bigger,  increase our minimun guess to 1 higher than previous guess
  if answer > compguess:
    print("Higher")
    min  = compguess + 1
    
#if answer is lower, then max guess should be lower than previous guess
  elif answer < compguess:
    print("Lower")
    max = compguess - 1

  else:
    print("correct answer")
    print("It took you", counter, "tries")