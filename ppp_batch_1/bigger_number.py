# Create a program that ask user to input 2 numbers. Print the bigger number.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"The bigger number is {num1}.")
elif num1 < num2:
    print(f"The bigger number is {num2}")
else:
    print("Both numbers re equal.")