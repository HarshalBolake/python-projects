import random

secret_number = random.randint(1,10)
guess = 0

print("I am thinking a number from 1 to 10.")

while guess != secret_number:
    guess = int(input("Take a guess: "))

    if guess < secret_number:
        print("Too less")
    elif guess > secret_number:
        print("Too high")
    else:
        print("You guessed it!")