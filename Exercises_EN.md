# 1 Basics

### 1.1 Variables

#### Exercise 1.1.1
Write a series of statements to declare 3 variables a, b and c and assign them the values **1**, **'France'** and **36.2** respectively. The values of these variables should then be displayed on the console.

#### Exercise 1.1.2
Write a series of statements to declare a variable called **message** and initialize it with the value “hello”. Then change this variable to contain the value “how are you”. The program should output the content of the variable to the console after the change.

#### Exercise 1.1.3
Write a series of statements to declare 2 variables **x** and **y** and assign them the values 3 and 8.5. Then convert the type of these variables to strings.
The program should display the type of these variables at the end after the conversion.

#### Exercise 1.1.4
Write a program that asks the user for his weight in kilograms and stores it in a variable. The program should display the weight entered by the user at the end.

#### Exercise 1.1.5
Write a program that accepts two numbers from the user, adds the numbers and displays the result on the console.

#### Exercise 1.1.6
Write a program that accepts two numbers from the user, divides the numbers and displays the result on the console. What happens if the divisor is 0?
a) Use integer division  
b) Use floating point division  

#### Exercise 1.1.7
Write a program that divides two float variables x = 22.0 and y = 7.0 and displays the result on the
console. Use the modulo operator to format the result to three decimal places precision.

### 1.2 Conditionals

#### Exercise 1.2.1
Write a program with which you can check whether an entered integer is greater than 5. If so, an output is displayed on the console.

#### Exercise 1.2.2
Write a program that accepts a number from the user and outputs to the console if the number is even or odd.

#### Exercise 1.2.3
In a competition, all participants in the heavyweight class must weight between 235 and 265 pounds. Write a program that asks for the competitors weight and then outputs whether he is eligible to participate in the competition or not.

#### Exercise 1.2.4
You enter 7 numbers using the keyboard. At the end, the program displays the the largest number.

#### Exercise 1.2.5
Write a program that checks whether the user's age is over 18 or not. If the user's age is greater than or equal to 18, the program should display 'The user is of legal age', otherwise 'The user is a minor'.

#### Exercise 1.2.6
A bank proceeds according to the following rule:
If a customer has a balance of more than 1,000 euros in their current account or a balance of more than 1,500 euros in their savings account, no check fee is charged. Otherwise, a fee of 0.15 euros will be charged. Write a program that asks for the balance of the two accounts and then outputs how much the fee is.

#### Exercises 1.2.7
A parcel service charges 3.00 euros shipping costs up to a weight of
10 kilos (inclusive). Above this weight, an additional 0.25 euros must be paid for each kilo. Write a program that asks the user for the weight of the shipment and then displays the shipping costs.

Weight of the shipment: 11  
Shipping costs: 3.25 euros  

#### Exercise 1.2.8
Write a program to calculate values from Euro to DM and vice versa. The user should be asked for the amount and into which currency the amount should be converted. The character 'e' should be evaluated for the calculation DM -> Euro. If the character entered, is a different character, the calculation should be Euro -> DM.

The formula you need for this is Euro = DM/1.95583 or DM = Euro * 1.95583

#### Exercise 1.2.9
Change the program from exercise 1.2.8 in a way, that from a weight of 20 kilos, 0.50 euros must be paid for every kilo over 10 kilos.

Weight of the shipment: 25   
Shipping costs: 10.50 euros  

#### Exercise 1.2.10
Write a program that asks the user for his year of birth, coded with two digits, and asks for the current year, also coded with two digits. The program should output the correct age of the user in years.

Year of birth: 62  
Current year: 09  
Your age is: 47  

#### Exercise 1.2.11
Write a program to calculate leap years. Whether a year is a leap year depends on several conditions: If a year is divisible by 400 without a remainder, it is always a leap year. If a year is divisible by 4 but not by 100, it is a leap year. In all other cases, it is not a leap year. Write a program that asks for a year number and then checks whether the year is a leap year. After the check, the program should output if it's a leap year or not.

#### Exercise 1.2.12
The manufacturer of a microwave oven recommends 50% more heating time when heating two portions and double the heating time when heating three portions. Heating more than three portions is not recommended. Write a program that asks the user for the number of portions and the heating time for one portion. The program will then output the recommended heating time. Note: Use four consecutive if queries without an else branch, each of them testing one of four cases: one serving, two servings, three servings, more than three servings.

#### Exercise 1.2.13
Sepp's petrol station is located on the A565 in Bonn on the edge of the Eifel. There is no other filling station for the next 200 kilometers. Write a program that helps drivers to decide whether they should refuel or not.

The program asks:  
- The tank capacity in liters  
- The fuel gauge in percent (full = 100, three-quarters full = 75, etc.)  
- The fuel consumption of the vehicle in km per liter.  

The output of the program is “Refuel!” or “Continue driving”, depending on whether the vehicle has enough fuel for 200 kilometers or not.

    Example:  
    Tank capacity: 12  
    Fuel gauge in %: 50  
    Fuel consumption km/l: 30   
    Refuel!  

### 1.3 Loops

