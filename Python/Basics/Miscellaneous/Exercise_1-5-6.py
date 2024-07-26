# Exercise 1-5-6
number = int(input('Enter a positive number higher than 1: '))
prime_number = True

if number < 2:
    print('Invalid Input')
    exit()

else:
    for i in range(2,number//2+1):
        if number % i == 0:
            prime_number = False
            print(f'{number} is not a prime number')
            break
    if prime_number == True:
        print(f'{number} is a prime number.')

# shorter alternative with for-else block
number = int(input('Enter a positive number higher than 1: '))

if number < 2:
    print('Invalid Input')
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f'{number} is not a prime number')
            break
    else:
        print(f'{number} is a prime number.')

    
    

