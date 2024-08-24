"""Write a Python program to convert a list of characters into a string."""

mylist = ['T','O','P','S']

str = ""
for i in range(len(mylist)):
    str += mylist[i]
print(str)