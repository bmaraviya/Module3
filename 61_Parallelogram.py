"""Write a Python program to calculate the area of a parallelogram"""

def parallelogram_area(base, height):
    return base * height
base = float(input("Enter the length of the base: "))
height = float(input("Enter the height of the parallelogram: "))
area = parallelogram_area(base, height)
print(f"The area of the parallelogram is {area}.")
