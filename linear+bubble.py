def linearSearch(data):
    # data = [1,2,3,67,4,6,10,45,7,5,81]
    target = input("Enter your target: ")
    found = False
    i = 0
    while found == False and (i < len(data) - 1):
        if data[i] == target:
            found = True
            print(data[i], " - target found")
            print("found in ", i, " steps")
        else:
            i = i + 1
            print(data[i], " - not target")

    if found == False:
        print("\n Item not in list")


def bubbleSort(data):
    # data = [101,400,2,3,67,4,6,10,45,7,5,81]
    swapped = True
    swaps = 0
    passnum = 0
    while swapped == True:
        swaps = 0
        passnum = passnum + 1
        for i in range(0, len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swaps = swaps + 1

                #data = data[i+1] and data[i+1] = data[i] but does at the same time
        if swaps < 1:
            return
        print("Pass ", passnum, ": ", data)


print("List entry")
print("Enter '00' if you have finished \n")
inp = ""
data = []
while inp != "00":

    inp = input("Enter a number to add to your list: ")
    if inp != 0:
        data.append(inp)

print("Your list: ", data)

choice = input(
    "Do you want to Linear Search('search') your List or Bubble Sort('sort'?")

if choice == "search":
    linearSearch(data)
else:
    bubbleSort(data)
