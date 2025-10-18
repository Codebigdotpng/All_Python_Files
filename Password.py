password="secret"
guess= input("Enter password-")
while guess != password:
    print("Incorrect password. Please try again.")
    guess= input("Enter password-")
if guess==password:
    print("Correct password. Access granted.")