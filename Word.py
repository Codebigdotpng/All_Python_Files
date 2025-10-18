while True:
    word = input("Type a word: ")

    if len(word) > 10:
        print("Too long! Try a shorter word.")
        continue  # Skip the rest and go back to top

    if word == "banana":
        print("You found the mystery word! 🍌")
        break

    print("Nope, not the mystery word.")
