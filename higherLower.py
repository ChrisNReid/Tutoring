#number guesing game
#randomly generated number
#computer asks us to guess untill we get it right
#feedback is higher or lower
def game():
  import random
  # random integer, inclusive of values
  answer = random.randint(1,10)
  x = False
  count = 0
  while x == False:
    guess = input("Enter a number : ")
    count = count + 1 #count+=1
    #print("counter = ", count)
    guessint = int(guess)
    if answer < guessint:
     print("Smaller")
    elif answer > guessint:
      print("Higher")
    else:
      x = True
      
  print("Well done!", "It took you", count, "guesses")

# main menu function
def mainmenu():
  print("Welcome to the main menu!")
  choice = input("Do you want to play a game?")
  if choice == ("Yes"):
    game()  

global usernames 
usernames = ["admin"]
global passwords
passwords = ["password"]


def login():
  x = False
  while x == False:
    usrname = input("enter your username: ")
    pswrd = input("enter your password: ")
  
    if (usrname == usernames[0]) and (pswrd == passwords[0]):
      print("log in successful")
      mainmenu()
      x = True
    else:
      print("incorrect details")

def signup():
  password = ""
  while len(password) < 6:
    username = input("Enter your username:")
    password = input("Enter your password:")
    confpassword = input("Please confirm password :")
    if confpassword == password and len(password) > 6:
      print("Approved")
    else:
      print("make sure password is above 6 characters")

  usernames.append(username)
  passwords.append(password)
  mainmenu()
  
def firstmenu():
  choice = input("Do you already have an account (y/n")

  if choice == 'y':
    login()
  else:
    signup()

firstmenu()