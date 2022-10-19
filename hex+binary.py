  # a program that takes a hexidecimal string input, and converts it to a normal number
def hex():
  hex  = input("Enter a Hexidecimal number ")

  letter1 = hex[0]
  letter2 = hex[1]

  table = [
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
          'E', 'F'
      ]
  # d3
  # (13 * 16) +3

  posletter1 = table.index(letter1)
  posletter2 = table.index(letter2)
  # index = location = address

  final = (posletter1 * 16 + posletter2)
  print(final)

def bin():
  # convert a binary number to a normal number

  binary = input("Enter an 8 bit Binary number ")
  finalcount = 0

  array = [128,64,32,16,8,4,2,1]

  for i in range(0,8):
    if binary[i] == '1':
    
      finalcount = finalcount+ array[i]

  
  print(finalcount)


array = ['1', '1', '0','1']
for i in range(0,4):
  print(array[i])



