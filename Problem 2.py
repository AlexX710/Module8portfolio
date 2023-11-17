# Alex Flores
# November 16, 2023
# The code takes two inputs and prints wether the sum is greater than 10, less than 10, or equal to 10.

num1 = int(input("Please enter a number:"))
num2 = int(input("Please enter a number:"))
sum = num1 + num2
def check_sum(num1, num2):
    if sum > 10:
        print("The sum is greater than 10")
    elif sum < 10:
        print("The sum is less than 10")
    else:
        print("The sum is equal to 10")

check_sum(num1, num2)
