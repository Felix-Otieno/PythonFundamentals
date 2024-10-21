import random

number = random.randint(0, 100)

print("Guess a magic number 0 to 100")

guess = -1

while guess != number:
    guess = eval(input("Enter your guess: "))

    if guess == number:
        print(f"Yes, the number is {number}")
    elif guess > number:
        print(f"Your guess is too high")
    else:
        print(f"You guess is too low")