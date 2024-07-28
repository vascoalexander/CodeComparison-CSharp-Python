# Exercise 2-2-6
lst = []
new_lst = []
for i in range(1,11):
    lst.append(i)

# using len() and range()
for i in range(0,len(lst),3):
    new_lst.append(lst[i])
print(new_lst)

new_lst.clear()
# slicing method
for i in lst[::3]:
    new_lst.append(i)
print(new_lst)