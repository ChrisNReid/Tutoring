#create a program that will keep track of items for a shopping list. The program should allow you to keep adding new items. You should also be able to record which shop you are going to visit for the item

#ask the user for an item
#ask user for items shop
#add both to a text file


item=input("Enter item :")
shop=input("Enter item's shop :")
priority=input("Enter the priority of the item :")

f =  open('shoppingList.txt','a')
f.write("\n" + item + " - " + shop +" - "+ priority)
f.close()

print("reading")
f = open('shoppingList.txt','r')
print(f.read()) 


#to order
#put in a 2d array
# [Grapes - Tesco - 1]
# [Apples - Tesco - 5]
# [Tomato - Waitrose - 2]
# [Banana - Tesco - 3]
# [Strawberry - Aldi - 4]

# sort based on the number at the end
# x = len(i)
# i[x]
# i[-1] = goes to the end of a list/string etc
# -1 means the end

x= "hello world"
print(x[-1])



