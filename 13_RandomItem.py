"""Write a Python program to select an item randomly from a list."""

import random

mylist = ["Python", "PHP", "Android", "ReactJS", "Java"]
item = random.choice(mylist)
print(item)