# Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

total_sum = 0

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    total_sum += num

print(f"The sum of all 10 numbers is {total_sum}.")