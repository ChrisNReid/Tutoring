x = 25
print(type(x))

#selection, 
#nested selection = if/else inside andother if/else
if x > 10:
  print("larger than 10")
  if x > 20:
    print("larger than 20")
else:
  print("smaller than 10")



def hi():
  #iteration = loops
  for i in range(0,10):
    print("hi")

#operators
#div and modulo
#DIV = //, divide and do not include remainders
print(7//2)

#MOD = %, divide, only show the remainder of a division
print(7%2)

print("\n")
print("boolean operators, NOT,AND, OR \n")
y = True
z = True
print("y = ", y)
print("z = ", z)

print("NOT y = ",not y)

print("y and z =", y and z)

print("y or z =", y or z)

print("\n DATA STRUCTURES \n")

array = []
for i in range(1,11):
    array.append(i)
print(array)
#array.remove(array[3])
if 4 in array:
  array.remove(4)
print(array)


#length of something
print(len(array))
a = "hello there"
print(len(a))
#substring = a part of a string
msg = a[0:5]
msg2 = a[6:13]
print(msg)
print(msg2)

#concatination = joining multiple strings together
newmsg = msg2 +" "+ msg
print(newmsg)

# ascii
print(ord("A"))
print(chr(206))
#prints all charcter codes
for i in range(0,512):
  print(i, " = ", chr(i))

def func():
  x= 10
  return x

print(" func returned: ",func())