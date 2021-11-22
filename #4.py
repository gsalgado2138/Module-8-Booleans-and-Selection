# Giovanni Salgado
# 11/21/21
# – Write a function that takes a year as a parameter and returns True if the year is a leap year.
# False if it is otherwise.
def is_leap(year):
    leap = False
    if (year % 4 == 0) and (year % 100 != 0):
        leap = True
    elif (year % 100 == 0) and (year % 400 != 0):
        leap = False
    elif (year % 400 == 0 ):
        leap = 'yes a leap year'
    else:
        leap = 'no not a leap year'
        return leap

year = int(input('enter year: '))
print(is_leap(year))