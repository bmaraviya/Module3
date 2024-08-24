"""Write a Python program to unzip a list of tuples into individual lists."""

tuple_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
list1, list2, list3 = zip(*tuple_list)
print(list(list1))  
print(list(list2)) 
print(list(list3))