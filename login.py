#login system, 
#sign up and log in
#main menu
# ask user if they want to login or sign up
# sign up, enter usrname and paswrd 
#    check usrnam is not empty
#    check password, least 6 characters, and a special character(!)
# if all okay. save login details to a array

#log in
#ask them to en
# check usrname and password is in a array

usernames = []
passwords = []
login = input("Do you want to Log In or Sign Up?")
if login == ("Sign Up"):
  signup = input("Enter a username:")
  signpassword = ""
  confpassword = "fff"

  while (signpassword != confpassword) or (signpassword == "password"):
    signpassword = input("Enter a password:")
    confpassword = input("confirm your password:")
  
  passwords.append(signpassword)
  usernames.append(signup)
  print("sign up successful")

  # types of testing data
  # normal = expected data
  # boundary = on the border between valid and invalid
  # erroneous = invalid data

  
 