"""Write a Python script to check if a given key already exists in a dictionary."""

mydict = {'python':3,'php': 1,'java': 2}

key = input('Enter key to check:')

if key in mydict:
    print("Exists")
else:
    print("Does not Exist")