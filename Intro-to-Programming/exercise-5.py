'''
Exercise 5: Bottle Deposits
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
    Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.
'''

import sys
small_cont = input('How many containers hold 1 litre or less?: ')
large_cont = input('How many containers hold more than 1 litre?: ')

try:
    total_refund = (int(small_cont) * 0.10) + (int(large_cont) * 0.25)
except:
    sys.exit('You didn\'t enter a number like you should\'ve.')

print(f'The total refund is ${total_refund}')
