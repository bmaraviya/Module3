"""Write a Python program to remove duplicates from a list."""

mylist = []
n = int(input("How many Elements:"))
for i in range(n):
    element = input("Enter a Element:")
    mylist.append(element)
print(mylist)

rm = list(set(mylist))
print(rm)