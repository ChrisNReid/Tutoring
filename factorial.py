# factorial of 5 = 5*4*3*2*1
# factorial of 3 = 3*2*1
# ask for input
# find factorial and output

number = int(input("Enter a number :"))
factorial = 1
for i in range(number, 0, -1):
    factorial = factorial * i

print("factorial of ", number, "is: ", factorial)

# Factorial
# factorial of 4 = 4!
# 4*3*2*1 = 24
# 5!
# 5*4*3*2*1 = 120

# ask for input
#calculate factorial of input
#loop until factorial is reached (include input)
#multiplying each number
result = 1
number = int(input("Enter a number :"))
for i in range(1, number + 1):
    result = i * result
    print(i, "*", result)
print(result)

# 1*1 = 1
# 2*1 = 2
# 3*2 = 6
# 4*6 = 24

# for i in range 4
#  go up until i < 4
#   its gonna finish at 3
