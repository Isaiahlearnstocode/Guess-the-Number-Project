# Imports the random library
import random

# This allows the variable "number" to store a value between 1 and 100
number =  random.randrange(1,100)
# This makes sure that the user inputs a number in between 1 and 100 and if they were to try to type and word they would get an error
guess = int(input("Guess a number between 1 and 100: "))

# While the user's guess is not equal to the number this code will execute
while guess != number:
    # If the users guess us less than the number this code will execute
    if guess < number:
        #It will print that the value of the number is higher. Try another number and 
        print("The value of the number is higher. Try another number")
        guess = int(input("Guess a number between 1 and 100: "))
    else:
        print("The value of the number is lower. Try another number")
        guess = int(input("Guess a number between 1 and 100: "))

print("You Win!")