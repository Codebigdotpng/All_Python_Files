import random
number = random.randint(1, 5)
guess = int(input("Guess a number between 1 and 5: "))

while guess != number:
    if guess == number:
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 1 and 5: "))

print("You guessed the number! It was", number)