#### Exercise 1.3.1
Write a program that runs in a for loop from 0 to 20. Output the value of the loop counter at each step.

#### Exercise 1.3.2
Write a program that runs via a for loop from 0 to 20 in steps of two. Output the value of the loop counter at each step.

#### Exercise 1.3.3
Write a program that runs in a for loop from 40 to 0. Output the value of the loop counter at each step.

#### Exercise 1.3.4
Write a program that calculates the following sum:
**Sum = 1 + 2 + 3 + 4 + ... + n**. The variable n is of type integer and is to be entered by the user. The result should be output at the end of the calculation.

#### Exercise 1.3.5
Write a program that calculates the product of odd numbers **Product = 1 * 3 * 5 * ... * n**. The variable n is of type integer and is to be entered by the user. The result should be output at the end of the calculation.

#### Exercise 1.3.6
Develop a program that uses a counting loop to display every value between 1 and 100 that is divisible by **7**.

#### Exercise 1.3.7
Write a program that adds integers entered by the user. The program first asks how many numbers are to be added. Then the program asks the user to enter the numbers one after the other. Finally, it displays the result on the screen. Implement the program with a for loop.

#### Exercise 1.3.8
Develop a program with loops that outputs a 7x7 rectangle as follows:

XXXXXXX  
XXXXXXX  
XXXXXXX  
XXXXXXX  
XXXXXXX  
XXXXXXX  
XXXXXXX  

#### Exercise 1.3.9
Develop a program with loops that outputs a 7x7 rectangle as follows:

X------  
-X-----  
--X----  
---X---  
----X--  
-----X-  
------X  

#### Exercise 1.3.10
Develop a program with loops that outputs a 7x7 rectangle as follows:

X-----x  
-X---X-  
--X-X--  
---X---  
--X-X--  
-X---X-  
X-----X  

#### Exercise 1.3.11
Develop a program with loops that outputs a 7x7 rectangle as follows:

X------  
-X-----  
--X----  
---XXXX  
--X----  
-X-----  
X------  

#### Exercise 1.3.12
Develop a program for a one-armed bandit. The player receives 10 coins. Each game costs 1 coin. If two values are the same, the player wins 3 coins; if 3 values are the same, the player immediately receives l0 coins.

Possible display:  

3 6 1 unfortunately lost, credit 9 coins  
3 3 5 3 coins, balance 11 coins  
5 3 5 3 coins, credit 13 coins  

Our machine has 10 figures (0 to 9), generated by the random number generator.  

#### Exercise 1.3.13
Develop a program with loops that outputs a sawtooth blade as follows:
```
*  
***  
*****  
*******  
*********  
***********  
*************  
```
#### Exercise 1.3.14
Develop a program with loops that outputs a sawtooth blade as follows:
```
********  
*******  
******  
*****  
****  
***  
**  
*  
```
#### Exercise 1.3.15
Develop a program with loops, that outputs a Christmas tree as follows:
```
	     *  
	    ***  
	   *****  
	  *******  
	 *********  
	***********  
	    ***  
	    ***  
	    ***  
```
#### Exercise 1.3.16
Develop the following for loops as while loops:

```python
for i in range(7):
    print(i)

for i in [2,5,3,1,4]:
    print(i)
```

#### Exercise 1.3.17
A customer owes his credit card company 1,000.00 euros. The company charges him 1.5% interest per month for the credit granted. He decides to stop using the credit card and to repay his loan monthly with a certain amount **n**. Write a program that asks for the monthly repayment amount and then prints the balance and the total amount of payments for each month until the balance is 0 or less.

**Example:**

Enter the monthly amount: 100   
Month: 1 Balance: 915.0 Total amount: 100.0   
Month: 2 Balance: 828.725 Total amount: 200.0  
Month: 3 Balance: 741.155875 Total amount: 300.0   
Month: 4 Balance: 652.273213125 Total amount: 400.0   
Month: 5 Balance: 562.057311321875 Total amount: 500.0  
Month: 6 Balance: 470.4881709917031 Total amount: 600.0  
Month: 7 Balance: 377.54549355657866 Total amount: 700.0  
Month: 8 Balance: 283.20867595992735 Total amount: 800.0  
Month: 9 Balance: 187.4568060993263 Total amount: 900.0  
Month: 10 Balance: 90.26865819081618 Total amount: 1000.0  
Month: 11 Balance: -8.377311936321576 Total amount: 1100.0  

Calculate the monthly interest based on the balance.
Then calculate the new balance by adding the interest and subtracting the amount repaid.

# 2 Data Structures

### 2.1 Arrays

### 2.2 Lists

### 2.3 Dictionaries

### 2.4 Stacks

### 2.5 Queues

### 2.6 Linked Lists


# 3 Algorithms

### 3.1 Sorting

### 3.2 Searching

### 3.3 Recursion

### 3.4 Dynamic Programming

### 3.5 Graph Algorithms


# 4 Advanced Topics

### 4.1 Object-Oriented Programming (OOP)

### 4.2 File I/O

### 4.3 Exception Handling

### 4.4 Regular Expressions

### 4.5 Date and Time

### 4.6 Unit Testing

### 4.7 Web Scraping