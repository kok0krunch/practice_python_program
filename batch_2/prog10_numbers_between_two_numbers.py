# Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    num1, num2 = num2, num1  

print(f"Numbers between {num1} and {num2} are:")

for num in range(num1 + 1, num2):
    print(num)