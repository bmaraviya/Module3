"""Write a Python function to get the largest number, smallest num and sum of all from a list."""

myslist = [32, 4, 81, 23, 67, 50]

def getData():
    summation = sum(myslist)
    maximum = max(myslist)
    minimum = min(myslist)

    print("Sum is",summation)
    print("Maximum Number is",maximum)
    print("Minimum Number is",minimum)

getData()