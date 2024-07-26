# Exercise 1-4-2
def elementInList(lst, element):
    if element in lst:
        return True
    else:
        return False
    
print(elementInList([1,2,3,4,5,6], 2))
print(elementInList([3,6,9,7,11], -1))