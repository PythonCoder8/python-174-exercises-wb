import sys
'''
Exercise 10: Arithmetic
Create a program that reads two integers, a and b, from the user. Your program must compute and display:

The sum of a and b
The difference when b is subracted from a
The product of a and b
'''

try:
    int_a = int(input('Enter an integer: '))
    int_b = int(input('Enter another integer: '))
except:
    sys.exit('Both of them weren\'t integers.')

print(f'The sum of both numbers is {int_a + int_b}')
print(f'When subtracting the second number from the first the difference is {int_a - int_b}')
print(f'The product of both numbers is {int_a}')
