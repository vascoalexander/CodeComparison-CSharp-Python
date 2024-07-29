# Exercise 2-2-17
from random import randint
lst = []
while len(lst) < 10:
    next_number = randint(-40,50)
    lst.append(next_number)

for i in lst:
    print(f"{i:4d}",end="")

print()

for i in range(len(lst)-1,-1,-1):
    print(f"{lst[i]:4d}",end="")

print()

# alternative with reverse()
lst.reverse()
for i in lst:
    print(f"{i:4d}", end="")


# numbers = []
# while len(numbers) < 5:
#     next_number = int(input("Enter next number: "))
#     numbers.append(next_number)
# 
# min = numbers[0]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
#     if number < min:
#         min = number
# 
# print(f"min number: {min}\nmax number: {max}")