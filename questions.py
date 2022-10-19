print("Question Game")
print("----------------")

#  array of the correct answers, call the item in the array to check if user input is the same as item in array

answers =  [ ["Pacific", "1"],
              ["Arctic","3"],
              ["London", "1"],
              ["8%","2"],
              ["Vatican City", "2"]
]
# Question 1
correctAnswer = 0
largestOcean = "What is the largest ocean?"


print (largestOcean)

print("option 1: Pacific")
print("option 2: Atlantic")
print("option 3: Indian")

answer = input ("Write your answer here.")

if answer == answers[0][0] or answer == answers[0][1]:
  print ("Correct")
  correctAnswer += 1
#  elif answer == "2":
  # print ("Correct")
else:
  print ("Incorrect, it's the Pacific")

# Question 2

smallestOcean = "What is the smallest ocean?"
print("option 1: Pacific")
print("option 2: Atlantic")
print("option 3: Arctic")

print (smallestOcean)

answer = input ("Write your answer here.")

if answer == answers[1][0] or answer == answers[1][1]:
  print ("Correct")
  correctAnswer = correctAnswer + 1
#  elif answer == "2":
  # print ("Correct")
else:
  print ("Incorrect, it's the Arctic")


# Question 3

capital1 = "What is the capital of the UK?"


print (capital1)
print("option 1: London")
print("option 2: Berlin")
print("option 3: England")


answer = input ("Write your answer here.")

if answer == answers[2][0] or answer == answers[2][1]:
  print ("Correct")
  correctAnswer = correctAnswer + 1

else:
    print ("Incorrect, it's London")

# Question 4


question4 = "What percentage of the UK is made up by cities?"

print (question4)
print("option 1: 100%")
print("option 2: 8%")
print("option 3: 12%")

answer = input ("Write your answer here.")

if answer == answers[3][0] or answer == answers[3][1]:
  print ("Correct")
  correctAnswer = correctAnswer + 1

else:
    print ("Incorrect, it's 8%")

# Question 5

small = "What is the smallest country"

print (small)

print("option 1: Rome")
print("option 2: Vatican City")
print("option 3: Madagascar")

answer = input ("Write your answer here.")

if answer == answers[4][0] or answer == answers[4][1]:
  print ("Correct")
  correctAnswer = correctAnswer + 1

else:
    print ("Incorrect, it's Vatican City")

print ("You got" , correctAnswer,  "out of 5 correct" )
