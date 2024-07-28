# Exercise 2-2-9
fruits = [('apple', 15), ('banana', 8), ('miller', 12), ('kiwi', 9), ('peach', 2)]

new_list = sorted(fruits, key=lambda x:x[1])
print(new_list)