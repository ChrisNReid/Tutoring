
#Unit Converter
def unitconvert():
  beginUnit = input("enter the unit being converted \n Options: \n celcius \n Pound \n Euro \n  ")
  beginValue = int(input("enter beginning value: "))
  endUnit = input("enter the final unit \n Options: \n fahrenheit \n Pound \n Euro \n")
  
  
  if beginUnit == "celcius" and endUnit == "fahrenheit":
    endValue = (beginValue * 1.8) + 32
    print(endValue)
  
  if beginUnit == "Pound" and endUnit == "Euro":
    endValue = (beginValue * 1.16)
    print(endValue)



#Money converter
#pound, euro, dollar
rate = [1.16 , 1.15, 0.86, 0.99, 0.87, 1 ]
exchange = int(input("enter the conversion \n Options:\n pound -> euro (0)\n pound -> dollar (1) \n euro -> pound (2)\n euro -> dollar(3)\n dollar -> pound(4)\n dollar -> euro(5) \n"))

beginValue = int(input("enter beginning value: "))
endValue = beginValue * rate[exchange]
print(endValue)

