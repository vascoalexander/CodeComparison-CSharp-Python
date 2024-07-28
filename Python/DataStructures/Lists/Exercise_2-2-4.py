# Exercise 2-2-4
# without count()
lst = [3,2,2,1,9,1,2,3,7]
counter = 0
for i in lst:
    if i == 1:
        counter += 1
print(counter)

# lazy
lst = [3,2,2,1,9,1,2,3,7]
print(lst.count(1))