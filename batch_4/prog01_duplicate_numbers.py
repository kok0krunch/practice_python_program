# Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

numbers = []

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)