# Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

first_num = int(input("Enter number 1: "))

minus_allnum = first_num

for i in range(2,11):
    num = int(input(f"Enter number {i}: "))
    minus_allnum -= num

print(f"The result of the first number minus all numbers is: {minus_allnum}.")