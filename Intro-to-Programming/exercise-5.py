import sys
small_cont = input('How many containers hold 1 litre or less?: ')
large_cont = input('How many containers hold more than 1 litre?: ')

try:
    total_refund = (int(small_cont) * 0.10) + (int(large_cont) * 0.25)
except:
    sys.exit('You didn\'t enter a number like you should\'ve.')

print(f'The total refund is ${total_refund}')
