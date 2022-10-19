

# for i in range (10):
#   number=int(input("Enter a number: "))
#   if number > 70:
#     number = str(number)
#     number = number + "\n"
#     f=open("textfile.txt","a")
#     f.write(number)
#     f.close()

# f=open("textfile.txt","r")
# print(f.read())
# f.close()

# import random
# for i in range(30):
#   number = random.randint(0,150)
#   number = str(number)
#   number = number + "\n"
#   f=open("textfile.txt","a")
#   f.write(number)
#   f.close()

# f = open("textfile.txt", "r")
# for line in f:
#   number = int(line)
#   if number > 70:
#     print(number)


#use Time for speeds

    
from time import time, ctime
import time
start = time.time()
time.sleep(3)
end  = time.time()
finaltime = end-start
print(finaltime)

t= time()
ctime(t)

