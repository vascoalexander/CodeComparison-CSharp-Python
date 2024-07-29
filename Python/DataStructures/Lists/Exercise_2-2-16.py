# Exercise 2-2-16
from random import shuffle, randint
elements = [3,6,8,7,2,'s','ch','d']
shuffle(elements)
print(elements)

# without shuffle()
def random_lst(x):
    random_lst = []
    while len(random_lst) < x:
        next_number = randint(0,x-1)
        if next_number not in random_lst:
            random_lst.append(next_number)
    return random_lst

shuffled_lst = []
random_index = random_lst(len(elements))
for i in range(0, len(elements)):
    next_random_index = random_index[i]
    shuffled_lst.append(elements[next_random_index])
print(shuffled_lst)
