Door_Number = 7

while True:
    i = int(input("Guess the number behind the door (1–10): "))

    if i > 10 or i < 1:
        print("The number behind the door can only be from 1 to 10.")
        continue

    if i == Door_Number:
        print("The door opens! You guessed it right!")
        break

    print("Nope. Try again.")
