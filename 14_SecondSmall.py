"""Write a Python program to find the second smallest number in a list."""

li = [] 
n = int(input("How many elements: "))
for i in range(1, n+1): 
    elem = int(input("Enter the elements: ")) 
    li.append(elem) 
li.sort() 

print(li) 
print("The second smallest value of this list: ",li[1])