"""Write a Python function to check whether a number is perfect or not."""

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
num = int(input("Enter a number to check if it is perfect: "))
if num > 0:
    print(f"{num} is a perfect number." if perfect_number(num) else f"{num} is not a perfect number.")
else:
    print("Please enter a positive integer.")