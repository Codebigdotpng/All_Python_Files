fruit = ["oranges", "apples", "bananas"]
fruit_length=len(fruit)
print("I need to get", fruit_length, "fruits from the shop.")
fruit.append("grapes")
print("Oh wait, I also need to get grapes.")
print("Now, I need to get", len(fruit), "fruits from the shop.")
print("Ok, I will buy", fruit)
veggies=["carrots", "broccoli", "spinach"]
veggie_length=len(veggies)
print("I need to get", veggie_length, "veggies from the shop.")
veggies.append("lettuce")
print("Oh wait, I also need to get lettuce.")
print("Now, I need to get", len(veggies), "veggies from the shop.")
print("Right, So, Let's buy", fruit_length,"fruit, so-", fruit, "&", veggie_length,"veggies, which are-", veggies)