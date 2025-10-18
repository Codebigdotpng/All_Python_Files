secret_number= 7
i= int(input("Guess the Number(Tip-the number must be less than 20!):"))
while i != secret_number:
    print("Not the right answer...do it AGAIN.")
    i= int(input("Guess the Number:"))
if i==secret_number:
   print("Yes! You got it!")