# Years in a Range
# Write a program to count the number years in a range that has a repeated digit.
# For example, 2012 has a repeated digit, but 2013 does not

year = input("Enter a year :")
repeated = False

# array = list(year)
# print(array)

for i in range (4):
   if year.count(year[i]) > 1:
     repeated = True

if repeated == True:
  print(year, " has a repeated digit")
else:
    print(year, " has no repeated digits")

