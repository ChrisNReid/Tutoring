
#Unit Converter
beginUnit = input("enter the unit being converted (celcius/..)")
beginValue = int(input("enter beginning value: "))
endUnit = input("enter the final unit (fahrenheit/..)")

if beginUnit == "celcius" and endUnit == "fahrenheit":
  endValue = (beginValue * 1.8) + 32
  print(endValue)
