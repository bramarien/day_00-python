import random
import sys


def guessinggame():
    attempts = 0
    guess = random.randint(1, 99)
    print("This is an interactive guessing game!")
    print("Enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck !")
    while (1):
        print("\nWhat's your guess between 1 and 99?")
        test = input()
        if test == "exit":
            print("Goodbye!")
            return
        if test.isdigit() == 0 or (int(test) > 99 or int(test) < 1):
            print("That's not a number")
        else:
            attempts += 1
            if int(test) > guess:
                print("Too high!")
            elif int(test) < guess:
                print("Too low!")
            elif int(test) == guess:
                print("Congratulations, you've got it!")
                print("You won in %d attempts!" % attempts)
                return


guessinggame()
