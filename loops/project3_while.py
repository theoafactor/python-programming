users = [
    {
        "firstname": "James Andrew 1st",
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



while True:
    # ask the user for their email
    userEmail = input("Please enter your email: ")

    if userEmail == "james@email.com":
        print('Welcome User')
        break
    else:
        print("Invalid email .. please try again")
