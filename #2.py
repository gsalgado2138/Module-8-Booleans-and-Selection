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

'''    
Same as Pb#1
Define function: sum of two inputs are compared to 10
Get input
Call function with passing the two inputs.
'''
def numbercomparsion(a, b):
   if a + b > 10:
        print("sum of {} and {} is greater than 10. ".format(a, b))
   elif a + b < 10:
        print("sum of {} and {} is less than 10. ".format(a, b))
   else:
        print("sum of {} and {} is equal to 10. ".format(a, b))

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
numbercomparison(a,b)
