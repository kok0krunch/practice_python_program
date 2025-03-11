# Create a program that ask user to input 2 numbers. Print the smaller number.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second numer: "))

smaller_num = min(num1, num2)

print(f"The smaller number is {smaller_num}.")