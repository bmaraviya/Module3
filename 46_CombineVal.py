"""Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, o {'item': 'item1', 'amount': 750}]"""

data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]
combined_dict = {}
for entry in data:
    item = entry['item']
    amount = entry['amount']
    if item in combined_dict:
        combined_dict[item] += amount
    else:
        combined_dict[item] = amount
print("Combined dictionary:", combined_dict)
