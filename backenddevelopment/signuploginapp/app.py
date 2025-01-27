print("Create Account NOw")
username = input("Enter Username: ")
password = input("Enter password: ")

print("Your Account has been created successfully")


username2 = input("Enter Username: ")
password2 = input("Enter Password: ")

if username == username2 and password == password2:
    print("You Have logged in to your account")
else:
    print("Invalid credentials")
