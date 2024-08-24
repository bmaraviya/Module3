"""Write a Python program to print all unique values in a dictionary."""

my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 200, 'e': 300, 'f': 400}
unique_values = []
for value in my_dict.values():
    if value not in unique_values:
        unique_values.append(value)
print("Unique values in the dictionary:", unique_values)
