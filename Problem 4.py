# Alex Flores
# November 16, 2023
# The code takes a year and returns true if the year is a leap year, false if otherwise

def leap_year(year):
    if(year % 4 == 0) and (year % 100 != 0):
        return True
    elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        return True
    else:
        return False

year = 2002
if leap_year(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
