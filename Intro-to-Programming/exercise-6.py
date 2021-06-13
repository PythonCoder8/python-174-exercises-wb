str_cost = input('How much did you pay at the restaurant (without tax or tip)?: $')

try:
    float_cost = float(str_cost)
except ValueError:
    print('You didn\'t enter a number or decimal for the cost like you should\'ve.')

total_cost = (0.31 * float_cost) + float_cost
print(f'The total cost is {total_cost}.')
