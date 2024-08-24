"""Write a Python program to check whether a list contains a sub list"""

list1 = [22,41,98,2,38]
list2 = [41,22]

count = 0

for i in list1:
    for j in list2:
        if i == j:
            count += 1

if count == len(list2):
    print("Sublist exists")
else:
    print("Sublist does not exists")