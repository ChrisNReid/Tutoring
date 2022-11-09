#Change return Program

#user input of money owed

#user input of money given

#calculate how much change left

#calculate in denominations £50, £20, £10, £5, £2, £1, 50p, 20p, 10p, 5p, 2p, 1p

moneyowed = float(input("Enter money  owed :"))
moneygiven =float(input("Enter money given :"))
change = (moneygiven - moneyowed)
print ("Change to give:", change)

# if change >= 50:
#   change = change - 50
#   print("Give £50")

# if change >= 20:
#   change = change-20
#   print("Give £20")

# if change >= 10:
#   change = change-10
#   print("Give £10")

# if change >= 5:
#   change = change-5
#   print("Give £5")
# if change >= 2:
#   change = change-2
#   print("Give £2")
# if change >= 1:
#   change = change-0.5
#   print("Give £1")
# if change >= 0.5:
#   change = change-1
#   print("Give 50p")
# if change >= 0.2:
#   change = change-0.2
#   print("Give 20p")
# if change >= 0.1:
#   change = change-0.1
#   print("Give 10p")
# if change >= 0.05:
#   change = change-0.05
#   print("Give 5p")
# if change >= 0.02:
#   change = change-0.02
#   print("Give 2p")
# if change >= 0.01:
#   change = change-0.01
#   print("Give 1p")
# else:
#   print("all done")

monies = [50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
for i in range(len(monies)):
  if change >= monies[i]:
    change = change - monies[i]
    print("Given money: ", monies[i])