# Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

numbers = []
duplicates = set()

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    if num not in duplicates:
        numbers.append(num)
        duplicates.add(num)
    
print("Numbers entered (duplicates are displayed only once):", numbers)