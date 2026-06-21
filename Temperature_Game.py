import random

# Weather Guessing Game

# GOD decides the temperature (between -20 and 40)
# Temperature in celcius, so get rekt americans
try:
    god_input = str(random.randint(-20, 40))  # 👈 GOD sets today's temperature here as a string

    actual_temperature = int(god_input)
except (ValueError, NameError):
    print("Uhh... wrong script. Not even an integer?!")
    exit()

# Check if God followed the temperature rule
if actual_temperature < -20 or actual_temperature > 40:
    print("⚠️ We can't even show you the weather report as the weather is insane. I gotta go to my room...")
    exit()
else:
    print("🌦️ Weather Report:")

    # Clue 1
    if actual_temperature < 0:
        print("Clue 1: It's freezing! Temperature less than zero! ❄️")
    elif actual_temperature < 10:
        print("Clue 1: It's pretty chilly. Less than 10 degrees. 🧥")
    else:
        print("Clue 1: No need for a jacket. More than 10 degrees. 🌞")

    # Clue 2
    if actual_temperature >= 30:
        print("Clue 2: It's hot enough to melt ice cream! More than 30 degrees heat. 🍦")
    elif actual_temperature >= 15:
        print("Clue 2: It’s a nice day outside. 15–30 degrees. 🚶‍♀️")
    else:
        print("Clue 2: You might want to stay warm. Less than 15 degrees. 🔥")

    # Clue 3
    if actual_temperature % 2 == 0:
        print("Clue 3: The temperature is an even number. 🔢")
    else:
        print("Clue 3: The temperature is an odd number. 🔢")

    # Start guessing game
    winner = None
    turn = 1
    while winner is None:
        print(f"\n🔁 Turn {turn}")

        # Player 1
        try:
            guess1 = int(input("Player 1, guess the temperature: "))
        except ValueError:
            print("ENTER A NUMBER, DUDE.")
            continue

        if guess1 == actual_temperature:
            winner = "Player 1"
            break
        elif abs(guess1 - actual_temperature) <= 2:
            print("🔥 Ooh! Very close, just a few degrees off!")
        elif guess1 // 10 == actual_temperature // 10:
            print("😊 Ooh! Close. Guess in the same tens place.")
        elif (20 <= guess1 < 30) and (20 <= actual_temperature < 30):
            print("🌡️ Ooh! In the same 20s range though.")
        else:
            print("❌ Nope! Not even close.")

        # Player 2
        try:
            guess2 = int(input("Player 2, guess the temperature: "))
        except ValueError:
            print("ENTER A NUMBER, DUDE.")
            continue

        if guess2 == actual_temperature:
            winner = "Player 2"
            break
        elif abs(guess2 - actual_temperature) <= 2:
            print("🔥 Ooh! Very close, just a few degrees off!")
        elif guess2 // 10 == actual_temperature // 10:
            print("😊 Ooh! Close. Guess in the same tens place.")
        elif (20 <= guess2 < 30) and (20 <= actual_temperature < 30):
            print("🌡️ Ooh! In the same 20s range though.")
        else:
            print("❌ Nope! Not even close.")

        turn += 1

    print(f"\n🏆 {winner} wins! Good Game! The temperature was {actual_temperature}°C. Good One, {winner}.")
