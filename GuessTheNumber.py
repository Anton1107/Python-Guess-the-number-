import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess number between 1 and {x} : "))
        if guess < random_number:
            print("Sorry the number is too low! Guess again!")
        elif guess > random_number:
            print("Sorry the number is to high! Guess again! ")
    print(f"Yay, congrats, you get guess the number {random_number} correctly!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could be high b/c low = high
        feedback = input(f"Is {guess} too high (H), too low (L), or correct(C)?? ".lower())
        if feedback == "h":
            high = guess - 1
        if feedback == "l":
            low = guess + 1
    print(f"Yay, the computer guessed your number, {guess}, correcctly!")


computer_guess(100)
