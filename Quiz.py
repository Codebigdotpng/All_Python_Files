try:
    divider = int(input("Enter a number: "))
    result = 100 / divider
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter a valid integer.")