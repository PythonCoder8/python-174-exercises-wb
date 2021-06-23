'''
Exercise 9: Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.
'''

import sys

try:
    deposited_money = float(input('How much money did you deposit?: '))
except:
    sys.exit('That is not an integer or float.')

interest = 0.04

year1 = (deposited_money * interest) + deposited_money
year2 = (year1 * interest) + year1
year3 = (year2 * interest) + year2

print(f'Your balance after the first year is {round(year1, 2)}.')
print(f'Your balance after the second year is {round(year2, 2)}.')
print(f'Your balance after the third year is {round(year3, 2)}.')