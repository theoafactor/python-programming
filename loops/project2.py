users = [
    {
        "firstname": "James",
        "lastname": "John",
        "email": "jamesjohn@gmail.com",
        "password": "password1"
    }, 
    {
       "firstname": "Mary",
        "lastname": "Joseph",
        "email": "maryjoseph@gmail.com",
        "password": "1996_mypassword"
    },
    {
        "firstname": "Andrew",
        "lastname": "Jacob",
        "email": "andry@gmail.com",
        "password": "flower123"
    },
    {
        "firstname": "Akeem",
        "lastname": "Ahmed",
        "email": "akeem@gmail.com",
        "password": "password2"
    }

]


## Greet the user
print( """ 
        ------------- Welcome to the Register --------------- 
        -----------------------------------------------------
        -----------------------------------------------------
        ----------------- by Olu Adeyemo --------------------
        
    """)



## collect email from the user
useremail = input("Please enter your email: ")

print("Great! The email you entered is " + useremail)

## collect password from the user
userPassword = input("Please enter your password: ")



## loop through the data
for user in users:
    if user['email'] == useremail and user['password'] == userPassword:
        print("Welcome " + user['firstname'] + " " + user['lastname'])
        break
else: 
    print("You are not registered")




  