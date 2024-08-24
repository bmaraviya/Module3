"""Write a Python program to find the highest 3 values in a dictionary"""


my_dict = {'a': 50, 'b': 200, 'c': 100, 'd': 300, 'e': 150}
top_3_values = sorted(my_dict.values(), reverse=True)[:3]
print("The highest values in the dictionary are:", top_3_values)
