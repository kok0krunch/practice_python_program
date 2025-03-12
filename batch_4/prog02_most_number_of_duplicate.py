# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

from collections import Counter

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break