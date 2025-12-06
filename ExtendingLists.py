numbers = [1, 2, 3]

# Using extend()
numbers.extend([4, 5])
print(numbers)  # Output: [1, 2, 3, 4, 5]

# Reset for comparison
numbers = [1, 2, 3]

# Using append()
numbers.append([4, 5])
print(numbers)  # Output: [1, 2, 3, [4, 5]] ← adds a NESTED list!