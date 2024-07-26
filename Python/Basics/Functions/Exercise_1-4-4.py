# Exercise 1-4-4
def removeDuplicates(lst):
    newList = sorted(set(lst))
    return newList

print(removeDuplicates([0,3,5,7,3,5,1,-1]))
print(removeDuplicates([0,5,9,10,3,2,1,-3]))