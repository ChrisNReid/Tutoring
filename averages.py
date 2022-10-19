# ask the user for a series of numbers until they want to find the average or quit
# when we know how many loops needed = for loops
# when we dont know the limit = while

again = True
#  create an empty array, called array
array = []

# a while loop that repeats as long as again = true
while again == True:
# ask for a user input, restricted to integers only
  number = int(input("Enter a number: "))
# add the user inputted number to the array
  array.append(number)
# asking the user for input, if they want to eneter another number
  choice = input("would you like to enter another number (y/n): ")

# checking if the user wants to enter another number, if not, stop looping
  if choice == 'n':
    again = False

print(array)

# go through each number in array and sum them together
# sum starts at zero
sum = 0

# looping through all numbers between begining and end of array
for i in range(0,len(array)):
# summing each item in array to a running total called sum
  sum  = sum + array[i]
# finding our average of sum total divided by how many numbers in our array
average = sum / len(array)

print("average = ", average)

# print the middle number that the user entered.. if they enetred 6 numbers, print the 3rd... if 10 numbers, print 5th.

# middle number is equal to half the length of the array.e.g. half of 6 numbers in array is 3
middle = len(array)/2

print("middle number = ", middle)

