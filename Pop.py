fruits = ['apple', 'banana', 'cherry', 'date']
fruits.reverse()
# Pop the last item
last_fruit = fruits.pop()
print(last_fruit)  
print(fruits)      

# Pop the item at index 1
second_fruit = fruits.pop(1)
print(second_fruit)  
print(fruits)        

Veggies = ['carrot', 'broccoli', 'spinach', 'pepper']
Veggies.reverse()

Veggies.pop()
print("Wait, i don't need that veggie anymore. Here is the updated list:", Veggies)
Veggies.pop(0)
print("I bought pepper yesterday! I don't need it today. Here is the updated list:", Veggies)

print("I now need", fruits, "&", Veggies)
