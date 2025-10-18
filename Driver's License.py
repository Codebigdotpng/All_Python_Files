try:
    age = int(input("Enter your age: "))
    has_license = input("Do you have a driver's license? (yes/no): ").lower()
    
    # Now you can use these variables for further processing
    print(f"Age: {age}")
    print(f"Has license: {has_license}")
    
except ValueError:
    print(" Please enter a valid number for your age.")