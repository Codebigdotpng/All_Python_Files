# Step 1: Ask which operation to use
print("Choose operation: +, -, *, /")
operation = input("Enter operation: ")

try:
    # Step 2: Ask number 1
    num1 = float(input("Enter first number: "))

    # Step 3: Ask number 2
    num2 = float(input("Enter second number: "))

    # Step 4: Solve
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result = "Cannot divide by zero!"
        else:
            result = num1 / num2
    else:
        result = "Nahh,I can't do that as your operation has to be +(Add),-(Subtract),*(Multiply)or /(Divide)."

    print(result)

except ValueError:
    print("Uhh... That's not an integer.")
