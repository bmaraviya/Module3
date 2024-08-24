"""Write a Python function that takes a list and returns a new list with unique 
elements of the first list."""

def unique_list(lst_of_elements):
    num = []
    for a in lst_of_elements:
        if a not in num:
            num.append(a)
    
    print("unique List: ",num)

lst_of_elements = []
n = int(input("How many Elements : "))
for i in range(0, n):
    ele = int(input())
    lst_of_elements.append(ele) 
print("Origional List: ", lst_of_elements)

unique_list(lst_of_elements)