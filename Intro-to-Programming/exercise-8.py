'''
Exercise 8: Widgets and Gizmos
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.
'''

import sys

try:
    widgets = int(input('How many widgets are you buying?: '))
    gizmos = int(input('How many gizmos are you buying?: '))

except:
    sys.exit('You must enter a number in order for the program to work.')

total_grams = (widgets * 75) + (gizmos * 112)
