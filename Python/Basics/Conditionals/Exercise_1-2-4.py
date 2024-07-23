# Exercise 1-2-4
currentMax = 0
for i in range(0,7):
    number = int(input('Enter a number: '))
    if number > currentMax:
        currentMax = number
print(currentMax)