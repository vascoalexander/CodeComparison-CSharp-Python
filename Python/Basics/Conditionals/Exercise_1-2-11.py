# Exercise 1-2-11
year = int(input('Enter the a Year: '))
if year % 400 == 0:
    isLeapYear = ""
elif year % 4 == 0 and year % 100 != 0:
    isLeapYear = ""
else:
    isLeapYear = " not"
print(f'{year} is{isLeapYear} a Leap Year.')