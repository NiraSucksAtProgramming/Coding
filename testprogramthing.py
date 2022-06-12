#Hello there
#I'm pretty new here, so I'm just gonna slap some code onto this here py file and publish it
#For this i'm just gonna make a password generator

from random import * #Importing modules
import clipboard

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()[]"

def passgen(): #Putting the code in a function for the sake of reusability
    global chars
    password = "" #Making an empty string so that we can add to it in the future

    passwordlen = int(input("Req. number of characters in password: "))

    for x in range(passwordlen):
        passwordchar = choice(chars) #And here is how we add to it. Picking a random char out of the string
        password += passwordchar     #and adding to the empty string!

    print(f"Here is your password:\n{password}")

    copy = input("Would you like the password to be copied to your clipboard?: ")
    if copy.lower() == "yes":
        clipboard.copy(password) #This is why I imported the clipboard module
        print("Successfully copied to clipboard!")
    else:
        pass

    useagain = input("Would you like to use this again?: ")
    if useagain.lower() == "yes":
        passgen() #This is what I mean by reusability, being able to run the program again, quick and easy thing to do.
    else:
        pass

passgen()
