
#user inputs radius
# program outputs area, circumference, volume of sphere
import math
radius = float(input("Enter a radius:"))

pi = math.pi

area = pi*(radius**2)
circum = 2*pi*radius
volume = (4*pi*(radius**3))/3

print("The area is: ", area)
print("The circumference is: ", circum)
print("The volume is:", volume)


#(3a x 4c)(3a x b)
#9a2 + 3ab +12ac + 4cb