# 1. Create the name variables
first_name = "Karan"  # Replace with your first name
last_name = "Arora"  # Replace with your last name

# 2. Concatenate with a space to create full_name
full_name = first_name + " " + last_name
print("Full name:", full_name)

# 3. Check if first_name length is greater than last_name length
# We use the len() function to get the length of strings
print("Is first name longer than last name?", len(first_name) > len(last_name))

# 4. Check if 'a' is in either first_name or last_name
# We use the 'in' operator combined with the 'or' logical operator
print("Is 'a' in first or last name?", ('a' in first_name) or ('a' in last_name))

# 5. Print the full name in all uppercase
# We use the .upper() string method
print("Full name in uppercase:", full_name.upper())