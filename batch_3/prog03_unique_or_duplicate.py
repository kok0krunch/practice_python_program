# Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

unique_numbers = set()

while True:
    try:
        num = int(input("Enter a number: "))
        if num in unique_numbers:
            print("Duplicate")
        else:
            print("Unique")
            unique_numbers.add(num)
    except ValueError:
        print("Invalid input.")
        break