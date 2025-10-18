my_dict = {}

# Create
my_dict['name'] = 'Karan'
my_dict['age'] = 8

# Read
print(my_dict['name'])      # Karan
print(my_dict.get('city'))  # None

# Update
my_dict['age'] = 9
my_dict['city'] = 'Gurgaon'

# Delete
del my_dict['city']

print(my_dict)  # {'name': 'Karan', 'age': 9}
