# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

number = ()

while True:
    try:
        num = int(input("Enter a number: "))
        number.append(num)
    except ValueError:
        break   