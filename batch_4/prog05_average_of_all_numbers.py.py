# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"The average of all entered numbers is {average}.")
else:
    print("No valid numbers were entered.")