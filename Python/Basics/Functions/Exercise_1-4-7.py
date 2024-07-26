# Exercise 1-4-7
def sliceSum(lst, start, end):
    result = 0
    for item in lst[start:end+1]:
        result += item
    return result

print(sliceSum([4,10,12,16,18], 2, 4))
print(sliceSum([2,4,6,8,10,12], 0, 1))