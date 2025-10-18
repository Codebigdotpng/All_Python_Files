coins=0
while True:
    answer=input("You found a coin!Do you want to pick it up?(say yes/no)")
    if answer=="yes":
        coins+=1
    elif answer=="no":
        print("Game over. You collected",coins,"coins.")
        break