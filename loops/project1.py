users  = ["James", "John", "Jerry", 'Mary', 'Andrew', "Jacob"]

# ask user to enter their name
username = input("Enter your name: ")

# check if the name entered is inside users list
for user in users:
    if username == user:
        print("You are registered")
    else:
        print("You are not registered")