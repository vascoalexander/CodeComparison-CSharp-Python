money = float(input('Enter the amount to be converted: '))
convertTo = input('Convert to? (e for euro or d for dm)')
if convertTo == 'e' or convertTo == 'E':
    print(f'{money} DM are {(money / 1.95583):.2f} in Euro.')
elif convertTo == 'd' or convertTo == 'D':
    print(f'{money} Euro are {(money * 1.95583):.2f} in DM')
else:
    print('Invalid input. Exit program!')
    exit()