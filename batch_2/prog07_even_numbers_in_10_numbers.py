# Create a program that ask user to input 10 numbers. Print how many are even numbers.

even_count = 0

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
   
    if num % 2 == 0:
        even_count += 1
       
print(f"The number of even numbers is {even_count}.")