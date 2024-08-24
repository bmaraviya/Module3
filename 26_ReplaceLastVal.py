"""Write a Python program to replace last value of tuples in a list."""

mytuple = [(5,6),(45,34,7,2)]
newval = 15
newlist = [t[:-1] + (newval,) for t in mytuple]
print(newlist)