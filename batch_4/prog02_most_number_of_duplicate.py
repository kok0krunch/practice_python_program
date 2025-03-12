# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

from collections import Counter

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
    
if numbers:
    count = Counter(numbers)
    most_number = count.most_common(1)[0]
    print(f"The number with the most duplicate is {most_number[0]}, entered {most_number[1]} times.")
else:
    print("All numbers are unique")