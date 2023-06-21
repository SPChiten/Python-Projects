import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1

        if guess == number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        print("Number of attempts:", attempts)

guess_number()

