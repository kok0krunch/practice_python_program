# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
    
if numbers:
    print("The highest number entered is:", max(numbers))
else:
    print("No valid numbers were entered.")