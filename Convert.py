num = 10
text = str(num)  # Convert number to text
print(text)  # Output: "10" (as a string)
print(type(text))  # Output: <class 'str'>

age = "9"      # Text (string)
new_age = int(age)  # Convert to a number
print(new_age + 1)  # Output: 10
#Above, You see Type Casting
#Below,You See implicit type conversion

x = 5   # Integer
y = 2.5 # Float
z = x + y  # Python automatically converts x to float
print(z)   # Output: 7.5
print(type(z))  # Output: <class 'float'>
