# Linear search

# defining a function
def linearSearch():
  array = [5,6,7,3,34,566,9,8,9,100,303,3848]

  # length of array
  # len(array)
  target = 7
  counter = 0

  while counter < len(array):
    if array[counter] == target:
      print('found')
    else:
      print('not found')
    counter = counter + 1


def linearSearch2():
  array = [5,6,7,3,34,566,9,8,9,100,303,3848]

  # length of array
  # len(array)
  target = 7
  counter = 0
  found = False

  while found == False:
    if array[counter] == target:
      print('found')
      found = True
    else:
      print('not found')
    counter = counter + 1



def linearSearch3():
  array = [5,6,7,3,34,566,9,8,9,100,303,3848]

  # length of array
  # len(array)
  target = 7

  for counter in range(0,5):
    if array[counter] == target:
      print('found')
     
    else:
      print('not found')

#  calling or runnning a function
linearSearch3()




#  adding to the end of an 1d array
# array.append(data)
# 2d array
# array.append([data,data])

# adding to a specific location 1d
# array.insert(location, data)
# 2d
# array.insert([row][column], [data,data]) 


array = ["Theo", "Jack", "Noah", "George", "Arthur"]
#  add 5 names into array
array.remove("Jack")
print(array)
array.insert(4, "Harry")
print(array)
array.insert(5, 5)
print(array)
# remove 2nd delattr


# replace 5th with another Name


# add interger 5 to the end of the array

