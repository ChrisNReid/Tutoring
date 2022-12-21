# factorial of 5 = 5*4*3*2*1
# factorial of 3 = 3*2*1
# ask for input
# find factorial and output

number=int(input("Enter a number :"))
factorial = 1
for i in range(number,0,-1):
  factorial = factorial*i

print("factorial of ", number, "is: ",factorial)

