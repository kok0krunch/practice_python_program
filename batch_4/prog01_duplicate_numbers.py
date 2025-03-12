# Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

numbers = []

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)
    
duplicates = set()
seen = set()
for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)