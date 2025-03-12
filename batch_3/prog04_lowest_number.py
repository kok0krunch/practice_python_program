# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

numbers = []
    
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input. Enter a number.")
        break