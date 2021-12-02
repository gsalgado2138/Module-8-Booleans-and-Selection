#Giovanni Salgado
#11/21/21
#a function that takes two inputs from a user and prints whether they are equal or not.
'''
1. define function
2. input statements
3. call the function

G = int(input('enter a number: '))
H = int(input('enter a different number: '))
if G == H:
    print('number are equal')
else:
    print('number are not equal')
'''
def equal_number(x,y):
    if num1 == num2:
        print("The two numbers are equal to each other")
    else:
        print("The numbers are not equal. Try again.")
    
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
equal_number(num1, num2)
