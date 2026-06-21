#Contact Book
Contact_Book = {}

while True:
    Profile = input("What would you like to do? (1=Add, 2=View, 3=Quit):")
    if Profile == "1":
        Name = input("Enter the name of the contact:")
        Number = input("Enter the number of the contact:")
        Contact_Book[Name] = Number
        print("Contact added successfully!")
    elif Profile == "2":
        if not Contact_Book:
            print("No contacts found.")
        else:
            print("Contact List:")
            for name, number in Contact_Book.items():
                print(f"{name}: {number}")
    elif Profile == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1, 2, or 3. Try again.")
