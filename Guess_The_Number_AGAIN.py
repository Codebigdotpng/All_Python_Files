secret_number = 5
guess = int(input("Guess the number:"))
while guess != secret_number:
    print("Wrong! Try again.")
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        break
print("Yes! You guessed it!")