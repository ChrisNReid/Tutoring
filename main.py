# Create a program that takes two strings/words. Then then converts this to an ASCII value and subtracts the values from each other.
# Extension:
# 1. Also add a function that removes any characters in the second word that occur in the first word. E.g. Fish and Tin, would return “Fsh” and “T

word1=input("Enter a word :")
word2=input("Enter another word:")
word1arr = []
word2arr = []
finalarr = []
diffarr = []
# find the ascii numbers of each letter for word 1 
# put in array
for i in range(0,len(word1)):
  word1arr.append(ord(word1[i]))
print(word1arr)

# find the ascii numbers of each letter for word 2
# put in array
for i in range(0,len(word2)):
  word2arr.append(ord(word2[i]))
print(word2arr)

# subtract each ascii value from the second words ascii value to give a new integer
# print this letter
for i in range(0,len(word1)):
    diff = abs(word1arr[i] + word2arr[i])
    finalarr.append(diff)

print(finalarr)
for i in range(len(finalarr)):
  letter = chr(finalarr[i])
  diffarr.append(letter)
print(diffarr)