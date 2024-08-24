"""Write a Python program to find the repeated items of a tuple."""

mytuple = (1, 2, 3, 4, 2, 3, 5, 6, 2, 4)
repeated_items = []
for item in mytuple:
    if mytuple.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)
print(repeated_items)