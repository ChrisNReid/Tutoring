#Theif
#write a program that displays all possible combination of 4 digits
number1=input("Enter a number :")
number2=input("Enter a second number :")
number3=input("Enter a third number :")
# number4=input("Enter a fourth number :")

array=[]
array.append(number1)
array.append(number2)
array.append(number3)

#array = [1,2,3,4]

for i in range(len(array)):
  for j in range(len(array)):
    for k in range(len(array)):
        if i!=j and i!=k and j!=k:
          print(array[i], array[j], array[k])

#scale up
#make it a function that accepts a list