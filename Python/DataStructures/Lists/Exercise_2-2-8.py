# Exercise 2-2-8
list_one = [9, 8, 7, 14, 3, 2, "a", "p", "hello", "b"]
list_two = ["b", 1, 9.2, 6, 3, 9, "p"]
new_list = set(list_one).union(set(list_two))
print(list(new_list))

# alternative without sets and union()
new_list.clear()
new_list = list_one
for i in list_two:
    if i not in list_one:
        new_list.append(i)
print(new_list)