import sys
userInput = input("Enter a number: ")

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
