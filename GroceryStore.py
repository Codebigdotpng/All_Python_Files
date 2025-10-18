inventory= {
    "banana":4,
    "apple":5,
    "bread_packet":3,
    "Mangoes":2,
    "Milk_Carton":6
}
print("Here are all the items as of now (The start of the day)")
for key, value in inventory.items():
    print(key + ": " + str(value))
print("3 bananas were sold.")
inventory.update({"banana":1})
print("A worker asks,'Do we have Mangoes?'")
if "Mangoes" in inventory:
    print("Yes")
else:
    print("No, we don't.")
print("4 Milk Cartons just got sold.")
inventory.update({"Milk_Carton":2})
print("5 apples were sold. We  don't have any more!")
inventory.pop("apple")
print("Item Restock!The items are replenished!")
inventory.update({"apple":7})
inventory.update({"bread_packet":5})
inventory.update({"banana":5})
inventory.update({"Mangoes":6})
inventory.update({"Milk_Carton":5})
print("The shop is closed! Here is a list of the items left:")
for key, value in inventory.items():
    print(key + ": " + str(value))