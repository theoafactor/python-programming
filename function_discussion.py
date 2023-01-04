gender = input("Enter your gender: ")

def greetUser(gender):
    print("Good morning sir") if gender == "male" else print("Good morning ma")



# if gender == "male":
#     greetUser('male')
# elif gender == "female":
#     greetUser('female')
# else:
#     print("Error! male or female is allowed")


greetUser(gender) if gender == "male" or gender == "female" else None



