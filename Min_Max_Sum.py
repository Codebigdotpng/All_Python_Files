#Examples of minimum, maximum, and summation functions in Python
#min
numbers=[3, 1, 4, 1, 5, 9, 2, 6, 5]
minimum=min(numbers)
print("The minimum is:", minimum)

print("The minimum is-", (min(13, 4, 98, 3, 2.5)))

words=["strawberry", "mango", "apple", "melon"]
print("The minimum word is:", min(words))

#max
numbers=[3, 1, 4, 1, 5, 9, 2, 6, 5]
maximum_value=max(numbers)
print("The maximum is:", maximum_value)

print("The maximum is-", (max(13, 4, 98, 3, 2.5)))

words=["strawberry", "mango", "apple", "melon"]
print("The maximum word is:", max(words))

#sum
numbers=[3, 1, 4, 1, 5, 9, 2, 6, 5]
summative_Value=sum(numbers)
print("The sum is:", summative_Value)
print("The sum is-", (sum([13, 4, 98, 3, 2.5])))

shirt=299
jacket=198.98
jeans=449.49
shoes=99.99
prices=[shirt, jacket, jeans, shoes]
total_price=sum(prices)
print("The cashier said your total price is:", total_price)
