# user has to enter a password
# has to be 6+ characters long
# user has to confirm the password
# check password is equal to confirm password. if so, print approved

password = input("Enter a password (more than 6 characters long) :")
if len(password) > 6:
  password1 = input("Please confirm password :")
  if password1 == password:
    print("Approved")
else:
  print("Your password must be more than 6 characters long.")
    


