"""Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}"""

sample_dict = {'1': ['a', 'b'], '2': ['c', 'd']}
combinations = [i + j for i in sample_dict['1'] for j in sample_dict['2']]
for i in combinations:
    print(i)
