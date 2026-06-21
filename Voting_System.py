Name= input("Enter your name: ")
Age= int(input("Enter your age: "))
print ("Hello,", Name, "you are", Age, "years old & will be", Age + 1, "years old next year!")

if Age >= 18:
    print(f"You are an adult & eligible to vote, {Name}!")
else:
    print(f"You can't vote yet, {Name}. You will be eligible to vote in {18 - Age} years.")