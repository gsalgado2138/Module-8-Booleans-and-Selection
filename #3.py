#Giovanni Salgado
#11/21/21
#Write a function that takes a list and prints if the value 5 is in that list
list = [1, 2, 3, 4, 5,]
for item in list:
    if item < 5 :
        print(item)
        
'''
input: list
define function to check whether there is 5 in the list
call function
'''
def checkValue(list):
    value  = 5
    if value in list:
        print('five is in the list')
        print(list)
    else:
        print('five is not the list')

list = [2, 3, 5, 1]
checkValue(list)
