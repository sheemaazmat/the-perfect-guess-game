import random

number = random.randint(1, 100)
user_guess = 0
guess_count = 0

while user_guess != number:

    user_guess = int(input("Guess the number: "))
    guess_count += 1

    if user_guess > number:
        print("Lower number please")

    elif user_guess < number:
        print("Higher number please")

    else:
        print("You guessed it!")
        print("Number of guesses:", guess_count)