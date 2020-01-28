import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


quit = False 
range = 100 

while not quit: 
    random_number = random.randint(1,range)
    count = 2
    number = -1
    while number != random_number:
        number = input("Hello! PLease guess a number between 1 and {}: ".format(range))
        if not number.isdigit(): 
            print("Please guess a number.")
        else:
            number = int(number)
            count = count + 1 
            print("Sorry, you were incorrect.")
            if number > random_number:
                print("Too high.")
            else number < random_number:
                print ("That guess was too low.")
print("Well done!")
print("You guessed it in {} attempts." .format(count))
play_again = input("\nWould you like to try again? (yes or no)? ")
play_again = play_again. lower()
if play_again == "yes" or play_again == "y":
    quit=False
else: 
    quit=true

print("Thank you for playing!")