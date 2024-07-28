# Exercise 2-2-10
ch = "hello everyone"
lst = list(ch)
lst.reverse()
new_string = ""
for i in lst:
    new_string += i
print(new_string)

# string slicing
ch = "hello everyone"
print(ch[::-1])