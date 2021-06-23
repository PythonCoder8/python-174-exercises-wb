'''
Exercise 3: Area of a Room
Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with
'''
length = int(input('Enter the length of the room in feet: '))
width = int(input('Enter the width of the room in feet: '))
print(f'The area of the room is {length * width} square feet.')
