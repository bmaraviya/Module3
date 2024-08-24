"""Write a Python script to sort (ascending and descending) a dictionary by value."""

student = {
    'Alex': 88,
    'Ben': 75,
    'Cyrus': 93,
    'Denver': 85
}
sorted_by_asc = dict(sorted(student.items(), key=lambda item: item[1]))
print("Ascending dictionary:",sorted_by_asc)
sorted_by_dsc = dict(sorted(student.items(), key=lambda item: item[1], reverse=True))
print("Descending dictionary:",sorted_by_dsc)