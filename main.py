#Program that finds the largest element in a list

#input a list
#loop through
#and compare each time to the previous highest number

list = []
for i in range(5):
    number = int(input("Enter a number :"))
    list.append(number)

print(list)

max = 0
for i in range(len(list)):
    if max > list[i]:
        max = max
    else:
        max = list[i]

print("the biggest number is: ", max)
