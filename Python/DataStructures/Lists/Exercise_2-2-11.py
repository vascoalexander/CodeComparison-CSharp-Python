from random import randint

lst = []
for i in range(1,21):
    next_random = randint(1,100)
    lst.append(next_random)
print(lst)

# unique numbers
lst = []
while len(lst) < 20:
    next_random = randint(1,100)
    if next_random not in lst:
        lst.append(next_random)
print(lst)
