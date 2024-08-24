"""Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'w3resource'"""

mystr = 'w3resource'
count_dict = {}
for char in mystr:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1

print("Character counts:", count_dict)
