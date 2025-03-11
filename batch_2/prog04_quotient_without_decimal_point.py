# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 // num2

print(f"The quotient of {num1} and {num2} is {result}.")