users = [
    {
        "firstname": "James",
        "lastname": "John",
        "email": "jamesjohn@gmail.com",
        "password": "password1",
        "awards": ['first_class', "second_citizen", "oprah_status"],
        "address": {
            "house_no": 2,
            "street_name": "Oweh",
            "state": "Lagos",
            "country": "Nigeria"
        }
    }, 
    {
       "firstname": "Mary",
        "lastname": "Joseph",
        "email": "maryjoseph@gmail.com",
        "password": "1996_mypassword",
        "awards": [],
        "address": {
            "house_no": 1,
            "street_name": "Abia",
            "state": "Lagos",
            "country": "Nigeria"
        }
    },
    {
        "firstname": "Andrew",
        "lastname": "Jacob",
        "email": "andry@gmail.com",
        "password": "flower123",
        "awards": ['second-citizen'],
        "address": {
            "house_no": 45,
            "street_name": "Jacobson",
            "state": "Ogun",
            "country": "Nigeria"
        }
    },
    {
        "firstname": "Akeem",
        "lastname": "Ahmed",
        "email": "akeem@gmail.com",
        "password": "password2",
        "awards": ["first-class"],
        "address": {
            "house_no": 55,
            "street_name": "Oweh",
            "state": "Lagos",
            "country": "Nigeria"
        }
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

        print("""---> Awards Received: """ + str(user['awards']) + """
---> Street Name: """ + user["address"]["street_name"] +
        
            """ """)

        break
else: 
    print("You are not registered")




  