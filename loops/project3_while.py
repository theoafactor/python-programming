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

no_of_failed_attempt = 0 ## add a counter for checking the number of failed attempts
checker = True
while checker:
    # ask the user for their email
    userEmail = input("Please enter your email: ")
    print("Great! The email you entered is " + userEmail)

    ## collect password from the user
    userPassword = input("Please enter your password: ")

    ## loop through the data
    for user in users:
        if user['email'] == userEmail and user['password'] == userPassword:
            print("Welcome " + user['firstname'] + " " + user['lastname'])

            print("""---> Awards Received: """ + str(user['awards']) + """
---> Street Name: """ + user["address"]["street_name"] +
            
                """ """)
            checker = False
            break   
    else: 
        no_of_failed_attempt = no_of_failed_attempt + 1
        if no_of_failed_attempt < 3:
            print("Invalid user email and password. Please check and try again.") 
        else:
            print("You ran out of chances. No more attempt")
            checker = False
            break