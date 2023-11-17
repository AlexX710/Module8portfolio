# Alex Flores
# November 16, 2023
# The program takes two inputs and prints out wether they are equal or not

num1 = int(input("Please enter a number:"))
num2 = int(input("Please enter a number:"))

def check(num1, num2):
    if num1 == num2:
        print("The numbers are equal")
    else:
        print("The numbers are not equal")
check(num1, num2)