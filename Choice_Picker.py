import random
answers = ["yes", "no", "maybe"]
question = str(input("Ask a yes or no question: "))
result = random.choice(answers)
print(result)