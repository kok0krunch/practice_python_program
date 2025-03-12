# Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
   
numbers = []

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

# Find numbers that appear only once
unique_numbers = [num for num in numbers if numbers.count(num) == 1]

# Display the result
if unique_numbers:
    print("Numbers that don't have duplicates:", unique_numbers)
else:
    print("No unique numbers found.")