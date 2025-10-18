# Stop the monkey
stopping_message = "stop"
print("A monkey is on your keyboard! (I'm surprised it's not your cat) Type 'stop' to make it stop.")
typo = input("Please type something: ")
print("Someone typed:", typo)

while typo != stopping_message:
    print("Uhhh...the monkey is still there! Make it stop!")
    typo = input("Please type something: ")
    print("Someone typed:", typo)

print("Finally! The monkey saw your message and got off.")
