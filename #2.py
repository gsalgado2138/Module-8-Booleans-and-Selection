# Giovanni Salgado
#11/21/21
#function that takes two inputs from a user and prints whether the sum is greater than 10, less than 10, or equal to 10.
G = int(input('enter a number: '))
I = int(input('enter a different number: '))
O = 10
if G + I > O:
    print('number is greater than 10')
if G + I < O:
    print('number is less than 10')
if G + I == O:
    print('the number is equal to 10')
