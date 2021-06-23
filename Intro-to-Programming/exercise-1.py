'''
Exercise 1: Mailing Address
Create a program that displays your name and complete mailing address formatted in
the manner that you would usually see it on the outside of an envelope. Your program
does not need to read any input from the user.
'''
recipentName = input('Enter your name: ')
homeAddress = input('Enter your home address: ')
streetName = input('Enter your street name: ')
city = input('Enter the name of the city that you live in: ')
province = input('Enter the name of the province/state that you live in: ')
postalCode = input('Enter your postal code/zip code: ')
country = input('Enter the country that you live in: ')
print(f'\nMailing address:\n\n{recipentName}\n{homeAddress}{streetName}\n{city} {province} {postalCode}\n{country}')
