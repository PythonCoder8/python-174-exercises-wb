import sys

try:
    widgets = int(input('How many widgets are you buying?: '))
    gizmos = int(input('How many gizmos are you buying?: '))

except:
    sys.exit('You must enter a number in order for the program to work.')

total_grams = (widgets * 75) + (gizmos * 112)