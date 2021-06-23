'''
Exercise 7: Sum of the first n positive integers
Write a program that reads a positive integer, n, from the user and then displays the
sum of all the integers from one to n. The sum of the first n positive integers can be
calculated using the formula:

sum = (n)(n + 1) divided by 2
(I didn't use the formula)
'''
import sys
userInput = input("Enter a positive integer: ")

if isinstance(userInput, float) == True:
    sys.exit("Decimals are not allowed. Only whole numbers are.")

try:
    userNumber = int(userInput)
except:
    sys.exit("Your input is not a number.")

userSum=0

for i in range(1,userNumber+1):
    userSum += i

print(f"The sum of the numbers from 1 to {userInput} is {userSum}.")
