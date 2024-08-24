"""Write a Python program to remove an empty tuple(s) from a list of tuples."""

tuple_list = [(10, 20), (), (30, 40), (), (50,60,70)]

new_list = []
for t in tuple_list:
    if len(t) > 0: 
        new_list.append(t)
print(new_list)
