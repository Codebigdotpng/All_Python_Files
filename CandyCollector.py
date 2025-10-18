candies = 0

while True:
    color = input("Pick a candy color (type 'stop' to end): ")
    
    if color == "blue":
        print("Who eats blue candy? Skipping...")
        continue

    if color == "stop":
        print("Game Over! You collected", candies, "candies.")
        break

    print("Yum! Candy collected.")
    candies += 1
