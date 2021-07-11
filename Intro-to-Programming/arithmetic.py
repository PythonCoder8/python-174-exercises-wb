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
    int_b = int(input('Enter an integer: '))

except ValueError:
    sys.exit('Invalid input. Both values of input weren\'t integers')

additionFunction = lambda a, b: a + b
print(f'Sum of the two numbers: {additionFunction(int_a, int_b)}')
subtractionFunction = lambda a, b: a - b
print(f'When the second integer is subtracted from the first integer the difference is {subtractionFunction(int_a, int_b)}')
multiplicationFunction = lambda a, b: a * b
print(f'When multiplying both integers the product is {multiplicationFunction(int_a, int_b)}')