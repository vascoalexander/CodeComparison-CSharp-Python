# Exercise 2-2-13
lst = []
for i in range(1,11):
    lst.append(i**3)
print(lst)

lst.clear()
for i in range(1,11):
    lst.append(pow(i, 3))
print(lst)