# Exercise 1-2-11
currentYear = int(input('Enter the current Year: '))
if currentYear % 400 == 0:
    isLeapYear = ""
elif currentYear % 4 == 0 and currentYear % 100 != 0:
    isLeapYear = ""
else:
    isLeapYear = " not"
print(f'{currentYear} is{isLeapYear} a Leap Year.')