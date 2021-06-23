'''
Exercise 4: Area of a Field
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
'''

import sys
length =  input('Enter the length of the field (feet): ')
width = input('Enter the width of the field (feet): ')

try:
    int_length = int(length)
except:
    sys.exit('You didn\'t enter a number like you should\'ve.')

try:
    int_width = int(width)
except:
    sys.exit('You didn\'t enter a number like you should\'ve.')


area = length * width
print(f'There are {area / 43560} acres in the field')
