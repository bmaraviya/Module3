"""Write a Python function that takes two lists and returns true if they have
at least one common member."""

list1 = [23,56,1,19,67,8]
list2 = [45,34,19,20]

def common_ele():
    for i in list1:
        if i in list2:
            return True
    return False

x = common_ele()
print(x)