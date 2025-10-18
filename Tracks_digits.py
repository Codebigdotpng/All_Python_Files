num = int(input("Enter a number: "))
original_num = abs(num)
count = 0

if original_num == 0:
    count = 1
else:
    while original_num > 0:
        original_num = original_num // 10
        count += 1

print("It has", count, "digits.")

input("Press Enter to exit...")  # So you can see the result
