'''
Exercise 11: Fuel Efficiency
In the United States, fuel efficiency for vehicles is normally expressed in miles-per-
gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
'''

import sys

try:
    fuelEfficiencyMPG = float(input('What is the fuel efficiency for your vehicle in miles per gallon (MPG)?: '))
except:
    sys.exit('You should enter a integer or a decimal as your answer.')

print(f'The fuel efficiency for your car in liters-per-hundred-kilometers (L/100 km) is {fuelEfficiencyMPG * 235.215} L/100 km.')
