"""Write a Python function to calculate the factorial of a number (a nonnegative integer)"""

def factorial(n):
    if n < 0:
        return "The input must be a non-negative integer."
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result
num = int(input("Enter a non-negative integer: "))
result = factorial(num)
print("Factorial:", result)
