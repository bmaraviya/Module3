"""Write a Python program to check whether an element exists within a tuple."""

mytuple = ('python','php','java')

element = input('Enter Element to check:')

if element in mytuple:
    print("Exists")
else:
    print("Does not Exist")