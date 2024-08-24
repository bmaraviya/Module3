"""Write a Python program to convert a list of tuples into a dictionary."""

tuple_list = [('Name', 'City', 'Subject'), ('Bansi', 'Rajkot','Python')]
keys = tuple_list[0]
values = tuple_list[1]
my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print(my_dict)