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
