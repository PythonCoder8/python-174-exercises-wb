'''
Exercise 6: Tax and Tip
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
'''

try:
    cost = float(input('How much did you pay at the restaurant (without tax or tip)?: $'))
except ValueError:
    print('You didn\'t enter an integer or decimal for the cost like you should\'ve.')

total_cost = (0.31 * float_cost) + float_cost
print(f'The total cost is {total_cost}.')
