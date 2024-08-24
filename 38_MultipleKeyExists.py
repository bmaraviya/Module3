"""Write a Python program to check multiple keys exists in a dictionary"""

my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
keys_to_check = {'apple', 'banana', 'date'}
all_exist = keys_to_check.issubset(my_dict.keys())
if all_exist:
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")
