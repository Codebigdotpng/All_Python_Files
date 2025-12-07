class Backpack:
    def __init__(self, owner, color, max_items):
        self.owner = owner
        self.color = color
        self.max_items = max_items
        self.items = []  # Always start empty!

    def add_item(self, item):
        if len(self.items) >= self.max_items:
            print("Backpack is full! You can't add", item)
        else:
            self.items.append(item)
            print("Added", item, "to", self.owner, "'s backpack.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print("Removed", item, "from", self.owner, "'s backpack.")
        else:
            print(item, "not found in", self.owner, "'s backpack.")

    def info(self):
        print(self.owner + "'s backpack is " + self.color + " and can contain:", self.max_items)
        print("Current items:", self.items)

    def list_items(self):
        if not self.items:
            print(self.owner + "'s backpack is empty.")
        else:
            print(self.owner + "'s backpack contains:")
            for item in self.items:
                print(" -", item)

# Test it!
my_backpack = Backpack("Kyra", "Black", 3)  # Try max=3 to test full backpack!
my_backpack.info()
my_backpack.add_item("Notebook")
my_backpack.add_item("Black Pen")
my_backpack.add_item("Blue Pen")
my_backpack.add_item("Pencil")  # Should fail—backpack full!
my_backpack.list_items()