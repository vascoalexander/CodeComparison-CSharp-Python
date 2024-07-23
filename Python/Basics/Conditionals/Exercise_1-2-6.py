# Exercise 1-2-6
currentAccount = float(input('How much money is in your current Acount?: '))
savingsAccount = float(input('How much money is in your savings Account?: '))
if currentAccount > 1000 or savingsAccount > 1500:
    print(f'The fee is 0.15 euro.')
else:
    print('No fee charged.')

# shorter alternative
currentAccount = float(input('How much money is in your current Acount?: '))
savingsAccount = float(input('How much money is in your savings Account?: '))
fee = 0.0 if currentAccount > 1000 or savingsAccount > 1500 else 0.15
print(f'The fee is {fee}')