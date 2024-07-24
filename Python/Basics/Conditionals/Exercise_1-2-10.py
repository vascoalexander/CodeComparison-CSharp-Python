# Exercise 1-2-10
birthyear = int(input('Enter your birthyear(YY): '))
currentYear = int(input('Enter the current Year(YY): '))
if birthyear > currentYear:
    age = (currentYear + 100) - birthyear
else:
    age = currentYear - birthyear
print(f'Your age is {age}.')