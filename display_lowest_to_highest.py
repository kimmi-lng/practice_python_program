#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function
#empty list
numbers = []
#ask for numbers
while True:
    try:
        ask_numb = float(input("Enter a number: "))
        numbers.append(ask_numb)
    except ValueError:
        print("Invalid input")
        break
print(f"From lowest to highest {sorted(numbers)}")
#condition maybe try and exempt for invalid input